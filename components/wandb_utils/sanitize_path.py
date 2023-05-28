'''
 # @ Author: Duy Nam
 # @ Email: nam.nd.00@gmail.com
 # @ Create Time: 2023-05-25 21:34:21
 # @ Modified by: Duy Nam
 # @ Modified time: 2023-05-25 21:35:47
 '''

import os


def sanitize_path(s):
    """
    Sanitizes the input path by:

    1. Expanding environment variables
    2. Expanding the home directory ('~')
    3. Calculating the absolute path

    :param s: input path
    :return: a sanitized version of the input path
    """
    return os.path.abspath(os.path.expanduser(os.path.expandvars(s)))
