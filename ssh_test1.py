import paramiko

# script perfectly works 

router_ip = "192.168.10.132"
router_username = "pyt"
router_password = "pyt"

ssh = paramiko.SSHClient()


def run_command_on_device(ip_address, username, password, command):
    """ Connect to a device, run a command, and return the output."""

    # Load SSH host keys.
    ssh.load_system_host_keys()
    # Add SSH host key when missing.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    total_attempts = 2
    for attempt in range(total_attempts):
        try:
            print("Attempt to connect: %s" % attempt)
            # Connect to router using username/password authentication.
            ssh.connect(router_ip, 
                        username=router_username, 
                        password=router_password,
                        look_for_keys=False )
            # Run command.
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("sh ip route")
            # Read output from command.
            output = ssh_stdout.readlines()
            # Close connection.
            ssh.close()
            return output

        except Exception as error_message:
            print("Unable to connect")
            print(error_message)

router_output = run_command_on_device(router_ip, router_username, router_password,"show ip route")

if router_output != None:
    for line in router_output:
        if "0.0.0.0/0" in line:
            print("Found Default Route")
            print(line)

router_output1 = run_command_on_device(router_ip, router_username, router_password,"show ip bgp")

if router_output1 != None:
    for line in router_output:
        if "172.20.1.0/24" in line:
            print("Found Default Route")
            print(line)