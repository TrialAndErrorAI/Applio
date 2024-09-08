#!/bin/bash

# Clean the staging area 

echo "Cleaning the staging area" 

git clean -df

# Take the commit id from the argument

commit_id=$1

echo "Commit id provided: $commit_id"

# if no commit id is provided Revert to one commit before the latest commit

if [ -z "$commit_id" ]
then
    echo "No commit id provided. Reverting to one commit before the latest commit"
    git reset --hard HEAD^
else
    echo "Reverting to commit id: $commit_id"
    git reset --hard $commit_id
fi

# Clean the staging area

echo "Cleaning the staging area"

git clean -df

# Restart the master Gunicorn process

echo "Restarting the master Gunicorn process"

cat applio.pid | xargs kill -HUP