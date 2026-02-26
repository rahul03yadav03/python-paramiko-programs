# Import Paramiko library (used for SSH connections)
import paramiko


# Take user input
ip =  input("Please enter IP: ")
usrname = input("PLease enter username: ")
pasw = input("Please enter password: ")


# Create SSH client object
client = paramiko.SSHClient()

# Automatically add the server's SSH key (if not already known)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# Connect to the remote SSH server
client.connect(ip, username = usrname, password=pasw)

# Execute a simple command on the remote system
stdin, stdout, stderr = client.exec_command("date")


# Read command output (returns bytes)
result = stdout.read()

# Convert bytes to string
final = result.decode()

# Print readable output
print("Command Output: ",final)


# Close SSH connection
client.close()
