import os
import sys
# ------------------ Usage ------------------
#python3 main.py ./Dubai_weather -e 2011 Task1  (For Nth Year: Max, Min Temp & Max Humid of Day)
#python3 main.py ./Dubai_weather -a 2011/3 Task2 (For Nth Month: Avg Max, Avg Min Temp & Avg Humid of Day)
#python3 main.py ./Dubai_weather -c 2011/3 Task3 (Barchart Split per day) 
#python3 main.py ./Dubai_weather -d 2011/3 Task4 (Barchart Combined per day)
#3.12.12

# ------------------ CONSTANTS COLORS ------------------

RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m' 

month_map = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
    5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
    9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}

# ------------------ FILE FINDING ------------------

def get_files(path, year, month_name):
    files = []

    if not os.path.exists(path):
        print("Directory not found")
        return files

    all_files = os.listdir(path) #[]
    # print(all_files)

    for name in all_files:
        if name.endswith(".txt") and str(year) in name:
            if month_name is None or month_name in name:
                files.append(path + "/" + name)

    return files

# ------------------ FILE READING ------------------

def read_weather_file(filename):
    data = []

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        parts = line.split(",")

        if parts[0] == "GST":
            continue

        if not parts[0][0].isdigit():
            continue

        try:
            record = {} #dict
            record["date"] = parts[0]
            record["max"] = int(float(parts[1]))
            record["min"] = int(float(parts[3]))
            record["humidity"] = int(float(parts[7])) #maxhumid

            data.append(record)
        except:
            continue

    return data

# ------------------ TASK 1 ------------------

def yearly_report(year, path):
    files = get_files(path, year, None)

    highest = -100
    lowest = 100
    humid = -1

    high_date = ""
    low_date = ""
    humid_date = ""

    for file in files:
        records = read_weather_file(file)
        for r in records:

            # Date Splitting
            parts = r["date"].split("-") #["2011", "8", "7"]
            
            day = parts[2]            

            month_num = int(parts[1])   
            month_str = month_map[month_num] # Month Map(8 -> "Aug")
            
            formatted_date = month_str + " " + day 

            if r["max"] > highest:
                highest = r["max"]
                high_date = formatted_date

            if r["min"] < lowest:
                lowest = r["min"]
                low_date = formatted_date

            if r["humidity"] > humid:
                humid = r["humidity"]
                humid_date = formatted_date

    print("Highest:", highest, "C on", high_date)
    print("Lowest:", lowest, "C on", low_date)
    print("Humidity:", humid, "% on", humid_date)

# ------------------ TASK 2 ------------------

def monthly_average(year, month, path):
    month_name = month_map[month]
    files = get_files(path, year, month_name)

    sum_max = 0
    sum_min = 0
    sum_hum = 0

    count = 0

    for file in files:
        records = read_weather_file(file)
        for r in records:
            sum_max += r["max"]
            sum_min += r["min"]
            sum_hum += r["humidity"]
            count += 1

    if count == 0:
        print("No data")
        return

    print("Highest Average:", sum_max // count, "C")
    print("Lowest Average:", sum_min // count, "C")
    print("Average Humidity:", sum_hum // count, "%")

# ------------------ TASK 3 ------------------

def bar_chart_split(year, month, path):
    month_name = month_map[month]
    files = get_files(path, year, month_name)

    print(month_name, year)

    for file in files:
        records = read_weather_file(file)
        for r in records:
            day = r["date"].split("-")[2]
            print(day, RED + "+" * r["max"] + RESET, r["max"], "C")
            print(day, BLUE + "+" * r["min"] + RESET, r["min"], "C")

# ------------------ TASK 4 ------------------

def bar_chart_combined(year, month, path):
    month_name = month_map[month]
    files = get_files(path, year, month_name)

    print(month_name, year)

    for file in files:
        records = read_weather_file(file)
        for r in records:
            day = r["date"].split("-")[2]
            blue = r["min"]
            red = r["max"] - r["min"] #min-max+++++

            print(
                day,
                BLUE + "+" * blue + RESET +
                RED + "+" * red + RESET, 
                r["min"], "C -", r["max"], "C"
            )

# Driving Code --- MAIN ---
def main():
    args = sys.argv
    # print(args)
    path = args[1]
    mode = args[2]
    date = args[3]

    if "/" in date:
        year = int(date.split("/")[0])
        month = int(date.split("/")[1])
    else:
        year = int(date)
        month = 1

    if mode == "-e":
        yearly_report(year, path)
    elif mode == "-a":
        monthly_average(year, month, path)
    elif mode == "-c":
        bar_chart_split(year, month, path)
    elif mode == "-d":
        bar_chart_combined(year, month, path)

main()

