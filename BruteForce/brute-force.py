#/usr/local/bin/python3
#-*- coding: utf-8 -*-
#===========================================
#
#           FILE: brute-force.py
#
#           USAGE:
#
#   DESCRIPTION: Brute-force String generation
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

import string # Common string operations

# string.printable String of ASCII characters which are considered printable. [digits, ascii_letters, punctuation, whitespace]
ALLOWED_CHARACTERS = string.printable
"""
string.digits = 0123456789
string.ascii_letters = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
string.whitespace = ' \t\n\r\x0b\x0c'

string.printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
"""
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS) # NUMBER_OF_CHARACTERS = 100

def characterToIndex(char):
    return ALLOWED_CHARACTERS.index(char)

def indexToCharacter(index):
    if NUMBER_OF_CHARACTERS <= index:
        raise ValueError("Index out of range.")
    else:
        return ALLOWED_CHARACTERS[index]

def next(string):
    """
    Get next sequence of characters.

    Treats characters as numbers (0-255). Foundation tries to increment
    character at the first position. If it fails, new character is
    added to the back of the list.

    It's basically a number with base = 256.

    :param string: A list of characters (can be empty).
    :type string: list
    :return: Next list of characters in the sequence
    :rettype: list
    """
    if len(string) <= 0:
        string.append(indexToCharacter(0))
    else:
        string[0] = indexToCharacter((characterToIndex(string[0]) +1) % NUMBER_OF_CHARACTERS)
        if characterToIndex(string[0]) is 0:
            return list(string[0]) + next(string[1:])

    return string

def main():
    sequence = list()
    while True:
        sequence = next(sequence)
        print(sequence)

if __name__ == "__main__":
    main()

