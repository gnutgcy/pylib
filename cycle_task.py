#! coding: utf-8


import time
import sys
from threading import Timer


def start(period):
    Timer(period, start, (period,)).start()
    print(time.time())
    pass


if __name__ == r"__main__":
    period = float(sys.argv[1])
    start(period)
    pass
