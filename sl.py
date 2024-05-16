#!/usr/bin/env python3
"""
SL(1): Cure your bad habit of mistyping, but with python.

Original credit to mtoyoda.
"""

import curses
import sys
from dataclasses import dataclass
from enum import Enum

CTRL_C = 3

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

LITTLE_LENGTH = 21
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


class Smoke:
    """Represent the position, pattern, and type of each smoke particle."""

    def __init__(self) -> None:
        self.y = 0
        self.x = 0
        self.pattern = 0
        self.kind = 0

    def update(self, y: int, x: int, pattern: int, kind: int) -> None:
        """Setter for Smoke"""
        self.y = y
        self.x = x
        self.pattern = pattern
        self.kind = kind

    def __repr__(self) -> str:
        if self.y + self.x + self.pattern + self.kind == 0:
            return "\b"
        return f"Instance: {self.pattern}:{self.kind}"


class Args:  # pylint: disable=too-few-public-methods
    """
    Store command line arguments in a single convenient location.

    Similar to argparse.Namespace.
    """

    def __init__(self, arg: str) -> None:
        self.alert = "a" in arg
        self.little = arg.count("l")
        self.fly = "F" in arg
        self.c51 = "c" in arg
        self.red = "r" in arg


@dataclass
class Window:
    """Represent a window in terms of rows and columns"""

    rows: int
    cols: int


class TrainType(Enum):
    """Specify a type of train to render"""

    D51 = "d51"
    C51 = "c51"
    LITTLE = "little"


@dataclass
class TrainInfo:  # pylint: disable=too-many-instance-attributes
    """Dataclass representing a train by storing a number of attributes"""

    train: tuple[tuple[str, ...], ...]
    coal: tuple[str, ...]
    length: int
    height: int
    patterns: int
    y_offset: int
    man_y_offset: int
    man_x_offset: int
    smokestack_height: int
    car: tuple[str, ...]
    length_multiplier: int
    height_divisor: int
    coal_offset: int


class Train:  # pylint: disable=too-few-public-methods
    """Represent a renderable Train object"""

    def _get_train_info(self, train_type: TrainType) -> TrainInfo:
        return {
            TrainType.D51: TrainInfo(
                train=tuple(
                    (
                        *D51BODY,
                        *D51WHL[i],
                        D51DEL,
                    )
                    for i in range(D51PATTERNS)
                ),
                coal=(
                    *COAL,
                    COALDEL,
                ),
                length=83,
                height=10,
                patterns=D51PATTERNS,
                y_offset=4,
                man_y_offset=2,
                man_x_offset=43,
                smokestack_height=7,
                car=("",),
                length_multiplier=1,
                height_divisor=7,
                coal_offset=53,
            ),
            TrainType.C51: TrainInfo(
                train=tuple(
                    (
                        *C51BODY,
                        *C51WHL[i],
                        C51DEL,
                    )
                    for i in range(C51PATTERNS)
                ),
                coal=(
                    COALDEL,
                    *COAL,
                    COALDEL,
                ),
                length=87,
                height=11,
                patterns=C51PATTERNS,
                y_offset=5,
                man_y_offset=3,
                man_x_offset=45,
                smokestack_height=7,
                car=("",),
                length_multiplier=1,
                height_divisor=7,
                coal_offset=53,
            ),
            TrainType.LITTLE: TrainInfo(
                train=tuple(
                    (
                        *LITTLE_BODY,
                        *LITTLE_WHL[i],
                        LITTLE_DEL,
                    )
                    for i in range(LITTLE_PATTERNS)
                ),
                coal=(*LITTLE_COAL, LITTLE_DEL),
                length=21,
                height=6,
                patterns=LITTLE_PATTERNS,
                y_offset=3,
                man_y_offset=1,
                man_x_offset=14,
                smokestack_height=4,
                car=(*LITTLE_CAR, LITTLE_DEL),
                length_multiplier=2,
                height_divisor=6,
                coal_offset=21,
            ),
        }[train_type]

    def __init__(
        self,
        type_: TrainType,
        stdscr: curses.window,
        window: Window,
        args: Args,
    ) -> None:
        self._smokes = [Smoke() for _ in range(window.cols)]
        self._smoke_sum = 0
        self._stdscr = stdscr
        self._window = window
        self._args = args
        self._info = self._get_train_info(type_)

    def _add_smoke(self, y: int, x: int) -> None:
        if x % 4 == 0:
            for i in range(self._smoke_sum):
                self._addstr(
                    self._smokes[i].y,
                    self._smokes[i].x,
                    SMOKE_ERASER[self._smokes[i].pattern],
                )
                self._smokes[i].y -= SMOKE_DY[self._smokes[i].pattern]
                self._smokes[i].x += SMOKE_DX[self._smokes[i].pattern]
                self._smokes[i].pattern += 1 if (self._smokes[i].pattern < 15) else 0
                self._addstr(
                    self._smokes[i].y,
                    self._smokes[i].x,
                    SMOKE[self._smokes[i].kind][self._smokes[i].pattern],
                )
            self._addstr(y, x, SMOKE[self._smoke_sum % 2][0])
            self._smokes[self._smoke_sum].update(y, x, 0, self._smoke_sum % 2)
            self._smoke_sum += 1

    def _add_man(self, y: int, x: int) -> None:
        man = [["", "(O)"], ["Help!", "\\O/"]]
        for i in range(2):
            self._addstr(y + i, x, man[(LITTLE_LENGTH * 4 + x) // 12 % 2][i])

    def _addstr(self, y: int, x: int, string: str) -> int:
        i = x
        j = 0
        while i < 0:
            i += 1
            j += 1
            if j == len(string):
                return curses.ERR
        while j < len(string):
            try:
                self._stdscr.addch(
                    y,
                    i,
                    string[j],
                    curses.color_pair(1 if self._args.red else 0),
                )
            except curses.error:
                return curses.ERR
            except IndexError:
                return curses.ERR
            i += 1
            j += 1
        return curses.OK

    def add_train(self, x: int) -> int:
        """Public render function. Display self._info at the specified `x`"""
        train = self._info
        length = train.length * (self._args.little + train.length_multiplier)
        if x < -length:
            return curses.ERR
        y = self._window.rows // 2 - train.y_offset
        if self._args.fly:
            y = (
                (x // train.height_divisor)
                + self._window.rows
                - (self._window.cols // train.height_divisor)
                - train.height
            )
        for i in range(train.height + 1):
            self._addstr(
                y + i,
                x,
                train.train[(length + x) % train.patterns][i],
            )
            self._addstr(
                y + i + int(self._args.fly) * train.length_multiplier,
                x + train.coal_offset,
                train.coal[i],
            )
            for car in range(self._args.little):
                self._addstr(
                    y + i + int(self._args.fly) * (4 + 2 * car),
                    x + (car + 2) * train.length,
                    train.car[i],
                )
        if self._args.alert:
            self._add_man(y + train.man_y_offset, x + train.man_x_offset)
            if self._args.little == 0:
                self._add_man(y + train.man_y_offset, x + train.man_x_offset + 4)
            for car in range(self._args.little):
                self._add_man(
                    y + train.man_y_offset + int(self._args.fly) * ((car + 1) * 2 + 2),
                    x + (train.length * car + 45),
                )
                self._add_man(
                    y + train.man_y_offset + int(self._args.fly) * ((car + 1) * 2 + 2),
                    x + (train.length * car + 45) + 8,
                )
        self._add_smoke(y - 1, x + train.smokestack_height)
        return curses.OK


def get_train_type(args: Args) -> TrainType:
    """Return the type of the train based on the command line arguments"""
    if args.little > 0:
        return TrainType.LITTLE
    if args.c51:
        return TrainType.C51
    return TrainType.D51


def main(stdscr: curses.window, args: Args) -> None:
    """Entry point for Steam Locomotive"""
    curses.curs_set(0)
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    stdscr.nodelay(True)
    stdscr.timeout(35)
    window = Window(stdscr.getmaxyx()[0] - 1, stdscr.getmaxyx()[1] - 1)
    i = window.cols - 1
    train = Train(get_train_type(args), stdscr, window, args)
    while True:
        try:
            if train.add_train(i) == curses.ERR:
                break
            if stdscr.getch() == CTRL_C:
                return
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
