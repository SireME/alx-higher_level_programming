#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"\
        <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
Total file size: File size: <total size>
where is the sum of all previous (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear, don’t print anything for this\
        status code
format: <status code>: <number>
status codes should be printed in ascending order
"""


import sys
import signal

# Initialize variables
file_size = 0
status_counts = {}


def print_statistics(signal, frame):
    # Print total file size
    print(f"File size: {file_size}")

    # Print number of lines by status code
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        print(f"{status_code}: {count}")


signal.signal(signal.SIGINT, print_statistics)

# Read stdin line by line
for line_number, line in enumerate(sys.stdin, start=1):
    # Parse the line
    parts = line.strip().split()
    ip_address = parts[0]
    status_code = int(parts[-2])
    file_size += int(parts[-1])

    # Increment the status code count
    status_counts[status_code] = status_counts.get(status_code, 0) + 1

    # Print statistics every 10 lines
    if line_number % 10 == 0:
        print_statistics(None, None)
