# coding: utf-8


import datetime


def record(info):
    msg = "%s - %s\n" % (str(datetime.datetime.now()), str(info))
    print(msg)
    pass


if __name__ == "__main__":
    pass
