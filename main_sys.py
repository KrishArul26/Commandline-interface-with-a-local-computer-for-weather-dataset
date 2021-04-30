import sys
from Assign_weather import weather_exctract as wea_exc


def print_help():
    print("Welcome to the  weather data extraction")
    print("usage: -i <input file path> -o <output file path> -c <columns> -t <start_time> -d< duration>")
    print("Enter column name")


args = sys.argv[1:]
print(args)

input_file, output_file, columns, start_time, duration = None, None, None, None, None

# Help
if "-h" in args:
    print_help()
    exit()

# Input file
if "-i" in args:
    try:
        input_file = open(args[args.index("-i") + 1])
    except FileNotFoundError:
        print("The input file does not exist !")
        exit()

# Output file
if "-o" in args:
    try:
        output_file = open(args[args.index("-o") + 1], "w")
    except IOError:
        print("The output file cannot be create !")
        exit()

# Start time
if "-t" in args:
    try:
        start_time = args[args.index("-t") + 1]
    except IndexError:
        print("Missing input value for time")
        print_help()
        exit()
else:
    start_time = None

# Duration
if "-d" in args:
    if "-t" in args:
        try:
            duration = float(args[args.index("-d") + 1])
        except IndexError:
            print("Missing input value for duration")
            print_help()
            exit()
    else:
        print("Start time not defined")
        exit()
else:
    duration = None

if "-c" in args:
    try:
        columns = list(args[args.index("-c") + 1: len(args)])
        if len(columns) == 0:
            print("Enter the columns name")
            exit()
    except IndexError:
        print("Missing input value for columns")
        print_help()
        exit()
else:
    columns = ['air_temp', 'humidity', 'leaf', 'leaf_dry', 'leaf_wet']

if input_file is None or output_file is None:
    print_help()
    exit()

for column in columns:
    if column != 'air_temp' and column != 'humidity' and column != 'leaf' and column != 'leaf_dry' and column != 'leaf_wet':
        print("Invalid Column Name")
        exit()

print(wea_exc(input_file, output_file, columns=columns, start_time=start_time, duration=duration))
