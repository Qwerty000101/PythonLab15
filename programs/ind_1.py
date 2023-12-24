#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def decorator_parameters(chars = " !?"):
    def decorator_translate(function):
        import re
        
        def wrapper(n):
            result = function(n)

            for item in set(result):
                if item in chars:
                    result = result.replace(item,"-")

            result = re.sub(r'-+', '-', result)
            return result
        
        return wrapper
    
    return decorator_translate


@decorator_parameters("?!:;,. ")
def translate(n):
    result = n.lower()
    elements = set(result)

    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g',
        'д': 'd', 'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya'}
    
    keys_lst = list(t.keys())

    for item in elements:
        if item in keys_lst:
            result = result.replace(item,t[item])

    return result


if __name__ == "__main__":
    while True:
        n = input("Введите строку: ")

        if n == "exit":
            break

        print(translate(n))