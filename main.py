import sys
import random
import pyperclip
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QComboBox

def generate_router_mac_address(oui):
    remaining_part = ':'.join('%02x' % random.randint(0, 255) for _ in range(3))
    return oui + ':' + remaining_part.upper()

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Router MAC Address Generator')
        self.setGeometry(300, 300, 350, 150)
        layout = QVBoxLayout()

        self.label = QLabel('Select a company and generate a MAC address', self)
        layout.addWidget(self.label)

        self.comboBox = QComboBox(self)
        self.ouis = {
            'Cisco Systems': '00:1D:AA',
            'Belkin': '00:1C:DF',
            'NETGEAR': '44:94:FC',
            'TP-Link': 'E8:94:F6',
            'D-Link': '00:1E:58',
            'Cisco Meraki': '30:23:03',
            'Ubiquiti': 'F0:9F:C2'
        }
        for company in self.ouis.keys():
            self.comboBox.addItem(company)
        layout.addWidget(self.comboBox)

        generate_btn = QPushButton('Generate MAC Address', self)
        generate_btn.clicked.connect(self.on_click_generate)
        layout.addWidget(generate_btn)

        copy_btn = QPushButton('Copy to Clipboard', self)
        copy_btn.clicked.connect(self.on_click_copy)
        layout.addWidget(copy_btn)

        self.setLayout(layout)

    def on_click_generate(self):
        selected_company = self.comboBox.currentText()
        selected_oui = self.ouis[selected_company]
        self.mac_address = generate_router_mac_address(selected_oui)
        self.label.setText(self.mac_address)

    def on_click_copy(self):
        pyperclip.copy(self.mac_address)
        self.label.setText('MAC Address copied to clipboard!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
