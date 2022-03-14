#!/usr/bin/env python3
"""
Demonstrates how to examine attributes of objects
"""

myobj = {10,20,30,40,50 }

for myattr in dir(myobj):
    print ('{}, {}'.format(myattr, getattr(myobj,myattr)))
