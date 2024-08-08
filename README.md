# Router MAC Address Generator

This application features a user-friendly graphical interface for generating MAC addresses that resemble those used by leading router manufacturers such as Cisco, NETGEAR, TP-Link, and others. It is developed with Python and utilizes the PyQt5 framework.

## Prerequisites

Ensure Python is installed on your machine (Python 3.6 or newer is recommended). Additionally, you will need PyQt5, which can be installed via pip.

## Installation

1. **Obtain the Source Code:**
   Clone the repository or download the source files:
   ```bash
   git clone https://github.com/JPShag/RTMAC.git
   cd RTMAC
   ```

2. **Install Dependencies:**
   Install PyQt5 using pip:
   ```bash
   pip install PyQt5 pyperclip
   ```

## Running the Application

Execute the following command within the directory containing the script to start the application:
```bash
python main.py
```

## Usage

When you launch the application, you will be presented with a dropdown menu to select a router manufacturer and a button to generate a MAC address. Selecting a manufacturer and clicking the button will produce a MAC address based on the chosen manufacturer's OUI, which will then be displayed.

## Features

- **Interactive GUI**: Provides a straightforward and interactive interface.
- **Customizable MAC Address Generation**: Allows selection of specific manufacturers for MAC address generation.
- **Copy to Clipboard**: Includes a feature to directly copy the generated MAC address to the clipboard.

## Contributing

Your contributions are encouraged and greatly appreciated. You can participate by:
- Reporting bugs
- Proposing new features
- Submitting pull requests with bug fixes or enhancements

## License

This project is released under the MIT License. For more details, see the [LICENSE](LICENSE) file included with the repository.
