import qrcode

def generateQRCode(urlString: str, fileName: str) -> None:
    """
    Generates a QR code from the provided URL and saves it as an image file.

    Parameters:
    urlString (str) - The URL to encode into the QR code.
    fileName (str) - The name of the file to save the QR code image.

    """
    try:
        # Create a QRCode object with specific parameters
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        # Add the data (URL) to the QR code
        qr.add_data(urlString)
        
        # Generate the QR code
        qr.make(fit=True)
        
        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Ensure the filename ends with .png
        if not fileName.lower().endswith('.png'):
            fileName += '.png'
        
        # Save the image
        img.save(fileName)
        print(f"QR code saved to {fileName}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt user for URL and filename
    urlString = input("Enter your URL: ")
    fileName = input("Enter file name: ")
    
    # Generate the QR code
    generateQRCode(urlString, fileName)
