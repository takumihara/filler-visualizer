import argparse
import subprocess
import sys
import time

RESET = "\033[0m"
BLUE = "\033[34m"

def main():
    parser = argparse.ArgumentParser(description='Test filler in an easier way')
    parser.add_argument('p1', help='same as p1 in filler_vm')
    parser.add_argument('p2', help='same as p2 in filler_vm')
    parser.add_argument('f', help='same as f in filler_vm')

    args = parser.parse_args()
    p1 = args.p1
    p2 = args.p2
    f = args.f
    res = subprocess.run(["./bin/filler_vm", "-t", "3", "-p1", f"{p1}", "-p2", f"{p2}", "-f", f"{f}"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    lines = res.stdout.splitlines()
    y, x = map(int, lines[9][:-1].split()[1:])

    print(lines[10])
    offset = 11
    lines_len = len(lines)
    print(lines_len, file=sys.stderr)
    while True:
        if offset + y + 1 > lines_len:
            print(f"{BLUE}HERE{RESET}")
            break
        # print(offset + y, file=sys.stderr)
        print_board(lines, offset, y)
        print(f"\033[{y}A", end="")
        time.sleep(0.1)
        offset += y
        token_y = int(lines[offset].split()[1])
        offset += 1 + token_y
        offset += 3
    print(lines[-2])
    print(lines[-1])


def print_board(lines, start, y_max):
    for y in range(start, start + y_max):
        print(lines[y])


if __name__ == "__main__":
    main()
