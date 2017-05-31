import argparse

parser = argparse.ArgumentParser(prog="b64ff.py", usage = "%(prog)s [options]", description = "[-] base64 encoder and decoder")
parser._optionals.title = "[-] Optional arguments"

terribles = list(xrange(1,51))
group = parser.add_mutually_exclusive_group() # "group", "choicse mode"
group.add_argument("-e", "--encode", action = "store_true", help = "Encode mode")
group.add_argument("-d", "--decode", action = "store_true", help = "Decode mode")
group.add_argument("-er", "--encode-repeat", type = int, choices = terribles, default = 1, metavar = '', help = "Encode repeat mode(repeat number: 0~50)")
group.add_argument("-dr", "--decode-repeat", type = int, choices = xrange(1,51), default = 1, metavar = '', help = "Decode repeat mode(repeat number: 0~50)") #help = argparse.SUPPRESS) 

print ev tparser._action_groups[1].help

parser.add_argument("-o", "--output", action = "store_true", help = "Input the outfile path.")
parser.add_argument("-v", "--verbose", action = "store_true", help = "Print the data")0

args = parser.parse_args()
parser.print_help()
#repeat_count = args.er + args.dr # oh ! good idea, anyway one argumet is 0.
"""
if args.verbose:ev
	print_data(data)
elif args.e:

elif args.d:

elif args.er:

elif args.dr:
"""