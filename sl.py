#!/usr/bin/env python3
# pylint: disable=missing-docstring

import curses
import sys

D51HEIGHT = 10
D51FUNNEL = 7
D51LENGTH = 83
D51PATTERNS = 6


D51STR1 = "      ====        ________                ___________ "
D51STR2 = "  _D _|  |_______/        \\__I_I_____===__|_________| "
D51STR3 = "   |(_)---  |   H\\________/ |   |        =|___ ___|   "
D51STR4 = "   /     |  |   H  |  |     |   |         ||_| |_||   "
D51STR5 = "  |      |  |   H  |__--------------------| [___] |   "
D51STR6 = "  | ________|___H__/__|_____/[][]~\\_______|       |   "
D51STR7 = "  |/ |   |-----------I_____I [][] []  D   |=======|__ "

D51WHL11 = "__/ =| o |=-~~\\  /~~\\  /~~\\  /~~\\ ____Y___________|__ "
D51WHL12 = " |/-=|___|=    ||    ||    ||    |_____/~\\___/        "
D51WHL13 = "  \\_/      \\O=====O=====O=====O_/      \\_/            "

D51WHL21 = "__/ =| o |=-~~\\  /~~\\  /~~\\  /~~\\ ____Y___________|__ "
D51WHL22 = " |/-=|___|=O=====O=====O=====O   |_____/~\\___/        "
D51WHL23 = "  \\_/      \\__/  \\__/  \\__/  \\__/      \\_/            "

D51WHL31 = "__/ =| o |=-O=====O=====O=====O \\ ____Y___________|__ "
D51WHL32 = " |/-=|___|=    ||    ||    ||    |_____/~\\___/        "
D51WHL33 = "  \\_/      \\__/  \\__/  \\__/  \\__/      \\_/            "

D51WHL41 = "__/ =| o |=-~O=====O=====O=====O\\ ____Y___________|__ "
D51WHL42 = " |/-=|___|=    ||    ||    ||    |_____/~\\___/        "
D51WHL43 = "  \\_/      \\__/  \\__/  \\__/  \\__/      \\_/            "

D51WHL51 = "__/ =| o |=-~~\\  /~~\\  /~~\\  /~~\\ ____Y___________|__ "
D51WHL52 = " |/-=|___|=   O=====O=====O=====O|_____/~\\___/        "
D51WHL53 = "  \\_/      \\__/  \\__/  \\__/  \\__/      \\_/            "

D51WHL61 = "__/ =| o |=-~~\\  /~~\\  /~~\\  /~~\\ ____Y___________|__ "
D51WHL62 = " |/-=|___|=    ||    ||    ||    |_____/~\\___/        "
D51WHL63 = "  \\_/      \\_O=====O=====O=====O/      \\_/            "

D51DEL = "                                                      "

COAL01 = "                              "
COAL02 = "                              "
COAL03 = "    _________________         "
COAL04 = "   _|                \\_____A  "
COAL05 = " =|                        |  "
COAL06 = " -|                        |  "
COAL07 = "__|________________________|_ "
COAL08 = "|__________________________|_ "
COAL09 = "   |_D__D__D_|  |_D__D__D_|   "
COAL10 = "    \\_/   \\_/    \\_/   \\_/    "

COALDEL = "                              "

LOGOHEIGHT = 6
LOGOFUNNEL = 4
LOGOLENGTH = 84
LOGOPATTERNS = 6

LOGO1 = "     ++      +------ "
LOGO2 = "     ||      |+-+ |  "
LOGO3 = "   /---------|| | |  "
LOGO4 = "  + ======== +-+ |  "

LWHL11 = " _|--O========O~\\-+  "
LWHL12 = "//// \\_/      \\_/    "

LWHL21 = " _|--/O========O\\-+  "
LWHL22 = "//// \\_/      \\_/    "

LWHL31 = " _|--/~O========O-+  "
LWHL32 = "//// \\_/      \\_/    "

LWHL41 = " _|--/~\\------/~\\-+  "
LWHL42 = "//// \\_O========O    "

LWHL51 = " _|--/~\\------/~\\-+  "
LWHL52 = "//// \\O========O/    "

LWHL61 = " _|--/~\\------/~\\-+  "
LWHL62 = "//// O========O_/    "

LCOAL1 = "____                 "
LCOAL2 = "|   \\@@@@@@@@@@@     "
LCOAL3 = "|    \\@@@@@@@@@@@@@_ "
LCOAL4 = "|                  | "
LCOAL5 = "|__________________| "
LCOAL6 = "   (O)       (O)     "

LCAR1 = "____________________ "
LCAR2 = "|  ___ ___ ___ ___ | "
LCAR3 = "|  |_| |_| |_| |_| | "
LCAR4 = "|__________________| "
LCAR5 = "|__________________| "
LCAR6 = "   (O)        (O)    "

DELLN = "                     "

C51HEIGHT = 11
C51FUNNEL = 7
C51LENGTH = 87
C51PATTERNS = 6

C51DEL = "                                                       "

C51STR1 = "        ___                                            "
C51STR2 = "       _|_|_  _     __       __             ___________"
C51STR3 = "    D__/   \\_(_)___|  |__H__|  |_____I_Ii_()|_________|"
C51STR4 = "     | `---'   |:: `--'  H  `--'         |  |___ ___|  "
C51STR5 = "    +|~~~~~~~~++::~~~~~~~H~~+=====+~~~~~~|~~||_| |_||  "
C51STR6 = "    ||        | ::       H  +=====+      |  |::  ...|  "
C51STR7 = "|    | _______|_::-----------------[][]-----|       |  "

C51WH61 = "| /~~ ||   |-----/~~~~\\  /[I_____I][][] --|||_______|__"
C51WH62 = "------'|oOo|==[]=-     ||      ||      |  ||=======_|__"
C51WH63 = "/~\\____|___|/~\\_|   O=======O=======O  |__|+-/~\\_|     "
C51WH64 = "\\_/         \\_/  \\____/  \\____/  \\____/      \\_/       "

C51WH51 = "| /~~ ||   |-----/~~~~\\  /[I_____I][][] --|||_______|__"
C51WH52 = "------'|oOo|===[]=-    ||      ||      |  ||=======_|__"
C51WH53 = "/~\\____|___|/~\\_|    O=======O=======O |__|+-/~\\_|     "
C51WH54 = "\\_/         \\_/  \\____/  \\____/  \\____/      \\_/       "

C51WH41 = "| /~~ ||   |-----/~~~~\\  /[I_____I][][] --|||_______|__"
C51WH42 = "------'|oOo|===[]=- O=======O=======O  |  ||=======_|__"
C51WH43 = "/~\\____|___|/~\\_|      ||      ||      |__|+-/~\\_|     "
C51WH44 = "\\_/         \\_/  \\____/  \\____/  \\____/      \\_/       "

C51WH31 = "| /~~ ||   |-----/~~~~\\  /[I_____I][][] --|||_______|__"
C51WH32 = "------'|oOo|==[]=- O=======O=======O   |  ||=======_|__"
C51WH33 = "/~\\____|___|/~\\_|      ||      ||      |__|+-/~\\_|     "
C51WH34 = "\\_/         \\_/  \\____/  \\____/  \\____/      \\_/       "

C51WH21 = "| /~~ ||   |-----/~~~~\\  /[I_____I][][] --|||_______|__"
C51WH22 = "------'|oOo|=[]=- O=======O=======O    |  ||=======_|__"
C51WH23 = "/~\\____|___|/~\\_|      ||      ||      |__|+-/~\\_|     "
C51WH24 = "\\_/         \\_/  \\____/  \\____/  \\____/      \\_/       "

C51WH11 = "| /~~ ||   |-----/~~~~\\  /[I_____I][][] --|||_______|__"
C51WH12 = "------'|oOo|=[]=-      ||      ||      |  ||=======_|__"
C51WH13 = "/~\\____|___|/~\\_|  O=======O=======O   |__|+-/~\\_|     "
C51WH14 = "\\_/         \\_/  \\____/  \\____/  \\____/      \\_/       "

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
        self.ptrn = 0
        self.kind = 0

    def update(self, y: int, x: int, ptrn: int, kind: int) -> None:
        self.y = y
        self.x = x
        self.ptrn = ptrn
        self.kind = kind

    def __repr__(self) -> str:
        if self.y + self.x + self.ptrn + self.kind == 0:
            return "\b"
        return f"Instance: {self.ptrn}:{self.kind}"


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
            addstr(stdscr, args, smokes[i].y, smokes[i].x, SMOKE_ERASER[smokes[i].ptrn])
            smokes[i].y -= SMOKE_DY[smokes[i].ptrn]
            smokes[i].x += SMOKE_DX[smokes[i].ptrn]
            smokes[i].ptrn += 1 if (smokes[i].ptrn < 15) else 0
            addstr(
                stdscr,
                args,
                smokes[i].y,
                smokes[i].x,
                SMOKE[smokes[i].kind][smokes[i].ptrn],
            )
        addstr(stdscr, args, y, x, SMOKE[smoke_sum % 2][0])
        smokes[smoke_sum].update(y, x, 0, smoke_sum % 2)
        smoke_sum += 1


def add_d51(stdscr: curses.window, x: int, args: Args, window: Window) -> int:
    d51 = [
        [
            D51STR1,
            D51STR2,
            D51STR3,
            D51STR4,
            D51STR5,
            D51STR6,
            D51STR7,
            D51WHL11,
            D51WHL12,
            D51WHL13,
            D51DEL,
        ],
        [
            D51STR1,
            D51STR2,
            D51STR3,
            D51STR4,
            D51STR5,
            D51STR6,
            D51STR7,
            D51WHL21,
            D51WHL22,
            D51WHL23,
            D51DEL,
        ],
        [
            D51STR1,
            D51STR2,
            D51STR3,
            D51STR4,
            D51STR5,
            D51STR6,
            D51STR7,
            D51WHL31,
            D51WHL32,
            D51WHL33,
            D51DEL,
        ],
        [
            D51STR1,
            D51STR2,
            D51STR3,
            D51STR4,
            D51STR5,
            D51STR6,
            D51STR7,
            D51WHL41,
            D51WHL42,
            D51WHL43,
            D51DEL,
        ],
        [
            D51STR1,
            D51STR2,
            D51STR3,
            D51STR4,
            D51STR5,
            D51STR6,
            D51STR7,
            D51WHL51,
            D51WHL52,
            D51WHL53,
            D51DEL,
        ],
        [
            D51STR1,
            D51STR2,
            D51STR3,
            D51STR4,
            D51STR5,
            D51STR6,
            D51STR7,
            D51WHL61,
            D51WHL62,
            D51WHL63,
            D51DEL,
        ],
    ]
    coal = [
        COAL01,
        COAL02,
        COAL03,
        COAL04,
        COAL05,
        COAL06,
        COAL07,
        COAL08,
        COAL09,
        COAL10,
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
    c51 = [
        [
            C51STR1,
            C51STR2,
            C51STR3,
            C51STR4,
            C51STR5,
            C51STR6,
            C51STR7,
            C51WH11,
            C51WH12,
            C51WH13,
            C51WH14,
            C51DEL,
        ],
        [
            C51STR1,
            C51STR2,
            C51STR3,
            C51STR4,
            C51STR5,
            C51STR6,
            C51STR7,
            C51WH21,
            C51WH22,
            C51WH23,
            C51WH24,
            C51DEL,
        ],
        [
            C51STR1,
            C51STR2,
            C51STR3,
            C51STR4,
            C51STR5,
            C51STR6,
            C51STR7,
            C51WH31,
            C51WH32,
            C51WH33,
            C51WH34,
            C51DEL,
        ],
        [
            C51STR1,
            C51STR2,
            C51STR3,
            C51STR4,
            C51STR5,
            C51STR6,
            C51STR7,
            C51WH41,
            C51WH42,
            C51WH43,
            C51WH44,
            C51DEL,
        ],
        [
            C51STR1,
            C51STR2,
            C51STR3,
            C51STR4,
            C51STR5,
            C51STR6,
            C51STR7,
            C51WH51,
            C51WH52,
            C51WH53,
            C51WH54,
            C51DEL,
        ],
        [
            C51STR1,
            C51STR2,
            C51STR3,
            C51STR4,
            C51STR5,
            C51STR6,
            C51STR7,
            C51WH61,
            C51WH62,
            C51WH63,
            C51WH64,
            C51DEL,
        ],
    ]
    coal = [
        COALDEL,
        COAL01,
        COAL02,
        COAL03,
        COAL04,
        COAL05,
        COAL06,
        COAL07,
        COAL08,
        COAL09,
        COAL10,
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
    sl = [
        [LOGO1, LOGO2, LOGO3, LOGO4, LWHL11, LWHL12, DELLN],
        [LOGO1, LOGO2, LOGO3, LOGO4, LWHL21, LWHL22, DELLN],
        [LOGO1, LOGO2, LOGO3, LOGO4, LWHL31, LWHL32, DELLN],
        [LOGO1, LOGO2, LOGO3, LOGO4, LWHL41, LWHL42, DELLN],
        [LOGO1, LOGO2, LOGO3, LOGO4, LWHL51, LWHL52, DELLN],
        [LOGO1, LOGO2, LOGO3, LOGO4, LWHL61, LWHL62, DELLN],
    ]
    coal = [LCOAL1, LCOAL2, LCOAL3, LCOAL4, LCOAL5, LCOAL6, DELLN]
    car = [LCAR1, LCAR2, LCAR3, LCAR4, LCAR5, LCAR6, DELLN]
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
        addstr(stdscr, args, y + i, x, sl[(logo_length + x) // 3 % LOGOPATTERNS][i])
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
