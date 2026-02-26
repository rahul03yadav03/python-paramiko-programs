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

# Ask for local file path
local_file = input("Enter full local file path to upload: ")

# Ask for remote file path (including filename)
remote_file = input("Enter full remote path (example: /home/msfadmin/test.txt): ")

# Upload file
sftp.put(local_file, remote_file)

print("File uploaded successfully!")


# Close connections
sftp.close()
ssh.close()
