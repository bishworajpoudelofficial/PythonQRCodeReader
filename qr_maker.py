import qrcode

# Function to create and save QR Code
def create_qr(data, file_name):
    img = qrcode.make(data)
    img.save(file_name)
    print(f"QR Code saved as {file_name}")

# Function to get input for each QR code type
def get_qr_data(choice):
    if choice == "1":
        return input("Enter URL: ")
    elif choice == "2":
        return input("Enter Text: ")
    elif choice == "3":
        phone = input("Enter Phone Number: ")
        return f"tel:{phone}"
    elif choice == "4":
        phone = input("Enter Phone Number: ")
        message = input("Enter SMS Message: ")
        return f"smsto:{phone}:{message}"
    elif choice == "5":
        email = input("Enter Email Address: ")
        return f"mailto:{email}"
    elif choice == "6":
        latitude = input("Enter Latitude: ")
        longitude = input("Enter Longitude: ")
        return f"geo:{latitude},{longitude}"
    elif choice == "7":
        ssid = input("Enter SSID (Wi-Fi name): ")
        encryption = input("Enter encryption type (WPA, WEP, or leave blank for none): ")
        password = input("Enter password (leave blank if no password): ")
        hidden = input("Is the network hidden? (true/false): ").lower()
        encryption_type = encryption if encryption else "nopass"
        hidden_value = "true" if hidden == "true" else "false"
        return f"WIFI:S:{ssid};T:{encryption_type};P:{password};H:{hidden_value};"
    else:
        return None

# Function to display the menu and get user choice
def display_menu():
    print("\nQR Code Maker")
    print("1. URL")
    print("2. Text")
    print("3. Phone Number")
    print("4. SMS")
    print("5. Email")
    print("6. Location")
    print("7. Wi-Fi")
    print("0. Exit")
    return input("Choose QR Code Type: ")

# Main program logic
def main():
    while True:
        choice = display_menu()
        if choice == "0":
            print("Exiting...")
            break
        
        qr_data = get_qr_data(choice)
        
        if qr_data:
            file_name = input("Enter file name (e.g., 'qrcode.png'): ")
            create_qr(qr_data, file_name)
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
