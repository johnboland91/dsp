# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    count = 0
    for word in words:
        if len(word) >= 2:
            count += 1
        elif word[0] == word[-1]:
            count += 1
    return count 


def front_x(words):
    x_list = [x for x in words if x[0] == "x"]
    words_list = [x for x in words if x[0] != "x"]
    x_list.sort()
    words_list.sort()
    x_list.extend(words_list)
    return x_list


def sort_last(tuples):
    sort_tuple = sorted(tuples, key = lambda x: x[-1])
    return sort_tuple


def remove_adjacent(nums):
    return [nums[i] for i in range(0,len(nums)) if nums[i] != nums[abs(i-1)]]


def linear_merge(list1, list2):
    def linear_merge(list1, list2):
    list1.extend(list2)
    list1.sort()
    return list1
