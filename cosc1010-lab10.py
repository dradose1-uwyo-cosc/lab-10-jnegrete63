# Jose Fanian Negrete osegura
# UWYO COSC 1010
# Submission Date: 11/19/2024
# Lab 10
# Lab Section:11
# Sources, people worked with, help given to: help from TA'S and help from co-pilot
# your
# comments
# here

#import modules you will need 



def uncover_password():
    from hashlib import sha256 
    def get_hash(to_hash):
        """You can use this to hash the passwords from the file of forbiden paswprds."""
        return sha256(to_hash.encode('utf-8')).hexdigest().upper()
    try:
        with open('hash', 'r') as hash:
            hash_1 = hash.read().strip()
    except FileNotFoundError:
        print("The hash file you are lookign for is not here, thats lame, try again.")
        return
    except Exception as braking_through:
        print(f"Boooooo, there seems to have been an error looking for the items, try to hack again if you may: {braking_through}")
        return

    try:
        from pathlib import Path
        path = Path ('rockyou.txt')
        contents = path.read_text()
        lists = contents.splitlines()
    except FileNotFoundError:
        print("sorry there were no passwords found here, try again.")
        return
    except Exception as braking_through:
        print(f"Sommething went wrong while haking the password, try again: {braking_through}")
        return
    else:
        found_password = ""
        for password in lists:
            password = password.strip()
            if get_hash(password) == hash_1:
                found_password = password
                
                break
        if found_password:
            print(f"Great Haking!!!, you found the password, it is: {password}")

uncover_password()


# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
