import sys
from PySide6 import QtWidgets, QtGui
from Layout.ocr_detector_ui import Ui_Form_OCR_Detector
import cv2
from PIL import ImageQt
from screenshot_area import Image_Area_Selection
from PIL.ImageQt import ImageQt
import numpy as np
import pytesseract as ocr
import pyperclip

ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# https://pyimagesearch.com/2021/08/16/installing-tesseract-pytesseract-and-python-ocr-packages-on-your-system/
# https://nanonets.com/blog/ocr-with-tesseract/


class Main_Window(QtWidgets.QWidget, Ui_Form_OCR_Detector):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.initUI()
        self.image_area_selection = Image_Area_Selection()
        self.loaded_img = None

    def initUI(self):
        """Connects the QtWidgets events to their respective functions.
        """
        self.pushButton_upload.clicked.connect(self.upload_image_from_file_manager)
        self.pushButton_camera.clicked.connect(self.capture_live_image)
        self.pushButton_screenshot.clicked.connect(self.screenshot)
        self.pushButton_clipboard.clicked.connect(self.copy_to_clipboard)
        self.pushButton_crop.clicked.connect(self.crop_loaded_img)

    
    def upload_image_from_file_manager(self):
        """Opens the system file manager allowing an local image to be loaded into the application.
        """

        file_path, _filter = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Open file', dir='.', filter="Image Files (*.png *.jpg *.jpeg)") 

        if file_path:
            img = cv2.imread(file_path)
            self.loaded_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            self.show_img_on_interface(img_file_path=file_path)

    def capture_live_image(self):
        """Accesses the main camera connected to the system, takes a picture and loads it to the application.
        """
        cam = cv2.VideoCapture(0)

        frame = None
        while True:
            ret, frame = cam.read()
            if not ret:
                ret = self.message_box(message_title='Error.', message='Error capturing image, make sure the camera is connected.')
                break
            break
        cam.release()

        self.loaded_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        height, width, _channel = frame.shape
        bytesPerLine = 3 * width
        qtImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        
        self.show_img_on_interface(img=qtImg)

    def screenshot(self):
        """Allows users to select a certain area of the screen to take a screenshot and load it to the application.
        """
        self.hide()
        roi = self.image_area_selection.select_area()

        self.loaded_img = np.array(roi)

        qtImg = ImageQt(roi)
        self.show_img_on_interface(img=qtImg)

        self.show()

    def show_img_on_interface(self, img=None, img_file_path=None):
        """Displays the image loaded into the application in the interface following the format required by the QtWidget used.

        Args:
            img (PySide6.QtGui.QImage or PIL.ImageQt.ImageQt, optional): Array representing the image loaded into the application. Defaults to None.
            img_file_path (string, optional): Absolute path to the local image loaded into the application. Defaults to None.
        """

        if img:
            print(type(img))
            try:
                self.label_image.setPixmap(QtGui.QPixmap.fromImage(img))
            except:
                _ret = self.message_box(message_title='Error.', message='Error loading image.')
        elif img_file_path:
            try:
                self.label_image.setPixmap(QtGui.QPixmap(img_file_path))
            except:
                _ret = self.message_box(message_title='Error.', message='Error loading image.')
        self.detect_data()

    def crop_loaded_img(self):
        """Opens a new window allowing the loaded image to be cropped into a smaller area.
        """
        if type(self.loaded_img) != type(None):
            r = cv2.selectROI("Select area.'Enter' to save or 'c' to cancel.", cv2.cvtColor(self.loaded_img, cv2.COLOR_BGR2RGB), showCrosshair=False)
            cv2.destroyWindow("Select area.'Enter' to save or 'c' to cancel.")
    
            cropped_image = self.loaded_img[int(r[1]):int(r[1]+r[3]), 
                                int(r[0]):int(r[0]+r[2])]
            
            self.loaded_img = cropped_image
            
            img = np.ascontiguousarray(cropped_image)
            
            height, width, _channel = img.shape
            bytesPerLine = 3 * width
            qtImg = QtGui.QImage(img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
            self.show_img_on_interface(img=qtImg)
            self.detect_data()
        else:
            _ret = self.message_box(message_title='Error.', message='Image required before cropping operation.')

    def detect_data(self):
        """Applies the pytesseract OCR detector to the image loaded into the application.
        """
        if type(self.loaded_img) != type(None):
            data = ocr.image_to_string(self.loaded_img)
            if data:
                self.plainTextEdit_detected_data.setPlainText(data)
            else:
                self.plainTextEdit_detected_data.setPlainText('No text detected.')

    def copy_to_clipboard(self):
        """Copy content fromt QtWidget plainTextEdit_detected_data to the system clipboard.
        """
        pyperclip.copy(self.plainTextEdit_detected_data.toPlainText())


    def message_box(self, message_title, message, _input=False):
        """Generates and shows a QMessageBox with a given message.

        Args:
            message (string): message to be shown.
            message_title (string): title of the messageBox.
            input (bool, optional): used if the user input is needed. Defaults to False.

        Returns:
            (QtWidgets.QMessageBox): user input.
        """
        
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle(message_title)
        msgBox.setText(message)
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)

        if _input:
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            msgBox.setDefaultButton(QtWidgets.QMessageBox.No)
        ret = msgBox.exec()
        return ret
            

if __name__ == '__main__':
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
        window = Main_Window()
        window.show()
        app.exec()