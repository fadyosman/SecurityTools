#!/usr/bin/python
from random import choice
import sys
#homographs for each letter. Encoded so that python won't complain.
Homographs = {'A':[u'\u0410',u'\u0391'] ,
				'B':[u'\u0412',u'\u0392'], 
				'C':[u'\u0421'],
				'E':[u'\u0415',u'\u0395'],
				'H':[u'\u041D',u'\u0397'],
				'J':[u'\u0408'],
				'K':[u'\u039A'],
				'M':[u'\u041C',u'\u039C'],
				'N':[u'\u039D'],
				'O':[u'\u041E',u'\u039F'],
				'P':[u'\u0420',u'\u03A1'],
				'S':[u'\u0405'],
				'T':[u'\u0422',u'\u03A4'],
				'X':[u'\u0425',u'\u03A7'],
				'Y':[u'\u03A5'], # End Of Capital letters.
				'a':[u'\u0430'],
				'c':[u'\u0441'],
				'e':[u'\u0435'],
				'i':[u'\u0456'],
				'j':[u'\u0458'],
				'k':[u'\u043A',u'\u03BA'],
				'o':[u'\u043E',u'\u03BF'],
				'p':[u'\u0440',u'\u03C1'],
				'r':[u'\u0433'],
				's':[u'\u0455'],
				'v':[u'\u03BD'],
				'x':[u'\u0445',u'\u03C7'],
				'y':[u'\u0443']}
def string_from_file(filename):
	in_file = open(filename ,"r")
	in_string = in_file.read();
	in_file.close()
	return in_string
	
def replace_all(in_string):
	out_str = in_string
	for l in Homographs:
		out_str = out_str.replace(l,choice(Homographs[l]).encode('utf8'))
	return out_str
	
def string_to_file(filename,out_string):
		out_file = open(filename ,"w")
		out_file.write(out_string)
		out_file.close()
#The Main Program Code.
print '''
*******************************************************************
*                             Homographit                         *
*                     Tool To Bypass Spam Filters                 *
*                    Created By Fady Mohamed Osman                *
*                         www.dark-masters.tk                     *
*******************************************************************
'''
if len(sys.argv) == 3 or len(sys.argv) == 1:
	if len(sys.argv) == 3:
		in_str = string_from_file(sys.argv[1])
		out_str = replace_all(in_str)
		string_to_file(sys.argv[2],out_str)
		print "done..."
	if len(sys.argv) == 1:
		print 'Usage : homographit.py infile outfile'
else:
	print '''Error : Wrong number of arguments.
	Usage : homographit.py infile outfile'''
