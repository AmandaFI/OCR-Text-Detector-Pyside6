# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ocr_detector_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_Form_OCR_Detector(object):
    def setupUi(self, Form_OCR_Detector):
        if not Form_OCR_Detector.objectName():
            Form_OCR_Detector.setObjectName(u"Form_OCR_Detector")
        Form_OCR_Detector.resize(601, 698)
        Form_OCR_Detector.setStyleSheet(u"#frame_2{\n"
"background-color: #1d232f;\n"
"border: 1px solid #009688;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"#frame{\n"
"background-color: #1d232f;\n"
"border: 1px solid #009688;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"#Form_OCR_Detector{\n"
"background-color: #171c26\n"
"}")
        self.verticalLayout = QVBoxLayout(Form_OCR_Detector)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(7, 7, 7, 7)
        self.frame = QFrame(Form_OCR_Detector)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, -1, 5, 0)
        self.label_title = QLabel(self.frame_3)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: #f1f7ff;")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_title)

        self.label_image = QLabel(self.frame_3)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setMinimumSize(QSize(350, 350))
        self.label_image.setFrameShape(QFrame.Panel)
        self.label_image.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.label_image)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 15)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 5, -1)
        self.pushButton_crop = QPushButton(self.frame_4)
        self.pushButton_crop.setObjectName(u"pushButton_crop")
        self.pushButton_crop.setMinimumSize(QSize(35, 35))
        self.pushButton_crop.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"background-color: #00bca9;\n"
"border: 1px solid #171c26;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #00dfc9;\n"
"	border: 1px solid #171c26;\n"
"	border-radius: 5px;\n"
"    }\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    background: #00d5c0;\n"
"	border: 1px solid #171c26;\n"
"	border-radius: 5px;\n"
"    }\n"
"")
        icon = QIcon()
        icon.addFile(u"icons/crop.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_crop.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton_crop)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_upload = QPushButton(self.frame_4)
        self.pushButton_upload.setObjectName(u"pushButton_upload")
        self.pushButton_upload.setMinimumSize(QSize(35, 35))
        self.pushButton_upload.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"background-color: #00bca9;\n"
"border: 1px solid #171c26;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #00dfc9;\n"
"	border: 1px solid #171c26;\n"
"	border-radius: 5px;\n"
"    }\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    background: #00d5c0;\n"
"	border: 1px solid #171c26;\n"
"	border-radius: 5px;\n"
"    }\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"icons/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_upload.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButton_upload)

        self.pushButton_screenshot = QPushButton(self.frame_4)
        self.pushButton_screenshot.setObjectName(u"pushButton_screenshot")
        self.pushButton_screenshot.setMinimumSize(QSize(35, 35))
        self.pushButton_screenshot.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"background-color: #00bca9;\n"
"border: 1px solid #171c26;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #00dfc9;\n"
"	border: 1px solid #171c26;\n"
"	border-radius: 5px;\n"
"    }\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    background: #00d5c0;\n"
"	border: 1px solid #171c26;\n"
"	border-radius: 5px;\n"
"    }\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"icons/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_screenshot.setIcon(icon2)

        self.horizontalLayout.addWidget(self.pushButton_screenshot)

        self.pushButton_camera = QPushButton(self.frame_4)
        self.pushButton_camera.setObjectName(u"pushButton_camera")
        self.pushButton_camera.setMinimumSize(QSize(35, 35))
        self.pushButton_camera.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"background-color: #00bca9;\n"
"border: 1px solid #171c26;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #00dfc9;\n"
"	border: 1px solid #171c26;\n"
"	border-radius: 5px;\n"
"    }\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    background: #00d5c0;\n"
"	border: 1px solid #171c26;\n"
"	border-radius: 5px;\n"
"    }\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"icons/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_camera.setIcon(icon3)

        self.horizontalLayout.addWidget(self.pushButton_camera)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.verticalLayout_2.setStretch(0, 9)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form_OCR_Detector)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 1, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(11)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: #f1f7ff;")

        self.verticalLayout_4.addWidget(self.label)

        self.plainTextEdit_detected_data = QPlainTextEdit(self.frame_5)
        self.plainTextEdit_detected_data.setObjectName(u"plainTextEdit_detected_data")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        self.plainTextEdit_detected_data.setFont(font2)
        self.plainTextEdit_detected_data.setFrameShape(QFrame.Panel)
        self.plainTextEdit_detected_data.setFrameShadow(QFrame.Plain)
        self.plainTextEdit_detected_data.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.plainTextEdit_detected_data)

        self.verticalLayout_4.setStretch(0, 1)

        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 5)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton_clipboard = QPushButton(self.frame_6)
        self.pushButton_clipboard.setObjectName(u"pushButton_clipboard")
        self.pushButton_clipboard.setMinimumSize(QSize(35, 35))
        self.pushButton_clipboard.setToolTipDuration(-1)
        self.pushButton_clipboard.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"background-color: #00bca9;\n"
"border: 1px solid #171c26;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #00dfc9;\n"
"	border: 1px solid #171c26;\n"
"	border-radius: 5px;\n"
"    }\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    background: #00d5c0;\n"
"	border: 1px solid #171c26;\n"
"	border-radius: 5px;\n"
"    }\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"icons/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_clipboard.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.pushButton_clipboard)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.verticalLayout_3.setStretch(0, 5)
        self.verticalLayout_3.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame_2)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Form_OCR_Detector)

        QMetaObject.connectSlotsByName(Form_OCR_Detector)
    # setupUi

    def retranslateUi(self, Form_OCR_Detector):
        Form_OCR_Detector.setWindowTitle(QCoreApplication.translate("Form_OCR_Detector", u"OCR Text Detector", None))
        self.label_title.setText(QCoreApplication.translate("Form_OCR_Detector", u"Choose Image for OCR Text Detection", None))
        self.label_image.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_crop.setToolTip(QCoreApplication.translate("Form_OCR_Detector", u"Crop loaded image", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_crop.setText("")
        self.pushButton_upload.setText("")
        self.pushButton_screenshot.setText("")
        self.pushButton_camera.setText("")
        self.label.setText(QCoreApplication.translate("Form_OCR_Detector", u"Detected Text:", None))
#if QT_CONFIG(tooltip)
        self.pushButton_clipboard.setToolTip(QCoreApplication.translate("Form_OCR_Detector", u"Copy to clipboard", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_clipboard.setText("")
    # retranslateUi

