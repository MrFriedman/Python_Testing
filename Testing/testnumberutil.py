# Coding for a doctest to check the validity of all paths in a program to output a number in the word form
# Author: Dylan Friedman
# FRDDYL002
# 12th April 2022
# testnumberutil.py
"""
>>> import numberutil
>>> numberutil.aswords(420)
'four hundred and twenty'

>>> numberutil.aswords(42)
'forty two'

>>> numberutil.aswords(100)
'one hundred'

>>> numberutil.aswords(422)
'four hundred and twenty two'

>>> numberutil.aswords(402)
'four hundred and two'

>>> numberutil.aswords(440)
'four hundred and forty'

>>> numberutil.aswords(0)
'zero'

>>> numberutil.aswords(11)
'eleven'

"""
import doctest
doctest.testmod(verbose=True)