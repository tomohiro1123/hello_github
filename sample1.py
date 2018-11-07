#!/usr/bin/env python
class Test():
    def hyouka(self, num):
        if num > 50:
            print("pass")
        else:
            print("fail")

if __name__ == "__main__":
    test = Test()
    test.hyouka(30)