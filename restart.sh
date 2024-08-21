#!/bin/bash

# Restart the master Gunicorn process

pgrep -f "python app.py" | xargs kill -HUP