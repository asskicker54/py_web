import argparse

parser = argparse.ArgumentParser()
parser.add_argument("nums", nargs="*")
args = parser.parse_args()

nums = []

if len(args.nums) == 0:
    print("NO PARAMS")
elif len(args.nums) > 2:
    print("TOO MANY PARAMS")
elif len(args.nums) < 2:
    print("TOO FEW PARAMS")
else:
    nums = list(map(int, args.nums))
    print(sum(nums))

