# Import Paramiko library (used to create SSH connections)
import paramiko


# Take user input for remote login
ip = input("Please enter ip: ")
usrname = input("Please enter username: ")
passw = input("Please entr Passwords: ")

# Create SSH client
ssh = paramiko.SSHClient()

# Automatically accept unknown host keys
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# Connect to remote machine
ssh.connect(ip, password = passw , username=usrname)

# Open SFTP session
sftp = ssh.open_sftp()

# Ask for remote file path (including filename)
remote_file = input("Enter full remote file path to download: ")


# Ask for local path where you want to save the file
local_file = input("Enter full local path: ")


# Download file from remote to local
sftp.get(remote_file,local_file)

print("File downloaded successfully!")

# Close connections
sftp.close()
ssh.close()
