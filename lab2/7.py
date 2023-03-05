import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("--count", action="store_true")
parser.add_argument("--num", action="store_true")
parser.add_argument("--sort", action="store_true")
args = parser.parse_args()
l = []

try:
    with open(args.file, 'r') as f:
        l = f.readlines()
except FileNotFoundError:
    print("ERROR")

if args.sort:
    l.sort()
if args.num:
    for i in range(len(l)):
        l[i] = str(i) + " " + l[i]
if args.count:
    l.append(f"\ncount: {len(l)}")

print(''.join(l))
