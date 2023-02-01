#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 3)
print(type(res))
print(res)

res = index_range(page=3000, page_size=100)
print(type(res))
print(res)



#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('1-simple_pagination').Server

server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print("AssertionError raised with 0")

try:
    should_err = server.get_page(2, 'Bob')
except AssertionError:
    print("AssertionError raised when page and/or page_size are not ints")


print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))
#print(server.dataset())
