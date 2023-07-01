# Python GUI for OCR detection with PyTesseract

## Table of Content

1. [Overview](#overview)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Getting Started](#getting-started)

---

## **Overview** <a name="overview"></a>

This project is a desktop application that uses the Optical Character Recognition (OCR) technique to detect text in images.

The user is able to load images into the application in three ways. The first way consists in loading from the local file manager. In the second way, the application allows the user to take a screenshot of certain screen area. The third way is by taking a instant photo using a webcam or camera connected to the machine. Once loaded, the user can crop the image if necessary.

The GUI was build using the PySide6 library and the Qt Designer tool. OCR detection is performed using the PyTesseract package and all image processing is done using the OpenCV library.

## **Technologies** <a name="technologies"></a>

- [PySide6](https://pypi.org/project/PySide6/)
- [Qt Designer](https://doc.qt.io/qt-6/qtdesigner-manual.html)
- [Tesseract](https://github.com/tesseract-ocr/tessdoc)
- [PyTesseract](https://pypi.org/project/pytesseract/)
- [OpenCv](https://docs.opencv.org/4.x/)

## **Installation** <a name="installation"></a>

To run this project the following prerequisites are necessary:

- Python installed
- Tesseract installed
- Required Python packages installed

If your system does not meet the mentioned prerequisites the following instructions may help:

- Install Pyhton from the [official source](https://www.python.org/downloads/)

- Install Tesseract following the [official repository](https://github.com/tesseract-ocr/tessdoc/blob/main/Downloads.md) tutorial.

- Install the required packages for this project using the provided requirements.txt file. Open a terminal inside the project directory and run:

```bash
$ pip install -r requirements.txt
```

## **Getting Started** <a name="getting-started"></a>

If your system meets the mentioned prerequisites just clone this repository and run the following initialization commands:

```bash
$ git clone https://github.com/AmandaFI/OCR-Text-Detector-Pyside6.git
$ cd OCR-Text-Detector-Pyside6
```

Important: If you are not using Windows or installed the Tesseract in a location different from the installation default location, it is necessary to change the Tesseract location path inside the main.py file (line 12) before running the application.

Run the application:

```bash
$ python main.py
```
