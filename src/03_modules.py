"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print(sys.argv)

# Print out the OS platform you're using:
# YOUR CODE HERE - darwin
print(sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE - 40854
print(os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE - /Users/christinaharris/Lambda/comp-sci/Intro-Python-I
print(os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE -posix.uname_result(sysname='Darwin', nodename='Christinas-MacBook-Pro.local', release='19.4.0', version='Darwin Kernel Version 19.4.0: Wed Mar  4 22:28:40 PST 2020; root:xnu-6153.101.6~15/RELEASE_X86_64', machine='x86_64')
print(os.uname())
