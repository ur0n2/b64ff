import argparse

parser = argparse.ArgumentParser(prog="b64ff.py", usage = "%(prog)s [options]", description = "[-] base64 encoder and decoder")
parser._optionals.title = "[-] Optional arguments"

terribles = list(xrange(1,51))
group = parser.add_mutually_exclusive_group() # "group", "choicse mode"
group.add_argument("-e", "--encode", type = str, help = "Encode mode") 
group.add_argument("-d", "--decode", type = str, help = "Decode mode") #, metavar = "to_decode_data.b64")

parser.add_argument("-r", "--repeat", type = int, choices = terribles, default = 1, metavar = "", help = "En/Decoded repeat number(repeat number: 0~50, default=1)")
parser.add_argument("-o", "--output", type = str, default = "out.b64", help = "Input outfile path")
parser.add_argument("-v", "--verbose", action = "store_false", default = False, help = "Print the data") #, action = "store_true"
args = parser.parse_args()
#print args

input_path = args.encode or args.decode # good code
verbose = args.verbose
repeat = args.repeat
output_path = args.output

print "input_path:", input_path
print args.verbose
print args.repeat
print args.output



#parser.print_help()

"""
@positional
e filename metavar = "encode_data.txt"
d filename metavar = "decode_data.b64"

@optional
-r repeat_number, default = 1
-o output_filename, default = out.b64
-v print_data(), default = FALSE
"""

#repeat_count = args.er + args.dr # oh ! good idea, anyway one argumet is 0.
"""
if args.verbose:ev
	print_data(data)
elif args.e:

elif args.d:

elif args.er:

elif args.dr:
"""