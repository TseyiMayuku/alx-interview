#!/usr/bin/python3
'''Script for Log parsing'''

import sys

STATUS_CODES = {
    '200': 0, 
    '301': 0, 
    '400': 0, 
    '401': 0,
    '403': 0, 
    '404': 0, 
    '405': 0, 
    '500': 0
}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        fields = line.strip().split(" ")
        if len(fields) >= 3:
            status = fields[-2]
            size = int(fields[-1])
            if status in STATUS_CODES:
                STATUS_CODES[status] += 1
            total_size += size
            line_count += 1

        if line_count % 10 == 0:
            print('Total file size: {}'.format(total_size))
            for code in sorted(STATUS_CODES):
                if STATUS_CODES[code] > 0:
                    print('{}: {}'.format(code, STATUS_CODES[code]))

except Exception as e:
    pass

finally:
    print('Total file size: {}'.format(total_size))
    for code in sorted(STATUS_CODES):
        if STATUS_CODES[code] > 0:
            print('{}: {}'.format(code, STATUS_CODES[code]))
