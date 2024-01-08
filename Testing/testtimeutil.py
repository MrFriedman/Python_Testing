# Coding for a doctest to varify the formatting of a digital time reading
# Author: Dylan Friedman
# FRDDYL002
# 16th April 2022
# testtimeutil.py
"""
>>> import timeutil
>>> timeutil.validate(':02 p.m.')
False

>>> timeutil.validate('111:02 p.m.')
False

>>> timeutil.validate('02:02 p.m.')
False

>>> timeutil.validate('12:02 pm')
False

>>> timeutil.validate('12:111 p.m.')
False

>>> timeutil.validate('12:02 p.m.')
True

"""
import doctest
doctest.testmod(verbose=True)
