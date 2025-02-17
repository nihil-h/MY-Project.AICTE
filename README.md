Steganography-based Encryption and Decryption
This project demonstrates how to hide a secret message inside an image using steganography and encrypt it for secure transmission. It is divided into two parts:

Encryption: Embeds the encrypted message inside the image.

Decryption: Extracts and decrypts the hidden message from the image.

Features

Encryption: Allows users to input a secret message, which is then encrypted and hidden inside an image file.

Decryption: The secret message can be retrieved from the image, provided the correct passcode is entered.

Security: The message is encrypted using a simple method, and the passcode ensures only authorized decryption.

Technologies Used

Python
OpenCV (cv2)
Image Processing
Project Structure
pgsql
Copy





Steganography-Encryption-Decryption/
│

├── encrypt.py              # Python script for encryption

├── decrypt.py              # Python script for decryption

├── mypic.jpg               # Input image file (for encryption)

├── encryptedImage.jpg      # Output encrypted image (generated after encryption)

└── README.md               # Project documentation (this file)
