#!/bin/bash

# Install system dependencies
apt-get update -y && apt-get install -y \
    python3-distutils \
    python3-dev \
    gcc \
    g++ \
    build-essential

# Upgrade pip
pip install --upgrade pip

# Install Python packages
pip install -r requirements.txt
