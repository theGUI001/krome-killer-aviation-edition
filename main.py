from imp import reload
import sys
from turtle import forward
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.webatis.xyz/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Voltar', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Avançar', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        refresh_btn = QAction('Recarregar', self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

        simbrief_btn = QAction('Simbrief', self)
        simbrief_btn.triggered.connect(self.go_simbrief)
        navbar.addAction(simbrief_btn)

        simbrief_btn = QAction('Cartas', self)
        simbrief_btn.triggered.connect(self.go_cartas)
        navbar.addAction(simbrief_btn)

        simbrief_btn = QAction('ATIS', self)
        simbrief_btn.triggered.connect(self.go_atis)
        navbar.addAction(simbrief_btn)

        simbrief_btn = QAction('Rota', self)
        simbrief_btn.triggered.connect(self.go_route)
        navbar.addAction(simbrief_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

    def go_simbrief(self):
        self.browser.setUrl(QUrl("https://www.simbrief.com/"))

    def go_cartas(self):
        self.browser.setUrl(QUrl("https://chartfox.org"))

    def go_atis(self):
        self.browser.setUrl(QUrl("https://www.webatis.xyz/"))

    def go_route(self):
        self.browser.setUrl(QUrl("http://onlineflightplanner.org/"))

    def navigate_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, url):
        self.url_bar.setText(url.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName("Krome Killer")
window = MainWindow()
app.exec_()
