import sys

args = sys.argv[1:]

d = []

do_sort = False

while args:
    arg = args.pop(0)
    if arg == "--sort":
        do_sort = True
    else:
        key, value = arg.split("=")
        d.append(f"Key: {key} Value: {value}")

if do_sort:
    d = sorted(d)

print(' '.join(d))

