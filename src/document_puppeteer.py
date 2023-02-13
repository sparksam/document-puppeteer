import tempfile
from pathlib import Path

import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import time
import os
import shutil
from TTS.api import TTS as tts


def init():
    # TODO implement this method.
    pass


def create_storage_dir() -> str:
    """
    Create  a storage folder in the temp folder

    Returns:
        str: storage Directory
    """
    temp_dir = tempfile.gettempdir()
    storage_dir = f"{os.sep.join([temp_dir, str(time.time())])}"
    # TODO fail if the folder could not be created
    if not os.path.exists(storage_dir):
        os.makedirs(storage_dir)
    return storage_dir


def pdf_to_images(pdf_path: str) -> tuple:
    """ Takes a pdf as an input and create for each page of the document an image in the tmp folder

    Args:
        pdf_path (str): Path to the pdf

    Returns:
        tuple: Returns the storage folder and the list of images names
    """
    # TODO Handle exceptions
    pdf_file = Path(pdf_path)
    images = []
    print(f"Reading pdf document: {pdf_path}")
    # Read the PDF pages at 500 DPI
    pdf_pages = convert_from_path(pdf_path=pdf_file, dpi=500)
    print(f"Document has {len(pdf_pages)} pages.")
    # Read through the PDF pages and convert them to images
    storage_dir = create_storage_dir()
    print(f"The storage folder is {storage_dir}")
    for page_enumeration, page in enumerate(pdf_pages, start=1):
        filename = f"page_{page_enumeration:03}.jpg"
        file_path = f"{os.sep.join([storage_dir,filename])}"
        print(f"Saving {file_path}")
        page.save(file_path, "JPEG")
        images.append(filename)
    return storage_dir, images


def convert_images_to_text(storage_dir: str, images: list) -> str:
    """
    Convert images to text using Tesseract

    Args:
        storage_dir (str): The Storage directory
        images (list): List of images

    Returns:
        str: Return the content of the images passed as input
    """
    # TODO Handle exceptions
    text = ""
    for image_enumeration, image in enumerate(images, start=1):
        print(f"Processing image {image}")
        file_path = f"{os.sep.join([storage_dir, image])}"
        text += str(((pytesseract.image_to_string(Image.open(file_path))))
                    ).replace("-\n", "")
    return text


def clean_tmp_file(storage_dir: str):
    """ Delete the temporary file used

    Args:
        storage_dir (str): The folder used for storage
    """
    # TODO Handle exceptions
    if os.path.exists(storage_dir):
        print(f"Delete temporary storage folder {storage_dir}")
        shutil.rmtree(storage_dir)


def save_output(output_file: str, ocr_content: str):
    with open(output_file, "w") as file:
        file.write(ocr_content)


def text_to_speech(output_file: str, ocr_content: str):
    # List available 🐸TTS models and choose the first one
    tts_models = tts.list_models()
    print(f"TTS available models: {tts_models}")
    # model_name = 'tts_models/en/ek1/tacotron2'
    model_name = tts_models[0]
    
    # Init TTS
    tts_engine = tts(model_name=model_name, progress_bar=True, gpu=False)
    # Run TTS
    # ❗ Since this model is multi-speaker and multi-lingual, we must set the target speaker and the language
    # Text to speech with a numpy output
    # wav = tts.tts("This is a test! This is also a test!!",
    #               speaker=tts.speakers[0], language=tts.languages[0])
    # Text to speech to a file
    # tts_engine.tts_to_file(text="Hello world!",
    #                 speaker=tts.speakers[0], language=tts.languages[0], file_path="output.wav")


if __name__ == "__main__":
    # # TODO add arguments to pass to CLI
    # # The current values are for testing purposes.

    # filename = "c4611_sample_explain"
    # out_file = os.sep.join(["tests/docs/text", f"{filename}.txt"])

    # # out_file = "A17_FlightPlan.pdf"
    # storage_dir, images = pdf_to_images(f"tests/docs/pdfs/{filename}.pdf")
    # ocr_content = convert_images_to_text(
    #     storage_dir=storage_dir, images=images)
    # save_output(output_file=out_file, ocr_content=ocr_content)
    # clean_tmp_file(storage_dir=storage_dir)
    
    text_to_speech(None,None)
    # pdf_to_images("tests/docs/pdfs/")
