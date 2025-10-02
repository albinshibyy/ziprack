# ZIPRACK
# Version: 1.01
# Created: albinshibyz | github
# bruteforcing py script
# for educational purpose only

import zipfile
import time  # Import time module for delays

print("ZIPRACK Program in Execution!")
print("Version: 3.69")
print("visit github repo for more info-")
print("bruteforcing tool for educational purpose only")
print("---------")

while True:
    try:
        # Ask for location of protected ZIP archive
        zip_file = input("Enter the location of the protected ZIP archive: ")

        # Check if the file exists
        if not zip_file:
            print("Please enter a valid file path.")
            continue

        # Create a ZipFile object with the zip_file path
        with zipfile.ZipFile(zip_file) as zf:
            # Check if the ZIP file is encrypted
            if not zf.infolist():
                print("The ZIP file is not encrypted.")
                continue

            # Ask for location of password list file
            password_list = input("Enter the location of the password list file: ")

            # Check if the file exists
            if not password_list:
                print("Please enter a valid file path.")
                continue

            # Open the password list file and read its contents
            with open(password_list, 'r') as pw_file:
                # Loop through each line in the password list file
                for line in pw_file:
                    # Strip any whitespace characters from the beginning or end of the line
                    password = line.strip()

                    try:
                        print("[ATTEMPT] target 192.06.##1")
                        print("attacking password")
                        time.sleep(0.5)  # Cool pause before attempting password # remove it for real use
                        
                        # Attempt to extract the contents of the ZIP archive using the current password
                        zf.extractall(pwd=password.encode())

                        # If successful, print the cracked password and exit the loop
                        print("---------------")
                        print("Successfull")
                        print("Host: 192.06.##1-01")
                        print(f"Cracked password: {password}")
                        print("decrypted files saved on default folder")
                        break

                    except zipfile.BadZipFile:
                        print("Invalid ZIP file. Please check the file path and try again.")
                        break

                    except zipfile.LargeZipFile:
                        print("The ZIP file is too large. Please try again with a smaller file.")
                        break

                    except RuntimeError:
                        # If the password is incorrect, continue trying other passwords
                        time.sleep(0.5)  # Small pause between failed attempts
                        continue

                    except Exception as e:
                        # If an error occurs, print the error message and continue trying other passwords
                        print(f"Error: {e}")
                        continue

                else:
                    # If all passwords have been tried and none worked, print a failure message
                    print("Could not crack the password.")

    except FileNotFoundError:
        print("The file was not found. Please check the file path and try again.")

    except PermissionError:
        print("Permission denied. Please check the file permissions and try again.")

    except Exception as e:
        print(f"An error occurred: {e}")

    # Ask the user if they want to retry the password cracking job
    retry = input("Do you want to retry? (y/n): ")
    if retry.lower() in ("n", "no", "nah", "exit"):
        print("PROGRAM EXITING!!!!!")
        print("FINGERPRINTS CLEARED")
        break

