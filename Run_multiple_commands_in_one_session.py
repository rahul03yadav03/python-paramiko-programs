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

    # List of commands to run on the remote system
    commands = ["ls", "date", "whoami"]

    # Loop through each command
    for comnd in commands:
        stdin, stdout, stderr = ssh.exec_command(comnd)

        # Read command output
        result = stdout.read()
        final = result.decode()

        # Print the output for each command
        print(f"Command: {comnd}")
        print("Command Output: ", final)

    # Close the SSH connection properly
    ssh.close()

# Catch authentication failure exception
except paramiko.AuthenticationException:
    print("Login failed")
