#!/bin/bash

# Install required packages from requirements.txt
pip install --upgrade pip
pip install -r ../requirements.txt

# Run Python collection pipeline
python3 data_collection.py

# Run your Python test file 
pytest test_data_collection.py