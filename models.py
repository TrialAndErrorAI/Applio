from pydantic import BaseModel

# Define Pydantic models for request bodies
class InferRequest(BaseModel):
    f0up_key: str = "0"
    filter_radius: str = "3"
    index_rate: str = "0.3"
    rms_mix_rate: str = "1"
    protect: str = "0.33"
    hop_length: str = "128"
    f0method: str = "rmvpe"
    input_path: str
    output_path: str
    pth_path: str
    index_path: str
    split_audio: str = "False"
    f0autotune: str = "False"
    clean_audio: str = "False"
    clean_strength: str = "0.7"
    export_format: str = "WAV"
    embedder_model: str = "contentvec"
    embedder_model_custom: str = None
    upscale_audio: str = "False"

class BatchInferRequest(BaseModel):
    f0up_key: str = "0"
    filter_radius: str = "3"
    index_rate: str = "0.3"
    rms_mix_rate: str = "1"
    protect: str = "0.33"
    hop_length: str = "128"
    f0method: str = "rmvpe"
    input_folder: str
    output_folder: str
    pth_path: str
    index_path: str
    split_audio: str = "False"
    f0autotune: str = "False"
    clean_audio: str = "False"
    clean_strength: str = "0.7"
    export_format: str = "WAV"
    embedder_model: str = "contentvec"
    embedder_model_custom: str = None
    upscale_audio: str = "False"

class TTSRequest(BaseModel):
    tts_text: str
    tts_voice: str
    tts_rate: str = "0"
    f0up_key: str = "0"
    filter_radius: str = "3"
    index_rate: str = "0.3"
    rms_mix_rate: str = "1"
    protect: str = "0.33"
    hop_length: str = "128"
    f0method: str = "rmvpe"
    output_tts_path: str
    output_rvc_path: str
    pth_path: str
    index_path: str
    split_audio: str = "False"
    f0autotune: str = "False"
    clean_audio: str = "False"
    clean_strength: str = "0.7"
    export_format: str = "WAV"
    embedder_model: str = "contentvec"
    embedder_model_custom: str = None
    upscale_audio: str = "False"

class PreprocessRequest(BaseModel):
    model_name: str
    dataset_path: str
    sampling_rate: str
    cpu_cores: str = None

class ExtractRequest(BaseModel):
    model_name: str
    rvc_version: str = "v2"
    f0method: str = "rmvpe"
    pitch_guidance: str = "True"
    hop_length: str = "128"
    cpu_cores: str = None
    sampling_rate: str
    embedder_model: str = "contentvec"
    embedder_model_custom: str = None

class TrainRequest(BaseModel):
    model_name: str
    rvc_version: str = "v2"
    save_every_epoch: str
    save_only_latest: str = "False"
    save_every_weights: str = "True"
    total_epoch: str = "1000"
    sampling_rate: str
    batch_size: str = "8"
    gpu: str = "0"
    pitch_guidance: str = "True"
    pretrained: str = "True"
    custom_pretrained: str = "False"
    g_pretrained_path: str = None
    d_pretrained_path: str = None
    overtraining_detector: str = "False"
    overtraining_threshold: str = "50"
    sync_graph: str = "False"
    cache_data_in_gpu: str = "False"

class IndexRequest(BaseModel):
    model_name: str
    rvc_version: str = "v2"

class ModelExtractRequest(BaseModel):
    pth_path: str
    model_name: str
    sampling_rate: str
    pitch_guidance: str
    rvc_version: str = "v2"
    epoch: str
    step: str

class ModelInformationRequest(BaseModel):
    pth_path: str

class ModelBlenderRequest(BaseModel):
    model_name: str
    pth_path_1: str
    pth_path_2: str
    ratio: str = "0.5"

class DownloadRequest(BaseModel):
    model_link: str

class PrerequisitesRequest(BaseModel):
    pretraineds_v1: str = "True"
    pretraineds_v2: str = "True"
    models: str = "True"
    exe: str = "True"

class AudioAnalyzerRequest(BaseModel):
    input_path: str
