#!/bin/python3

import math
import os
import random
import re
import sys

user_int = int(input("Enter a number: "))

# User int is even else it's odd
if user_int % 2 == 0 and user_int > 2 and user_int < 5:
    print("Not Weird")
elif user_int % 2 == 0 and user_int > 6 and user_int < 20:
    print("Weird")
elif user_int % 2 == 0 and user_int > 20:
    print("Not Weird")
else:
    print("Weird")