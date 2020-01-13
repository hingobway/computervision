import cv2 as cv
import numpy as np



def findClosest(arr, n, target):

    if (target <= arr[0]):
        return arr[0]
    if (target >= arr[n - 1]):
        return arr[n - 1]


    i = 0;
    j = n;
    mid = 0
    while (i < j):
        mid = (i + j) / 2

        if (arr[mid] == target):
            return arr[mid]

        if (target < arr[mid]):

            if (mid > 0 and target > arr[mid - 1]):
                return getClosest(arr[mid - 1], arr[mid], target)


            j = mid

        else:
            if (mid < n - 1 and target < arr[mid + 1]):
                return getClosest(arr[mid], arr[mid + 1], target)


            i = mid + 1

    return arr[mid]


# Method to compare which one is the more close.
# We find the closest by taking the difference
# between the target and both values. It assumes
# that val2 is greater than val1 and target lies
# between these two.
def getClosest(val1, val2, target):
    if (target - val1 >= val2 - target):
        return val2
    else:
        return val1