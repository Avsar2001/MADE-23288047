#!/bin/bash

# Install required packages from requirements.txt
pip3 install --upgrade pip
pip3 install -r ../requirements.txt

# Run Python collection pipeline
python3 data_collection.py