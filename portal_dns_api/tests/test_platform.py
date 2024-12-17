"""
    Кроссплатформенный модуль python, который дает информацию об архитектуре машины,
    операционной системе и её версии, версии Python.
"""

import platform


def test():
    dd = platform.python_version()
    return f'Hi test! {dd}'

rr = test()
print(rr)