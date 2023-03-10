#!/usr/bin/python3
""" Log parser """
import sys

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_code_data = {code: 0 for code in status_codes}
total_file_size = 0
try:
    count = 0
    for line in sys.stdin:
        split_str = line.split()
        if len(split_str) > 6:
            total_file_size += int(split_str[-1])
            code = split_str[-2]
            if code in status_code_data:
                count += 1
                status_code_data[code] += 1
                if count % 10 == 0:
                    print('File size: {}'.format(total_file_size))
                    for k, v in sorted(status_code_data.items()):
                        if v != 0:
                            print('{}: {}'.format(k, v))
except KeyboardInterrupt:
    print('File size: {}'.format(total_file_size))
    for k, v in sorted(status_code_data.items()):
        if v != 0:
            print('{}: {}'.format(k, v))
    raise
else:
    print('File size: {}'.format(total_file_size))
    for k, v in sorted(status_code_data.items()):
        if v != 0:
            print('{}: {}'.format(k, v))
