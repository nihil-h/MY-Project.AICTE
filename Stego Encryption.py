import cv2
import os
import string

# Read the image
img = cv2.imread("mypic.jpg")  # Replace with the correct image path

# Get the secret message and passcode
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Create dictionaries for encryption
d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Variables to track position in image
n = 0
m = 0
z = 0

# Encrypt the message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)

# Open the image after encryption
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

# Ask for the passcode to complete the encryption process
print("Encryption complete.")
