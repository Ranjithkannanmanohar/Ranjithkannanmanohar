import os

# perfectly working - need to create a ip_list file for list of ip address to ping.

with open("ip_list.txt") as file:
    park = file.read()
    park = park.splitlines()
    print(f" {park}  \n")
    # ping for each ip in the file
for ip in park:
    response = os.popen(f"ping {ip} ").read()
    
    #saving some ping output details to output file
    
    if("Request timed out." or "unreachable") in response:
	    print(response)
	    f = open("ip_output.txt","a")
	    f.write(str(ip) + ' link is down'+'\n')
	    f.close() 
    else:
	    print(response)
	    f = open("ip_output.txt","a")  
	    f.write(str(ip) + ' is up '+'\n')
	    f.close() 
    # print output file to screen
with open("ip_output.txt") as file:
    output = file.read()
    f.close()
    print(output)
with open("ip_output.txt","w") as file:    
	pass