#!/usr//bin/env python3
#-*- coding: utf-8 -*-
#===========================================
#
#           FILE: brute-force02.py
#
#           USAGE:
#
#   DESCRIPTION: Password cracker using literal brute force,searching each character
#               to see if it matches an ASCII character.0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
#               The password is randomly generated and will vary from 100,000 to 250,000 characters long.
#
#       OPTIONS: ----
#  REQUIREMENTS: ----
#          BUGS: ----
#         NOTES: ----
#        AUTHOR: Chyi Yaqing
#  ORGANIZATION:
#       VERSION: 0.1.0
#       CREATED: 04/24/2017
#      REVISION: ----
#      Copyright © 2017 Chyi Yaqing
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software FOundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAB PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#===================================================================
import random
import time
import string

"""
Whenever you are doing string addition in Python, you are probably doing it wrong.
As a fix, use list and str.join
"""

password = ""
attempted_password = ""
#list_of_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
list_of_chars = string.digits + string.ascii_letters

for _ in range(random.randint(64, 128)): # range() function will already start from zero
    password += list_of_chars[random.randint(0, 61)]

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("The function {.__name__} took {:.15f} seconds to finish.".format(func, time.time() - start))
        return result
    return wrapper

@timeit
def solve_password(word):
    global attempted_password
    for character in word:
        for entry in list_of_chars:
            if character == entry:
                attempted_password += character
                continue
    return attempted_password

print("The password: {0:}\nLength of password was: {1:}\nIs correct? : {2:}".format(solve_password(password),len(password), attempted_password == password))


def create_password(chars):
    password = []
    for _ in range(random.randint(64,128)):
        password.append(random.choice(chars))
    return "".join(password)
print("The password: {0:}\nLength of password was: {1:}".format(create_password(list_of_chars), len(create_password(list_of_chars))))
