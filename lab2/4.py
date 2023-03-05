import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file1")
parser.add_argument("file2")
parser.add_argument("--upper", action="store_true")
parser.add_argument("--lines", type=int)

args = parser.parse_args()

l = []
with open(args.file1, 'r') as f1:
    l = f1.readlines()

if args.upper:
    for i in range(len(l)):
        l[i] = str.upper(l[i])

if args.lines is not None:
    l = l[:args.lines]

with open(args.file2, 'w') as f2:
    f2.writelines(l)
