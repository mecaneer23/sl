#!/usr/bin/env python3
# pylint: disable=missing-docstring

import curses
import sys

D51HEIGHT = 10
D51FUNNEL = 7
D51LENGTH = 83
D51PATTERNS = 6


D51BODY = (
    "      ====        ________                ___________ ",
    "  _D _|  |_______/        \\__I_I_____===__|_________| ",
    "   |(_)---  |   H\\________/ |   |        =|___ ___|   ",
    "   /     |  |   H  |  |     |   |         ||_| |_||   ",
    "  |      |  |   H  |__--------------------| [___] |   ",
    "  | ________|___H__/__|_____/[][]~\\_______|       |   ",
    "  |/ |   |-----------I_____I [][] []  D   |=======|__ ",
)

D51WHL = (
    (
        "__/ =| o |=-~~\\  /~~\\  /~~\\  /~~\\ ____Y___________|__ ",
        " |/-=|___|=    ||    ||    ||    |_____/~\\___/        ",
        "  \\_/      \\O=====O=====O=====O_/      \\_/            ",
    ),
    (
        "__/ =| o |=-~~\\  /~~\\  /~~\\  /~~\\ ____Y___________|__ ",
        " |/-=|___|=O=====O=====O=====O   |_____/~\\___/        ",
        "  \\_/      \\__/  \\__/  \\__/  \\__/      \\_/            ",
    ),
    (
        "__/ =| o |=-O=====O=====O=====O \\ ____Y___________|__ ",
        " |/-=|___|=    ||    ||    ||    |_____/~\\___/        ",
        "  \\_/      \\__/  \\__/  \\__/  \\__/      \\_/            ",
    ),
    (
        "__/ =| o |=-~O=====O=====O=====O\\ ____Y___________|__ ",
        " |/-=|___|=    ||    ||    ||    |_____/~\\___/        ",
        "  \\_/      \\__/  \\__/  \\__/  \\__/      \\_/            ",
    ),
    (
        "__/ =| o |=-~~\\  /~~\\  /~~\\  /~~\\ ____Y___________|__ ",
        " |/-=|___|=   O=====O=====O=====O|_____/~\\___/        ",
        "  \\_/      \\__/  \\__/  \\__/  \\__/      \\_/            ",
    ),
    (
        "__/ =| o |=-~~\\  /~~\\  /~~\\  /~~\\ ____Y___________|__ ",
        " |/-=|___|=    ||    ||    ||    |_____/~\\___/        ",
        "  \\_/      \\_O=====O=====O=====O/      \\_/            ",
    ),
)

D51DEL = "                                                      "

COAL = (
    "                              ",
    "                              ",
    "    _________________         ",
    "   _|                \\_____A  ",
    " =|                        |  ",
    " -|                        |  ",
    "__|________________________|_ ",
    "|__________________________|_ ",
    "   |_D__D__D_|  |_D__D__D_|   ",
    "    \\_/   \\_/    \\_/   \\_/    ",
)

COALDEL = "                              "

LOGOHEIGHT = 6
LOGOFUNNEL = 4
LOGOLENGTH = 84
LITTLE_PATTERNS = 6

LITTLE_BODY = (
    "     ++      +------ ",
    "     ||      |+-+ |  ",
    "   /---------|| | |  ",
    "  + ======== +-+ |  ",
)

LITTLE_WHL = (
    (
        " _|--O========O~\\-+  ",
        "//// \\_/      \\_/    ",
    ),
    (
        " _|--/O========O\\-+  ",
        "//// \\_/      \\_/    ",
    ),
    (
        " _|--/~O========O-+  ",
        "//// \\_/      \\_/    ",
    ),
    (
        " _|--/~\\------/~\\-+  ",
        "//// \\_O========O    ",
    ),
    (
        " _|--/~\\------/~\\-+  ",
        "//// \\O========O/    ",
    ),
    (
        " _|--/~\\------/~\\-+  ",
        "//// O========O_/    ",
    ),
)

LITTLE_COAL = (
    "____                 ",
    "|   \\@@@@@@@@@@@     ",
    "|    \\@@@@@@@@@@@@@_ ",
    "|                  | ",
    "|__________________| ",
    "   (O)       (O)     ",
)

LITTLE_CAR = (
    "____________________ ",
    "|  ___ ___ ___ ___ | ",
    "|  |_| |_| |_| |_| | ",
    "|__________________| ",
    "|__________________| ",
    "   (O)        (O)    ",
)

LITTLE_DEL = "                     "

C51HEIGHT = 11
C51FUNNEL = 7
C51LENGTH = 87
C51PATTERNS = 6

C51DEL = "                                                       "

C51BODY = (
    "        ___                                            ",
    "       _|_|_  _     __       __             ___________",
    "    D__/   \\_(_)___|  |__H__|  |_____I_Ii_()|_________|",
    "     | `---'   |:: `--'  H  `--'         |  |___ ___|  ",
    "    +|~~~~~~~~++::~~~~~~~H~~+=====+~~~~~~|~~||_| |_||  ",
    "    ||        | ::       H  +=====+      |  |::  ...|  ",
    "|    | _______|_::-----------------[][]-----|       |  ",
)

C51WHL = (
    (
        "| /~~ ||   |-----/~~~~\\  /[I_____I][][] --|||_______|__",
        "------'|oOo|==[]=-     ||      ||      |  ||=======_|__",
        "/~\\____|___|/~\\_|   O=======O=======O  |__|+-/~\\_|     ",
        "\\_/         \\_/  \\____/  \\____/  \\____/      \\_/       ",
    ),
    (
        "| /~~ ||   |-----/~~~~\\  /[I_____I][][] --|||_______|__",
        "------'|oOo|===[]=-    ||      ||      |  ||=======_|__",
        "/~\\____|___|/~\\_|    O=======O=======O |__|+-/~\\_|     ",
        "\\_/         \\_/  \\____/  \\____/  \\____/      \\_/       ",
    ),
    (
        "| /~~ ||   |-----/~~~~\\  /[I_____I][][] --|||_______|__",
        "------'|oOo|===[]=- O=======O=======O  |  ||=======_|__",
        "/~\\____|___|/~\\_|      ||      ||      |__|+-/~\\_|     ",
        "\\_/         \\_/  \\____/  \\____/  \\____/      \\_/       ",
    ),
    (
        "| /~~ ||   |-----/~~~~\\  /[I_____I][][] --|||_______|__",
        "------'|oOo|==[]=- O=======O=======O   |  ||=======_|__",
        "/~\\____|___|/~\\_|      ||      ||      |__|+-/~\\_|     ",
        "\\_/         \\_/  \\____/  \\____/  \\____/      \\_/       ",
    ),
    (
        "| /~~ ||   |-----/~~~~\\  /[I_____I][][] --|||_______|__",
        "------'|oOo|=[]=- O=======O=======O    |  ||=======_|__",
        "/~\\____|___|/~\\_|      ||      ||      |__|+-/~\\_|     ",
        "\\_/         \\_/  \\____/  \\____/  \\____/      \\_/       ",
    ),
    (
        "| /~~ ||   |-----/~~~~\\  /[I_____I][][] --|||_______|__",
        "------'|oOo|=[]=-      ||      ||      |  ||=======_|__",
        "/~\\____|___|/~\\_|  O=======O=======O   |__|+-/~\\_|     ",
        "\\_/         \\_/  \\____/  \\____/  \\____/      \\_/       ",
    ),
)

SMOKE = [
    [
        "(   )",
        "(    )",
        "(    )",
        "(   )",
        "(  )",
        "(  )",
        "( )",
        "( )",
        "()",
        "()",
        "O",
        "O",
        "O",
        "O",
        "O",
        " ",
    ],
    [
        "(@@@)",
        "(@@@@)",
        "(@@@@)",
        "(@@@)",
        "(@@)",
        "(@@)",
        "(@)",
        "(@)",
        "@@",
        "@@",
        "@",
        "@",
        "@",
        "@",
        "@",
        " ",
    ],
]
SMOKE_ERASER = [
    "     ",
    "      ",
    "      ",
    "     ",
    "    ",
    "    ",
    "   ",
    "   ",
    "  ",
    "  ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
]
SMOKE_DY = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
SMOKE_DX = [-2, -1, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3]


class SmokeClass:
    def __init__(self) -> None:
        self.y = 0
        self.x = 0
        self.pattern = 0
        self.kind = 0

    def update(self, y: int, x: int, pattern: int, kind: int) -> None:
        self.y = y
        self.x = x
        self.pattern = pattern
        self.kind = kind

    def __repr__(self) -> str:
        if self.y + self.x + self.pattern + self.kind == 0:
            return "\b"
        return f"Instance: {self.pattern}:{self.kind}"


class Args:  # pylint: disable=too-few-public-methods
    def __init__(self, arg: str) -> None:
        self.alert = "a" in arg
        self.little = arg.count("l")
        self.fly = "F" in arg
        self.c51 = "c" in arg
        self.red = "r" in arg


class Window:  # pylint: disable=too-few-public-methods
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols


def add_man(stdscr: curses.window, args: Args, y: int, x: int) -> None:
    man = [["", "(O)"], ["Help!", "\\O/"]]
    for i in range(2):
        addstr(stdscr, args, y + i, x, man[(LOGOLENGTH + x) // 12 % 2][i])


smokes = [SmokeClass() for _ in range(1000)]
smoke_sum = 0


def add_smoke(stdscr: curses.window, args: Args, y: int, x: int) -> None:
    global smoke_sum
    if x % 4 == 0:
        for i in range(smoke_sum):
            addstr(
                stdscr, args, smokes[i].y, smokes[i].x, SMOKE_ERASER[smokes[i].pattern]
            )
            smokes[i].y -= SMOKE_DY[smokes[i].pattern]
            smokes[i].x += SMOKE_DX[smokes[i].pattern]
            smokes[i].pattern += 1 if (smokes[i].pattern < 15) else 0
            addstr(
                stdscr,
                args,
                smokes[i].y,
                smokes[i].x,
                SMOKE[smokes[i].kind][smokes[i].pattern],
            )
        addstr(stdscr, args, y, x, SMOKE[smoke_sum % 2][0])
        smokes[smoke_sum].update(y, x, 0, smoke_sum % 2)
        smoke_sum += 1


def add_d51(stdscr: curses.window, x: int, args: Args, window: Window) -> int:
    d51 = tuple(
        (
            *D51BODY,
            *D51WHL[i],
            D51DEL,
        )
        for i in range(D51PATTERNS)
    )
    coal = [
        *COAL,
        COALDEL,
    ]

    if x < -D51LENGTH:
        return curses.ERR
    y = window.rows // 2 - 4
    if args.fly:
        y = (x // 7) + window.rows - (window.cols // 7) - D51HEIGHT
    for i in range(D51HEIGHT + 1):
        addstr(stdscr, args, y + i, x, d51[(D51LENGTH + x) % D51PATTERNS][i])
        if x + 53 <= window.cols:
            addstr(stdscr, args, y + i + int(args.fly), x + 53, coal[i])
    if args.alert:
        add_man(stdscr, args, y + 2, x + 43)
        add_man(stdscr, args, y + 2, x + 47)
    add_smoke(stdscr, args, y - 1, x + D51FUNNEL - 1)
    return curses.OK


def add_c51(stdscr: curses.window, x: int, args: Args, window: Window) -> int:
    c51 = tuple(
        (
            *C51BODY,
            *C51WHL[i],
            C51DEL,
        )
        for i in range(C51PATTERNS)
    )
    coal = [
        COALDEL,
        *COAL,
        COALDEL,
    ]

    if x < -C51LENGTH:
        return curses.ERR
    y = window.rows // 2 - 5
    extra_y_offset = 0
    if args.fly:
        y = (x // 7) + window.rows - (window.cols // 7) - C51HEIGHT
        extra_y_offset = 1
    for i in range(C51HEIGHT + 1):
        addstr(stdscr, args, y + i, x, c51[(C51LENGTH + x) % C51PATTERNS][i])
        addstr(stdscr, args, y + i + extra_y_offset, x + 53, coal[i])
    if args.alert:
        add_man(stdscr, args, y + 3, x + 45)
        add_man(stdscr, args, y + 3, x + 49)
    add_smoke(stdscr, args, y - 1, x + C51FUNNEL)
    return curses.OK


def add_sl(stdscr: curses.window, x: int, args: Args, window: Window) -> int:
    sl = tuple(
        (
            *LITTLE_BODY,
            *LITTLE_WHL[i],
            LITTLE_DEL,
        )
        for i in range(LITTLE_PATTERNS)
    )
    coal = (*LITTLE_COAL, LITTLE_DEL)
    car = (*LITTLE_CAR, LITTLE_DEL)
    count = 2 if args.alert else args.little
    logo_length = 21 * (count + 2)
    if x < -logo_length:
        return curses.ERR
    y = window.rows // 2 - 3
    a, b, c = 0, 0, 0
    b_mod = 0
    if args.fly:
        y = (x // 6) + window.rows - (window.cols // 6) - LOGOHEIGHT
        a, b, c = 2, 4, 6
    for i in range(LOGOHEIGHT + 1):
        addstr(stdscr, args, y + i, x, sl[(logo_length + x) // 3 % LITTLE_PATTERNS][i])
        addstr(stdscr, args, y + i + a, x + 21, coal[i])
        for car_index in range(count):
            if args.fly:
                b_mod = b + (2 * car_index)
            addstr(stdscr, args, y + i + b_mod, x + (car_index + 2) * 21, car[i])
    if args.alert:
        add_man(stdscr, args, y + 1, x + 14)
        add_man(stdscr, args, y + 1 + b, x + 45)
        add_man(stdscr, args, y + 1 + b, x + 53)
        add_man(stdscr, args, y + 1 + c, x + 66)
        add_man(stdscr, args, y + 1 + c, x + 74)
    add_smoke(stdscr, args, y - 1, x + LOGOFUNNEL)
    return curses.OK


def addstr(stdscr: curses.window, args: Args, y: int, x: int, string: str) -> int:
    i = x
    j = 0
    while i < 0:
        i += 1
        j += 1
        if j == len(string):
            return curses.ERR
    while j < len(string):
        try:
            stdscr.addch(y, i, string[j], curses.color_pair(1 if args.red else 0))
        except curses.error:
            return curses.ERR
        except IndexError:
            return curses.ERR
        i += 1
        j += 1
    return curses.OK


def init(stdscr: curses.window) -> None:
    curses.curs_set(0)
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    stdscr.nodelay(True)
    stdscr.timeout(40)


def main(stdscr: curses.window, args: Args) -> None:
    init(stdscr)
    window = Window(stdscr.getmaxyx()[0] - 1, stdscr.getmaxyx()[1] - 1)
    i = window.cols - 1
    while True:
        try:
            if args.little > 0:
                if add_sl(stdscr, i, args, window) == curses.ERR:
                    break
            elif args.c51:
                if add_c51(stdscr, i, args, window) == curses.ERR:
                    break
            else:
                if add_d51(stdscr, i, args, window) == curses.ERR:
                    break
            stdscr.getch()
            stdscr.refresh()
        except curses.error as e:
            raise e
        except KeyboardInterrupt:
            return
        i -= 1


if __name__ == "__main__":
    curses.wrapper(
        main,
        Args(
            sys.argv[1][1:] if len(sys.argv) > 1 and sys.argv[1].startswith("-") else ""
        ),
    )
