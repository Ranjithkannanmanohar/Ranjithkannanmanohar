import getpass
import telnetlib

HOST = "192.168.10.132"
user = input("Enter your Username: ")
password = getpass.getpass()
enablepassword = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    tn.read_until(b"R1>")
    tn.write(b"enable\n")
    tn.write(enablepassword.encode('ascii') + b"\n")
    #tn.write(b"conf t\n")
    #tn.write(b"int loop 1\n")
    #tn.write(b"ip add 10.10.10.20 255.255.255.255\n")
    #tn.write(b"no sh\n")
    #tn.write(b"end\n")
    tn.read_until(b"R1#")
    tn.write(b"sh ip int brie\n")
    tn.write(b"sh ip bgp summary\n")
    tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))