# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 10:39:40 2023

@author: End-User
"""

def say_hello(to):
    return f"Hello {to}!"

def main():
    name = input("Name")
    print(say_hello(name))
    
if __name__=="__main":
    main()