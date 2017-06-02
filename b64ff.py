#-*- coding: utf-8-*-
#17.05.23 by ur0n2
#b64ff.py: base64 for file
#pass the text file and binary file test.

import base64
import argparse


def encode_base64(finput):
	encode_base64_data = base64.b64encode(finput)
	return encode_base64_data 


def decode_base64(finput):
	decode_base64_data = base64.b64decode(finput)
	return decode_base64_data 


def print_usage():
	print("Usage: Base64 encode to file: b64ff.py e in.b64 o out.b64") 
	print("       Base64 decode to file: b64ff.py d in.b64 o out.b64")
	print("       Can be omitted arguments are 'o' and 'out.b64'\n")


def print_data(data):
	print(data)


if __name__ == '__main__':	
	parser = argparse.ArgumentParser(prog="b64ff.py", usage = "%(prog)s [options]", description = "[-] base64 encoder and decoder")
	parser._optionals.title = "[-] Optional arguments"

	terribles = list(xrange(1,51))
	group = parser.add_mutually_exclusive_group() # "group", "choicse mode"
	group.add_argument("-e", "--encode", type = str, help = "Encode mode") 
	group.add_argument("-d", "--decode", type = str, help = "Decode mode") #, metavar = "to_decode_data.b64")

	parser.add_argument("-r", "--repeat", type = int, choices = terribles, default = 1, metavar = "", help = "En/Decoded repeat number(repeat number: 0~50, default=1)")
	parser.add_argument("-o", "--output", type = str, default = "out.b64", help = "Input outfile path")
	parser.add_argument("-v", "--verbose", action = "store_true", default = False, help = "Print the data") #, action = "store_true"
	args = parser.parse_args()
	#print(args)

	file_path = args.encode or args.decode # good code
	verbose = args.verbose
	repeat = args.repeat
	output_path = args.output

	try:
		if args.encode: 
			print("[-] Encode mode")
			with open(file_path, "rb") as finput:
				data = finput.read()
				for x in xrange(0, repeat):
					data = encode_base64(data)
				if verbose:
					print_data(data)
				with open(output_path, "wb") as foutput:
					foutput.write(data)
		elif args.decode:
			print("[-] Decode mode")
			with open(file_path, "rb") as finput:
				data = finput.read()
				for x in xrange(0, repeat):
					data = decode_base64(data)
				if verbose:
					print_data(data)
				with open(output_path, "wb") as foutput:
					foutput.write(data)
	except:
		print("[+] This is not base64 data. Please refer to help menu. (-h, --help).")
