# webonary_selenium_log_parser
A python3 script to parse the logs from Selenium IDE for Webonary.org

# Usage:
$ python3 log_parser.py

usage: log_parser.py [-h] [-i INPUT_FILE] [-o OUTPUT_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --inputfile INPUT_FILE
                        The logfile you want to parse
  -o OUTPUT_FILE, --outputfile OUTPUT_FILE
                        The file where you would like the output to go
                        
# Note:
When using the script for the first time, you may want to change the default file path for the input file. It can be found at around line 20 in the script. Otherwise you'll run into a file exception error unless you use the '-i' argument to specify a different file.
