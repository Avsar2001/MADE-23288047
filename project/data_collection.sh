#!/bin/bash

# Export kaggle.json to os env for Kaggle authentication
KAGGLE_JSON_PATH="./kaggle.json"
KAGGLE_CONFIG_DIR=$(dirname "$KAGGLE_JSON_PATH")
export KAGGLE_CONFIG_DIR

# Install required packages from requirements.txt
pip3 install --upgrade pip
pip3 install -r ../requirements.txt

# Run Python collection pipeline
python3 ./data_collection.py