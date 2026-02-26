# Import Paramiko library (used to create SSH connections)
import paramiko


# Take user input for remote login
ip = input("Please enter ip: ")
usrname = input("Please enter username: ")
passw = input("Please entr password: ")

# Python script to execute remotely
script_path = input("Please Enter full path to your python Script: ")

try:
    # Create SSH client
    ssh = paramiko.SSHClient()

    # Automatically accept unknown host keys
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the remote server
    ssh.connect(ip, password = passw, username = usrname)

    

    # Execute the Python script
    stdin, stdout, stderr = ssh.exec_command(f"python3 {script_path}")

    # Read command output and errors
    result = stdout.read().decode()
    error = stderr.read().decode()

    # Print command output if any
    if result:
        print("Command Output: ", result)

    # Print error output if any
    if error:
        print("Error Output: ", error)

    # Close the SSH connection properly
    ssh.close()

# Handle failed login
except paramiko.AuthenticationException:
    print("Login failed")

