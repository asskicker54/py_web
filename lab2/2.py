import sys

args = sys.argv[1:]
l = []
do_count = False
do_num = False
do_sort = False

while args:
    arg = args.pop(0)
    if arg == "--count":
        do_count = True
    elif arg == "--num":
        do_num = True
    elif arg == "--sort":
        do_sort = True
    else:
        file = arg
        try:
            with open(file, 'r') as f:
                l = f.readlines()
        except FileNotFoundError:
            print("ERROR")

if do_sort:
    l = sorted(l)

if do_num:
    for i in range(len(l)):
        l[i] = str(i) + " " + l[i]

if do_count:
    l.append(f"count: {len(l)}")

print('\n'.join(l))
