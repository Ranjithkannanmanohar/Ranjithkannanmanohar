import getpass
import telnetlib

# template with inherit password
# just to run the show commands or excute some commands 
# this code works perfectly 

HOST = "192.168.10.130"
user = "pytest"
password = "pytest"
enablepassword = "pytest"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    tn.read_until(b"switch1>")
    tn.write(b"enable\n")
    tn.write(enablepassword.encode('ascii') + b"\n")
    tn.write(b"show ip int brief\n")
    #tn.write(b"conf t\n")
    #tn.write(b"int loop 1\n")
    #tn.write(b"no ip address\n")
    #tn.write(b"sh\n")
    #tn.write(b"end\n")
    tn.write(b" sh ip bgp summary\n")
    tn.write(b" sh cdp neigh\n")
    #tn.write(b" sh cdp neigh details\n")
    tn.write(b" sh int e0/0 | in err\n")
    tn.write(b" sh int e0/0 | in tx\n")
    tn.write(b" sh int e0/0 | in rx\n")
    tn.read_until(b"switch1#")
    tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))