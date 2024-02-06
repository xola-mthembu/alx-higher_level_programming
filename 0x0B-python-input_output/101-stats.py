#!/usr/bin/python3
"""
Module 101-stats.py
Reads stdin line by line and computes metrics: total file size and
the number of lines by status code.
"""


import sys


def print_stats(total_size, status_codes):
    """Prints the statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
        404: 0, 405: 0, 500: 0
    }
    total_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) > 2:
                try:
                    status = int(parts[-2])
                    size = int(parts[-1])
                    if status in status_codes:
                        status_codes[status] += 1
                    total_size += size
                except (ValueError, IndexError):
                    pass

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
