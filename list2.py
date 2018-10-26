#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""
Title: backend list assessment

purpose: more practice on list manipulation in python

Answer Author: Aaron Jackson
Github: TimeApollo

"""

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    """reduces same adjacent elements to one instance in list"""
    if len(nums) == 0: return []
    new_list = [nums[0]]
    for count , num in enumerate(nums[1:]):
        if num != nums[count]: new_list.append(num)
    return new_list


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    """merging sorted lists into a sorted list while iterating through both"""
    total_len = len(list1) + len(list2)
    index_list1 = index_list2 = 0
    result = []
    while len(result) < total_len:
        if len(list1) == index_list1:
            result += list2[index_list2:]
        elif len(list2) == index_list2:
            result += list1[index_list1:]
        elif list1[index_list1] < list2[index_list2]:
            result.append(list1[index_list1])
            index_list1 += 1
        else:
            result.append(list2[index_list2])
            index_list2 += 1
    return result



# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])
    test(remove_adjacent([1,2,3,1,1,3,3,4,4,1,2,3]),[1,2,3,1,3,4,1,2,3])

    print('linear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])

# Standard boilerplate (python idiom) to call the main() function.
if __name__ == '__main__':
    main()
