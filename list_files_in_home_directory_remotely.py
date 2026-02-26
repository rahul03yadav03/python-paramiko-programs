# Import Paramiko library (used to create SSH connections)
import paramiko


# Take user input for remote login
ip = input("Please enter ip: ")
usrname = input("Please enter username: ")
passw = input("Please entr Passwords: ")

# Create an SSH client object
ssh = paramiko.SSHClient()


# Automatically accept unknown host keys (avoid manual verification)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# Connect to the remote machine using provided credentials
ssh.connect(ip, username =usrname, password = passw)


# Execute a command on the remote machine
# This command lists files and folders inside /home directory
stdin, stdout, stderr = ssh.exec_command("ls /home")


# Read the command output (returns data in bytes format)
result = stdout.read()


# Convert bytes output into readable string format
final = result.decode()

# Print the readable output
print("Command Output: ",final)


# Close the SSH connection
ssh.close()
