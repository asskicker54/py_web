import argparse

parser = argparse.ArgumentParser()
parser.add_argument("pairs", nargs="+")
parser.add_argument("--sort", action="store_true")
args = parser.parse_args()
d = []
for pair in args.pairs:
    key, value = pair.split("=")
    d.append(f"Key: {key} Value: {value}")

if args.sort:
    d = sorted(d)
print('\n'.join(d))
