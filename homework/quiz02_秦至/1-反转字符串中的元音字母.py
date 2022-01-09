# -*- coding: utf-8 -*-
"""
@Time : 2022/1/9 13:06 -> 13:15
@Author : Zhi QIN 
@File : 1-反转字符串中的元音字母.py 
@Software: PyCharm
@Brief :
1. 反转字符串中的元音字母

编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1：
输入："hello"
输出："holle"

示例 2：
输入："leetcode"
输出："leotcede"

提示：元音字母不包含字母 "y" 。
"""


def inverse_vowel(word):
    vowels = 'aeiou'
    word_list = list(word)
    length = len(word)
    if length < 2:
        return word
    prev, post = 0, length - 1
    while post > prev:
        if word_list[prev] not in vowels:
            prev += 1
        if word_list[post] not in vowels:
            post -= 1

        if word_list[prev] in vowels and word_list[post] in vowels:
            word_list[prev], word_list[post] = word_list[post], word_list[prev]
            prev += 1
            post -= 1

    return ''.join(word_list)


if __name__ == '__main__':
    word = 'leetcode'
    print(inverse_vowel(word))
