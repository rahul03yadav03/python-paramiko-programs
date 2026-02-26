# Import Paramiko library (used to create SSH connections)
import paramiko


# Take user input for remote login
ip = input("Please enter ip: ")
usrname = input("Please enter username: ")
passw = input("Please entr password: ")

try:
    # Create SSH client
    ssh = paramiko.SSHClient()

    # Automatically accept unknown host keys (avoid host verification errors)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Attempt to connect using provided credentials
    ssh.connect(ip, password = passw, username = usrname)

    # If no exception occurs, login was successful
    print("Login successful!")

    # Close the SSH connection properly
    ssh.close()


# Catch authentication failure exception
except paramiko.AuthenticationException:

    # Incorrect username or password
    print("Login Failed!")
