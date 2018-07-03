# coding: utf-8


import unittest
import HTMLTestRunner


def RunTestCases(title, description, testcases_path, testcases_re, report_file):
    with open(report_file, 'wb') as report_stream:
        runner = HTMLTestRunner.HTMLTestRunner(stream=report_stream,
                                               title=title,
                                               description=description)
        discover = unittest.defaultTestLoader.discover(start_dir=testcases_path,
                                                       pattern=testcases_re,
                                                       top_level_dir=None)
        runner.run(discover)
    pass


if __name__ == "__main__":
    pass
