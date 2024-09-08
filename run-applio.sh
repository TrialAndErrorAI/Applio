#!/bin/sh
printf "\033]0;Applio\007"
. .venv/bin/activate

# Default port
PORT=${1:-6969}

 export PYTORCH_ENABLE_MPS_FALLBACK=1
 export PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0

 # Start the service
echo "Starting Applio Service"
gunicorn -p applio.pid -w 1 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT api:app --timeout 300
