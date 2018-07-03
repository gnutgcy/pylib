# coding: utf-8


import ConfigParser


class ini_cfg:
    def __init__(self, cfg_file):
        self.cfg_ps = ConfigParser.ConfigParser()
        self.cfg_ps.read(cfg_file)
        pass

    def get(self, section, option):
        self.cfg_ps.get(section=section, option=option)
        pass


if __name__ == "__main__":
    pass
