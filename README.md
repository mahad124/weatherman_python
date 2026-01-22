# WeatherMan Python

A command-line weather data analysis tool that processes historical weather data from text files and generates reports and visualizations.

## Features

WeatherMan provides four different analysis modes:

1. **Yearly Report** - Find the highest temperature, lowest temperature, and maximum humidity for a given year
2. **Monthly Average** - Calculate average maximum temperature, average minimum temperature, and average humidity for a specific month
3. **Bar Chart (Split)** - Display daily maximum and minimum temperatures as separate bar charts
4. **Bar Chart (Combined)** - Display daily temperature ranges (min-max) as combined bar charts

## Requirements

- Python 3.x
- No external dependencies required (uses only standard library)

## Usage

### Command Syntax

```bash
python3 main.py <path_to_weather_data> <mode> <date> <task_name>
```

### Parameters

- `<path_to_weather_data>` - Path to the directory containing weather data files (e.g., `./Dubai_weather`)
- `<mode>` - Analysis mode:
  - `-e` - Yearly report (Task 1)
  - `-a` - Monthly average (Task 2)
  - `-c` - Bar chart split (Task 3)
  - `-d` - Bar chart combined (Task 4)
- `<date>` - Date specification:
  - For yearly reports: `YYYY` (e.g., `2011`)
  - For monthly reports: `YYYY/MM` (e.g., `2011/3` for March 2011)
- `<task_name>` - Optional task identifier (e.g., `Task1`, `Task2`, etc.)

## Examples

### Task 1: Yearly Report
Find the highest temperature, lowest temperature, and maximum humidity for the year 2011:

```bash
python3 main.py ./Dubai_weather -e 2011 Task1
```

**Output:**
```
Highest: 45 C on Aug 15
Lowest: 10 C on Jan 3
Humidity: 95 % on Aug 20
```

### Task 2: Monthly Average
Calculate average temperatures and humidity for March 2011:

```bash
python3 main.py ./Dubai_weather -a 2011/3 Task2
```

**Output:**
```
Highest Average: 32 C
Lowest Average: 22 C
Average Humidity: 65 %
```

### Task 3: Bar Chart (Split)
Display daily maximum and minimum temperatures separately for March 2011:

```bash
python3 main.py ./Dubai_weather -c 2011/3 Task3
```

**Output:**
```
Mar 2011
1 ++++++++++++++++++++++++++++++++ 35 C
1 +++++++++++++++++++ 20 C
2 +++++++++++++++++++++++++++++++ 34 C
2 ++++++++++++++++++ 19 C
...
```

### Task 4: Bar Chart (Combined)
Display daily temperature ranges (min-max) as combined bar charts for March 2011:

```bash
python3 main.py ./Dubai_weather -d 2011/3 Task4
```

**Output:**
```
Mar 2011
1 +++++++++++++++++++++++++++++++++++++++++++ 20 C - 35 C
2 ++++++++++++++++++++++++++++++++++++++++++ 19 C - 34 C
...
```

## Data Format

The tool expects weather data files in the following format:
- Files should be `.txt` files
- Filenames should contain the year (e.g., `Dubai_weather_2011_Jan.txt`)
- Each line should contain comma-separated values with:
  - Date (format: `YYYY-MM-DD`)
  - Maximum temperature
  - Minimum temperature
  - Maximum humidity

Example data line:
```
2011-03-15,35,25,65,...
```

## Project Structure

```
WeatherMan_Python/
├── main.py                 # Main application file
├── Dubai_weather/          # Dubai weather data files
├── lahore_weather/         # Lahore weather data files
├── Murree_weather/         # Murree weather data files
└── README.md              # This file
```

## How It Works

1. **File Finding**: The tool scans the specified directory for `.txt` files matching the year and month criteria
2. **Data Parsing**: Reads and parses weather data from text files, extracting dates, temperatures, and humidity
3. **Analysis**: Performs calculations based on the selected mode:
   - Finds extremes (max/min) for yearly reports
   - Calculates averages for monthly reports
   - Generates ASCII bar charts for visualization
4. **Output**: Displays results in the terminal with color-coded visualizations (red for max, blue for min)

## Notes

- The tool uses ANSI color codes for terminal output (red for maximum temperatures, blue for minimum temperatures)
- Date formatting uses month abbreviations (Jan, Feb, Mar, etc.)
- Temperature values are displayed in Celsius (°C)
- Humidity values are displayed as percentages (%)

## Version

Current version: 3.12.12
