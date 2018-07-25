#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

tobytes = \
    input('Enter the value you need converted from char to bytes: ')
converted = len(tobytes.encode('utf8'))
print('')
print('')
sys.stdout.write('Length of String in Bytes: ')
print(converted)
sys.stdout.flush
