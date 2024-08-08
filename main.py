import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

def generate_router_mac_address():
    ouis = [
        '00:1D:AA',  # Cisco Systems
        '00:1C:DF',  # Belkin
        '44:94:FC',  # NETGEAR
        'E8:94:F6',  # TP-Link
        '00:1E:58',  # D-Link
        '30:23:03',  # Cisco Meraki
        'F0:9F:C2',  # Ubiquiti
    ]
    selected_oui = random.choice(ouis)
    remaining_part = ':'.join('%02x' % random.randint(0, 255) for _ in range(3))
    return selected_oui + ':' + remaining_part.upper()

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Router MAC Address Generator')
        self.setGeometry(300, 300, 300, 100)
        layout = QVBoxLayout()

        self.label = QLabel('Click generate to get a router MAC address', self)
        layout.addWidget(self.label)

        btn = QPushButton('Generate MAC Address', self)
        btn.clicked.connect(self.on_click)
        layout.addWidget(btn)

        self.setLayout(layout)

    def on_click(self):
        mac_address = generate_router_mac_address()
        self.label.setText(mac_address)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
