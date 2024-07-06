#!/bin/sh
printf "\033]0;Applio\007"
. .venv/bin/activate

 export PYTORCH_ENABLE_MPS_FALLBACK=1
 export PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0
 
clear
while true; do
    python app.py
    echo "Applio Exited. Restarting Applio in 5 seconds..."
    sleep 5
done
