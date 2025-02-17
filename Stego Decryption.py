import cv2

# Read the encrypted image
img = cv2.imread("encryptedImage.jpg")  # Replace with the correct encrypted image path

# Get the passcode to verify decryption
pas = input("Enter passcode for Decryption: ")

# Hardcoded passcode for security verification
password = "your_secure_password_here"  # Replace with the same passcode used during encryption

# Decrypt the message if the passcode is correct
if password == pas:
    message = ""
    n = 0
    m = 0
    z = 0

    # Loop through the image and decrypt the message
    for i in range(0, img.size, 3):  # Access the image data (every 3 elements for R, G, B)
        message += chr(img[n, m, z])
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    # Output the decrypted message
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
