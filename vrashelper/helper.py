'''
This file contains useful funtions for working with python

Will get updated throughout the semester

Author: Victor Rasmussen
'''

import os


def work_here():
    current_dir = os.getcwd()  # Store current working directory
    calling_dir = os.path.abspath(os.path.curdir)  # Get directory from which the script is called
    os.chdir(calling_dir)




class colorbank:
    default = '\033[0m'
    hackergreen = '\x1b[38;5;118m'
    white = '\x1b[37m'
    error_red = '\033[31m'
    warning = "\033[0;33m"
    blue= "\033[0;34m"


class ctext:
    nline = "\n"
    bold = "\033[1m"
    default = '\033[0m'
    remove_line = "\033[A                             \033[A"