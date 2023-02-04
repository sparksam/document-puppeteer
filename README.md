# Document Puppeteer
Document Puppeteer is a project that manipulates documents of multiple formats (PDF, Doc, Images, Videos), OCR them, correct the grammar, and probably translate it to other languages. 

## Requirements
This project relies on existing tools such as Tesseract and Poppler.
I use an Apple Sillicon Mac for development so here are the instructions used to set the environment
```bash
brew install tesseract
brew install poppler
git clone github.com/sparksam/document_puppeteer
cd document_puppeteer
python3.10 -m venv venv --upgrade-deps
source venv/bin/activate
pip install -r requirements.txt
```

### TODO 
- [ ] Python script that takes documents as input and OCR them
- [ ] Convert Text to speech using Coqui TTS
- [ ] Spellcheck fix 
- [ ] Convert the documents to different other formats. 

### Issues
- [ ] Large documents processing is time and resource cosuming with Poppler and Tesseract. Find ways to improve. Probably reduce the DPI but is that a trade-off for the text accuracy? 

### Authors
- @sparksam ☕️