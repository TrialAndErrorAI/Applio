#!/bin/bash

printf "\033]0;Application Starter\007"

start_applio() {
  # get the current directory
  current_dir=$(pwd)
  cd /workspace/Applio
  echo "Starting up Applio..."
  sh run-applio.sh 2>&1 | sed 's/^/[Applio] /'
  echo "Applio startup complete."
  cd $current_dir
}

start_audio_manipulator() {
  # get the current directory
  current_dir=$(pwd)
  cd /workspace/AudioManipulator
  echo "Starting up Audio Manipulator..."
  sh start.sh 2>&1 | sed 's/^/[AudioManipulator] /'
  echo "Audio Manipulator startup complete."
  cd $current_dir
}

start_all_apps() {
  start_applio &
  start_audio_manipulator
}

start_all_apps