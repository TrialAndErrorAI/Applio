#!/bin/bash

# Clean the staging area 

git clean -df

# Take the latest pull from the repository

git pull

# Restart the master Gunicorn process

cat applio.pid | xargs kill -HUP