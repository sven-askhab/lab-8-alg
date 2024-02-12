#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def merge_sort(arr):
    if not arr or arr == [arr[0]]:
        return arr, 0
    else:
        middle = len(arr) // 2
        left, inv_left = merge_sort(arr[:middle])
        right, inv_right = merge_sort(arr[middle:])
        merged, inv_merge = merge(left, right)
        return merged, inv_left + inv_right + inv_merge


def merge(left, right):


    def merge_helper(l, r, acc, inv_count):
        if not l:
            return acc + r, inv_count
        if not r:
            return acc + l, inv_count
        if l[0] <= r[0]:
            return merge_helper(l[1:], r, acc + [l[0]], inv_count)
        else:
            return merge_helper(l, r[1:], acc + [r[0]], inv_count + len(l))


    return merge_helper(left, right, [], 0)


def main():
    arr = [6, 4, 1, 2, 8, 7, 3, 5]
    sorted_arr, inversions = merge_sort(arr)
    print("Отсортированный массив:", sorted_arr)
    print("Количество инверсий:", inversions)


if __name__ == '__main__':
    main()
