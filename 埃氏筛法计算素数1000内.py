#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()
#模块是对象，并且所有的模块都有一个内置属性 __name__。一个模块的 __name__ 的值取决于您如何应用模块。
#如果 import 一个模块，那么模块__name__ 的值通常为模块文件名，不带路径或者文件扩展名。
#但是您也可以像一个标准的程序样直接运行模块，在这种情况下, __name__ 的值将是一个特别缺省"__main__"。
