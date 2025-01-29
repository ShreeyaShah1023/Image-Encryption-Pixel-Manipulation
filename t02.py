from PIL import Image
import numpy as np

# Function to encrypt the image
def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to a NumPy array and ensure uint8 dtype
    img_array = np.array(img, dtype=np.uint8)
    
    # Encrypt the array (addition wrapped around at 256)
    encrypted_array = ((img_array.astype(np.int16) + key) % 256).astype(np.uint8)
    
    # Convert the encrypted array back to an image
    encrypted_image = Image.fromarray(encrypted_array)
    
    # Save the encrypted image
    encrypted_image.save("encrypted_image.png")
    print("Image encrypted successfully! Saved as 'encrypted_image.png'.")

# Function to decrypt the image
def decrypt_image(image_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    
    # Convert the image to a NumPy array and ensure uint8 dtype
    img_array = np.array(img, dtype=np.uint8)
    
    # Decrypt the array (subtraction wrapped around at 256)
    decrypted_array = ((img_array.astype(np.int16) - key) % 256).astype(np.uint8)
    
    # Convert the decrypted array back to an image
    decrypted_image = Image.fromarray(decrypted_array)
    
    # Save the decrypted image
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted successfully! Saved as 'decrypted_image.png'.")

# Main script
if __name__ == "__main__":
    print("Choose an option:")
    print("1. Encrypt an Image")
    print("2. Decrypt an Image")
    
    # Get the user's choice
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        # Get input details for encryption
        image_path = input("Enter the path of the image to encrypt: ")
        key = int(input("Enter the encryption key (integer): "))
        encrypt_image(image_path, key)
    elif choice == 2:
        # Get input details for decryption
        image_path = input("Enter the path of the encrypted image: ")
        key = int(input("Enter the decryption key (integer): "))
        decrypt_image(image_path, key)
    else:
        print("Invalid choice!")
