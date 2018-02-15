import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('--add', nargs=2, help='[--add] [x] [y] adds x and y')
parser.add_argument('--sub', nargs=2, help='[--sub] [x] [y] subtracts y from x')
parser.add_argument('--mult', nargs=2, help='[--mult] [x] [y] multiplies x by y')
parser.add_argument('--divi', nargs=2, help='[--divi] [x] [y] dividess x by y')
parser.add_argument('--read', nargs = 1, help='[--read] [filepath] reads/prints the given file')
parser.add_argument('--remove', nargs=1, help='[--remove] [filepath] deletes the given filepath')
parser.add_argument('--hello', help='prints hello', action='store_true')
parser.add_argument('--bye', help='prints goodbye', action='store_true')

args = parser.parse_args()

if args.add is not None:
	print int(args.add[0]) + int(args.add[1])

if args.sub is not None:
	print int(args.sub[0]) - int(args.sub[1])

if args.mult is not None:
	print int(args.mult[0]) * int(args.mult[1])

if args.divi is not None:
	print int(args.divi[0]) / int(args.divi[1])

if args.read is not None:
	f = open(args.read[0], 'r')
	contents = f.read()
	print(contents)
	f.close()

if args.remove is not None:
	os.remove(args.remove[0])
	print 'file removed.'

if args.hello is not False:
	print 'hello'

if args.bye is not False:
	print 'bye'
