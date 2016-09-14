# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-09-06 21:01:37
# @Last Modified by:   boyac
# @Last Modified time: 2016-09-15 00:40:39


'''
Questions:
Problem 1
The sentence "A quick brown fox jumps over the lazy dog" contains
every single letter in the alphabet. Such sentences are called pangrams.
You are to write a method getMissingLetters, which takes a String,
sentence, and returns all the letters it is missing (which prevent it
from being a pangram). You should ignore the case of the letters in sentence,
and your return should be all lower case letters, in alphabetical order.
You should also ignore all non US-ASCII characters.

The code you submit must contain a method that conforms to the expected
method signature, as follows:

Java Definition
Public Class: MissingLetters
Method signature: public String getMissingLetters(String sentence)

C++ Definition
Function signature: string getMissingLetters(const string& sentence)

C Definition
Function signature: char *getMissingLetters(const char *sentence)

Here the return value is a dynamically allocated string,
which can be free'd using free(result). If the function fails
because it cannot allocate memory it should return NULL.

Examples:
(Note that in the examples below, the double quotes should not be
considered part of the input or output strings.)

0)  "A quick brown fox jumps over the lazy dog"
Returns: "" 
(This sentence contains every letter)

1)  "A slow yellow fox crawls under the proactive dog"
Returns: "bjkmqz"

2)  "Lions, and tigers, and bears, oh my!"
Returns: "cfjkpquvwxz"

3)  ""
Returns: "abcdefghijklmnopqrstuvwxyz"
'''


from string import ascii_lowercase as al

def getMissingLetters(string):
    return ''.join(set(al) - set(string.lower()))



if __name__ == '__main__':
	print getMissingLetters('A quick brown fox jumps over the lazy dog') # ''
	print getMissingLetters('A slow yellow fox crawls under the proactive dog') # bkjmqz
	print getMissingLetters('Lions, and tigers, and bears, oh my!') # cfkjqpuwvxz
	print getMissingLetters('') # acbedgfihkjmlonqpsrutwvyxz