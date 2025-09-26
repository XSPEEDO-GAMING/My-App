import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplashScreen
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Your Site Pro - Online App")
        self.setGeometry(100, 100, 1200, 800)

        # متصفح مدمج
        self.browser = QWebEngineView()

        # ✅ تحميل الموقع من الإنترنت باستخدام QUrl
        self.browser.load(QUrl("https://xspeedo-gaming.github.io/Your-Site-Pro/"))

        self.setCentralWidget(self.browser)


if __name__ != "_main_":
    app = QApplication(sys.argv)

    # شاشة ترحيب
    splash_pix = QPixmap(400, 300)
    splash_pix.fill(Qt.white)

    splash = QSplashScreen(splash_pix)
    splash.setFont(QFont("Arial", 18))
    splash.showMessage("🚀 Your Site Pro جاري تشغيل", Qt.AlignCenter, Qt.black)
    splash.show()

    # بعد 3 ثواني يفتح البرنامج
    window = MainWindow()
    QTimer.singleShot(3000, splash.close)
    QTimer.singleShot(3000, window.show)


    sys.exit(app.exec_())
