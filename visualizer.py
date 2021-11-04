import argparse
import os
import signal
import time

RESET = "\033[0m"
BLUE = "\033[34m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
GREEN = "\033[32m"
BOLD = "\033[1m"
BOLD_UNDERLINE = "\033[1m\033[4m"
stop = False


def main():
    global stop
    parser = argparse.ArgumentParser(description='Visualize your filler game')
    parser.add_argument('-n', help='time between showing boards', type=float, default=0.1)
    parser.add_argument('-s', help='stop at the first board', type=bool, default=False)

    args = parser.parse_args()
    n = args.n
    stop = args.s

    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    p1_name = os.path.basename(lines[5].split()[1])
    p2_name = os.path.basename(lines[7].split()[1])
    y, x = map(int, lines[9][:-1].split()[1:])

    v = Visualizer(lines, x, y, p1_name, p2_name)
    while True:
        v.print_zone_bar()
        v.print_board()
        v.move_token_num()
        if v.is_ended():
            break
        else:
            print(f"\033[{y + 3}A", end="")
        if not v.is_success():
            v.move_token_num()
        time.sleep(n)
        if stop is True:
            signal.sigwait([signal.SIGQUIT, signal.SIGINT])
            stop = False
    v.print_results()


class Visualizer:
    def __init__(self, lines, x, y, p1_name, p2_name):
        self.lines = lines
        self.x = x
        self.y = y
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.offset = 9
        self.lines_len = len(lines)

    def print_zone_bar(self):
        p1_counter = 0
        p2_counter = 0

        for y in range(self.offset + 2, self.offset + 2 + self.y):
            line = self.lines[y].split()[1]
            for x in range(self.x):
                if line[x] in ("o", "O"):
                    p1_counter += 1
                elif line[x] in ("x", "X"):
                    p2_counter += 1
        print(f"{RED}p1: {p1_counter} / {self.x * self.y}")
        print(f"{BLUE}p2: {p2_counter} / {self.x * self.y}{RESET}")

    def print_board(self):
        self.offset += 1
        print("     ", end="")
        for num in self.lines[self.offset].lstrip():
            print(f"{num}  ", end="")
        print()
        self.offset += 1
        for y in range(self.offset, self.offset + self.y):
            line = self.lines[y].split()
            print(line[0], end="")
            print("  ", end="")
            line = line[1]
            for x in range(self.x):
                if line[x] == "O":
                    print(f"{RED}{line[x]}", end="")
                elif line[x] == "o":
                    print(f"{BOLD_UNDERLINE}{RED}O{RESET}", end="")
                elif line[x] == "X":
                    print(f"{BLUE}{line[x]}", end="")
                elif line[x] == "x":
                    print(f"{BOLD_UNDERLINE}{BLUE}X{RESET}", end="")
                else:
                    print(f"{RESET}{line[x]}", end="")
                print("  ", end="")
            print(RESET)
        self.offset += self.y

    def move_token_num(self):
        token_y = int(self.lines[self.offset].split()[1])
        # token width/height info and token piece height, placement of token info
        self.offset += 1 + token_y + 1

    def is_ended(self) -> bool:
        return self.offset + 2 >= self.lines_len

    def is_success(self) -> bool:
        return self.lines[self.offset].split()[0] == "Plateau"

    def print_results(self):
        print(f"{RED}{self.p1_name} {self.lines[-2].split()[3]}")
        print(f"{BLUE}{self.p2_name} {self.lines[-1].split()[3]}{RESET}")


def signal_handler(signum, frame):
    global stop
    stop = True


if __name__ == "__main__":
    signal.signal(signal.SIGQUIT, signal_handler)
    # signal.signal(signal.SIGSTOP, signal_handler)
    main()
