# QR Code Maker in Python

This is a simple QR Code generator built using Python. It allows users to create QR codes for different types of data, such as URLs, text, phone numbers, SMS messages, emails, locations (latitude and longitude), and Wi-Fi credentials.

## Features

- Generate QR codes for the following data types:
  - URL
  - Text
  - Phone Number
  - SMS
  - Email
  - Location (Latitude, Longitude)
  - Wi-Fi credentials (SSID, Encryption, Password, Hidden/Visible)
  
- Save the generated QR code as an image file (e.g., `.png`).

## Requirements

- Python 3.x
- `qrcode` library

## Installation

1. Clone the repository or download the project files:

    ```bash
    git clone https://github.com/yourusername/qrcode-maker.git
    cd qrcode-maker
    ```

2. Install the required Python library:

    ```bash
    pip install qrcode[pil]
    ```

## How to Use

1. Run the `main.py` script:

    ```bash
    python main.py
    ```

2. Follow the on-screen menu to select the type of QR code you want to generate:
   - `1. URL` — Enter the URL to generate a QR code.
   - `2. Text` — Enter the text for the QR code.
   - `3. Phone Number` — Enter a phone number in the format `tel:+<number>`.
   - `4. SMS` — Enter a phone number and a message.
   - `5. Email` — Enter the email address.
   - `6. Location` — Enter the latitude and longitude.
   - `7. Wi-Fi` — Enter the Wi-Fi SSID, encryption type, password, and whether the network is hidden.

3. After providing the required information, you will be prompted to specify the file name for the QR code image.

4. The generated QR code will be saved in the specified file.

## Example Usage

Here is a step-by-step example of generating a QR code for a URL:

1. Run the program:
   
    ```bash
    python main.py
    ```

2. Select the type of QR code (`1` for URL) from the menu:
   
    ```
    1. URL
    ```

3. Enter the URL, e.g., `https://example.com`.

4. Enter the file name to save the QR code (e.g., `qrcode.png`).

5. The QR code will be generated and saved as `qrcode.png`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Author

- **Bishworaj Poudel**  
  - [GitHub](https://github.com/bishworajpoudelofficial)
  - [Website](https://brp.com.np)
  - [LinkedIn](https://linkedin.com/in/bishworajpoudelofficial)
  - [YouTube](https://youtube.com/technologychannel)

Feel free to contribute to the project by submitting a pull request or reporting issues.
