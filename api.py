from fastapi import FastAPI, HTTPException, UploadFile, File
from models import TTSRequest, InferRequest, BatchInferRequest, PreprocessRequest, ExtractRequest, TrainRequest, IndexRequest, ModelExtractRequest, ModelInformationRequest, ModelBlenderRequest, DownloadRequest, PrerequisitesRequest, AudioAnalyzerRequest
import subprocess
import sys
import os

app = FastAPI(debug=True)

# Add the current directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import functions from main.py
from core import (
    run_infer_script, run_batch_infer_script, run_tts_script,
    run_preprocess_script, run_extract_script, run_train_script,
    run_index_script, run_model_extract_script, run_model_information_script,
    run_model_blender_script, run_tensorboard_script, run_download_script,
    run_prerequisites_script, run_audio_analyzer_script
)

# Define API endpoints
@app.get("/health")
async def health():
    return {"message": "Applio is healthy"}

@app.post("/upload")
# accept a file upload and save it to the /assets/audios directory
async def upload(file: UploadFile = File(...)):
    try:
        # save the file to the /assets/audios directory
        file_path = os.path.join(current_dir, "assets", "audios", file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return [file_path]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/infer")
async def infer(request: InferRequest):
    try:
        result = run_infer_script(**request.dict())
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/batch_infer")
async def batch_infer(request: BatchInferRequest):
    try:
        result = run_batch_infer_script(**request.dict())
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/tts")
async def tts(request: TTSRequest):
    try:
        result = run_tts_script(**request.dict())
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/preprocess")
async def preprocess(request: PreprocessRequest):
    try:
        result = run_preprocess_script(**request.dict())
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/extract")
async def extract(request: ExtractRequest):
    try:
        result = run_extract_script(**request.dict())
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/train")
async def train(request: TrainRequest):
    try:
        result = run_train_script(**request.dict())
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/index")
async def index(request: IndexRequest):
    try:
        result = run_index_script(**request.dict())
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/model_extract")
async def model_extract(request: ModelExtractRequest):
    try:
        result = run_model_extract_script(**request.dict())
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/model_information")
async def model_information(request: ModelInformationRequest):
    try:
        result = run_model_information_script(**request.dict())
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/model_blender")
async def model_blender(request: ModelBlenderRequest):
    try:
        result = run_model_blender_script(**request.dict())
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/tensorboard")
async def tensorboard():
    try:
        result = run_tensorboard_script()
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/download")
async def download(request: DownloadRequest):
    try:
        result = run_download_script(**request.dict())
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/prerequisites")
async def prerequisites(request: PrerequisitesRequest):
    try:
        result = run_prerequisites_script(**request.dict())
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/audio_analyzer")
async def audio_analyzer(request: AudioAnalyzerRequest):
    try:
        result = run_audio_analyzer_script(**request.dict())
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6969)