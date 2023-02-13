#!/bin/bash
brew install tesseract
brew install poppler
arch -arm64e brew install --build-from-source mecab
python3.10 -m venv venv --upgrade-deps
source venv/bin/activate
pip cache purge # Delete cache files from pervious installations
ARCHFLAGS='-arch arm64' pip install --compile --use-pep517 -r requirements.txt