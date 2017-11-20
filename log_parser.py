#!/usr/bin/python3

import os
from datetime import datetime as dt


# Variables for the script to find the input log file
logDirectory = "/foo/bar"                         # the directory where the log file is at
logName = "sampleLogFile.txt"                      # the name of the log file
logPath = os.path.join(logDirectory, logName)    # combines the above variables together in a way python

# Initializing variables that are needed to store the parsed data
passed = []             # name and completion dates of the sites that passed testing
failed = []             # formated data of the sites that failed testing
error = []              # what failed on the sites
site_test = []          # what sites have been tested
completed_line = []     # the final line in the log 
count = 0               # currently only marks the beginning of the loop to help grab the start time


# opens the filePath file as read only, the with method automatically closes the file at completion
with open(logPath, 'r') as log_file:
    # begins looping through the file
    for line in log_file:
        # grabs the start time from the first line in the log file
        if count == 0:
            line_one = line.split(' ')
            start_time = "{} {}".format(line_one[0], line_one[1])
        # grabs the site's name
        if "[info] Playing test case" in line:
            site_test = line.split(' ')
            site_test[-1] = site_test[-1].strip('\n')
            if site_test[-1] == "Page":
                site_test[-1] = str(' '.join(site_test[-2:]))
        # checks to see if there were errors
        elif "[error]" in line:
            error_list = line.split(' ')
            error_list[-1] = error_list[-1].strip('\n')
            error.append(' '.join(error_list[3:]))
        # detects whether the site's test passed or failed 
        elif "[info] Test case " in line:
            # passed sites display the site's name and time that the test completed
            if "passed" in line:
                passed_time = line.split(' ')
                passed += ["{:20}\t{}".format(site_test[-1], passed_time[1])]
            # failed items display the site name and the error line
            if "failed" in line:
                for failure in error:
                    failed += ["{:20}\t{}".format(site_test[-1], failure)]
        # grabs the test completed line to display
        elif "[info] Test suite completed:" in line:
            completed_line = line.split(" ")
        count += 1
# these variables grab the final line to find the testing completion time
end_line = line.split(' ')
end_time = "{} {}".format(end_line[0], end_line[1])
# calculates the testing time duration
total_time = dt.strptime(end_time, "%Y-%m-%d %H:%M:%S") - dt.strptime(start_time, "%Y-%m-%d %H:%M:%S")

# initializes the file for the report, the file name will appear like: parsedLog_%Y-%m-%d.txt
with open('parsedLog_{}.txt'.format(line_one[0]), 'w') as f:
    # prinsts the final report to a file
    print("Testing Start Time: {}".format(start_time), file=f)
    print('*Passed' + '=' * 50, file=f)
    for i in passed:
        print(i, file=f)
    print('\n*Failed' + '=' * 50, file=f)
    for i in failed:
        print(i, file=f)
    print('', file=f)
    for i in completed_line[3:]:
        print(i, end=' ', file=f)
    print('', file=f)
    print("Total time to completion: {}".format(total_time), file=f)
