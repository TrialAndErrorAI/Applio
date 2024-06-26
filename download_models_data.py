# Make an API call to fetch all the voices 

import requests
import json
import os
import boto3
import concurrent.futures
from dataplane import s3_download
from botocore.client import Config

S3Connect = boto3.client('s3', 
             endpoint_url='https://40ad419de279f41e9626e2faf500b6b4.r2.cloudflarestorage.com',
             aws_access_key_id='7da645d13a990ecc11f684221ed975e3',
             aws_secret_access_key='2ed0fe3463962449e5dbc8a66fb1f5ff49e06ecb2badac62120cc2c8caadc3e0',
             config=Config(signature_version='s3v4'),
             region_name='us-east-1')

# API endpoint
BFF_API_URL = "https://api.voxapp.ai"
get_all_voices_url = f"{BFF_API_URL}/get_all_voices"

def download_pretrained_model():
  print("Downloading pretrained model...")
  file_name = 'pretrained_v2.zip'
  
  # check if the folder exists
  if os.path.exists("pretrained_v2"):
    print("Skipping.... Pretrained model folder already exists")
    return
  
  # download the index file
  rs = s3_download(Bucket='vox-ai',
            S3Client=S3Connect,
            LocalFilePath=file_name,
            DownloadMethod="File",
            S3FilePath=file_name)
  
  if rs["result"] != "OK":
    print(f"Pretrained model download failed, Response: {rs}")
    raise Exception("Pretrained model download failed, try again later")
  
  print("Pretrained model zip downloaded successfully")
  
  # Unzip the downloaded file
  os.system(f"unzip {file_name}")
  print("Pretrained model unzipped successfully") 
  
  # Remove the zip file
  os.system(f"rm {file_name}")
  print("Pretrained model zip file removed successfully")

def fetch_all_voices():
  print("Fetching all voices...")
  # Make an API call to fetch all the voices
  response = requests.get(get_all_voices_url)
  data = response.json()
  print(f"Total voices fetched: {len(data)}")
  return data

def download_model_and_index_files(data):
  print("Starting download of model and index files...")
  # Define a function to process a single voice
  def process_voice(voice):
    print(f"Processing voice id {voice['voiceId']}...")
    voice_id = voice['voiceId']
    model_file_path = voice['modelPath']
    index_file_path = voice['indexPath']

    if model_file_path is None or index_file_path is None or model_file_path == "" or index_file_path == "" or not model_file_path.endswith(".pth") or not index_file_path.endswith(".index"):
      print(f"Valid Model or index file path is missing for voice id {voice_id}")
      return voice_id

    model_filename = model_file_path.split('/')[-1]
    index_filename = index_file_path.split('/')[-1]
    
    # check if the model file exists
    if os.path.exists(model_file_path):
      print(f"Skipping.... Model file {model_filename} already exists")
      
    else:
      # download the model file
      rs = download_model_file(voice_id, model_file_path, model_filename)

      if rs["result"] == "Fail":
        print(f"Model file {model_filename} download failed, Response: {rs}")
        return voice_id

      print(f"Model file {model_filename} downloaded successfully, Response: {rs}")

    # download the index file if it does not exist
    if os.path.exists(index_file_path):
      print(f"Skipping.... Index file {index_filename} already exists")
      
    else:
      rs = download_index_file(voice_id, index_file_path, index_filename)

      if rs["result"] == "Fail":
        print(f"Index file {index_filename} download failed, Response: {rs}")
        return voice_id

      print(f"Index file {index_filename} downloaded successfully, Response: {rs}")

  # Split the data into batches of 10
  batches = [data[i:i+10] for i in range(0, len(data), 10)]
  total_records = len(data)
  processed_records = 0
  num_batches = len(batches)
  if len(data) % 10 != 0:
    num_batches += 1
  print(f"Total batches created: {num_batches}")

  # Process each batch in parallel
  with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(process_voice, voice) for batch in batches for voice in batch]
  
    # Wait for all futures to complete
    concurrent.futures.wait(futures)
  
    # Print the progress of each batch
    for i, future in enumerate(futures[:len(batches)]):
      if future.exception() is None:
        print(f"Batch {i+1} completed successfully")
      else:
        print(f"Batch {i+1} failed")
  
      processed_records += len(batches[i])
      print(f"Processed {processed_records} out of {total_records} records")

  # Count the number of successful and failed downloads
  success_count = 0
  failed_count = 0
  failed_voice_ids = []
  for future in futures:
    if future.exception() is None:
      success_count += 1
    else:
      failed_count += 1
      failed_voice_ids.append(future.result())

  # Print the success and failed count
  print(f"Download completed. Success count: {success_count}, Failed count: {failed_count}")

  # Print the list of voice ids that failed to download
  if failed_count > 0:
    print("Failed voice ids:")
    for voice_id in failed_voice_ids:
      print(voice_id)
  

def download_model_file(voice_id, model_file_path, model_filename):

  print(f"Downloading model file {model_filename}... at {model_file_path}")

  # create the directory if it does not exist
  if not os.path.exists(os.path.dirname(model_file_path)):
    os.makedirs(os.path.dirname(model_file_path))

  # download the model file
  rs = s3_download(Bucket='vox-ai-model-pth-files',
            S3Client=S3Connect,
            LocalFilePath=model_file_path,
            DownloadMethod="File",
            S3FilePath=model_filename)
  return rs

def download_index_file(voice_id, index_file_path, index_filename):
  
  print(f"Downloading index file {index_filename}... at {index_file_path}")
  
  # create the directory if it does not exist
  if not os.path.exists(os.path.dirname(index_file_path)):
    os.makedirs(os.path.dirname(index_file_path))

  # download the index file
  rs = s3_download(Bucket='vox-ai-model-index-files',
            S3Client=S3Connect,
            LocalFilePath=index_file_path,
            DownloadMethod="File",
            S3FilePath=index_filename)
  return rs
        
def main():
  # Download the pretrained model
  download_pretrained_model()
  # Call the function to fetch all the voices
  # data = fetch_all_voices()
  # download_model_and_index_files(data)

if __name__ == "__main__":
  main()
