import msvcrt
import os
import shutil
import random
import sys
import time
import math
import msvcrt as key


def bubbleSort(list_a):
    st = time.time()
    ifSorted = False
    while not ifSorted:
        ifSorted = True
        for i in range(0, len(list_a) - 1):
                if list_a[i] > list_a[i+1]:
                    ifSorted = False
                    list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    et = time.time()
    runningTime = et - st
    print("\nElapsed time for Bubble sort in " + str(listLength) + " element list is: " + str(round(runningTime, 2)) + " seconds")
    return list_a

def selectionSort(list_a):
    st = time.time()
    list_length = range(0, len(list_a) - 1)
    for i in list_length:
        min_value = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j
        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]
    et = time.time()
    runningTime = et - st
    print("\nElapsed time for Selection sort in " + str(listLength) + " element list is: " + str(round(runningTime, 2)) + " seconds")
    return list_a

def insertionSort(list_a):
    st = time.time()
    list_length = range(1, len(list_a))
    for i in list_length:
        value_to_sort = list_a[i]

        while list_a[i - 1] > value_to_sort and i > 0:
            list_a[i], list_a[i - 1] = list_a[i - 1], list_a[i]
            i -= 1
    et = time.time()
    runningTime = et - st
    print("\nElapsed time for Insertion sort in " + str(listLength) + " element list is: " + str(round(runningTime, 2)) + " seconds")
    return list_a

def quickSort(list_a):
    st = time.time()
    length = len(list_a)
    if length<=1:
        return list_a
    else:
        pivot = list_a.pop()

    biggerItems = []
    smallerItems = []
    for item in list_a:
        if item > pivot:
            biggerItems.append(item)
        else:
            smallerItems.append(item)
    if(len(list_a) + 2 == listLength):
        et = time.time()
        runningTime = et - st
        print("\nElapsed time for Quick sort in " + str(listLength) + " element list is: " + str(round(runningTime, 2)) + " seconds")
    return quickSort(smallerItems) + [pivot] + quickSort(biggerItems)

def toString(list_a):
    for y in list_a:
        print(y, end=" ")

def Convert(string):
    list1 = list(string.split())
    return list1
while True:
    try:
        randomList = []
        sys.setrecursionlimit(10000000)

        print("Please type down size of tabel to sort:")
        listLength = int(input())

        if listLength < 0:
            print("Size of your tabel must be higher than 0.")
            print("\nPlease press any key to re-sort new tabel, or press Q key to leave from the application.")
            input()
            os.system('cls')

        with open("List.txt", "w") as file:
            for i in range(0, listLength - 1):
                    i = random.randint(0,999)
                    file.write(str(i)+" ")
    #randomList.append(random.randint(0,999))
        file.close()

        with open("List.txt") as file:
            wholeList = file.read()
        file.close()

        randomList = Convert(wholeList)

        for i in range(0, listLength - 1):
            randomList[i] = int(randomList[i])

        randomList1 = randomList.copy()
        randomList2 = randomList.copy()
        randomList3 = randomList.copy()


        toString(bubbleSort(randomList))
        toString(selectionSort(randomList1))
        toString(insertionSort(randomList2))
        toString(quickSort(randomList3))



        with open("List.txt", "w") as file:
            file.write(str(randomList) + "\n")
            file.close()

        print("\nPlease press any key to re-sort new tabels, or press Q key to leave from the application.")
        userInput = input()
        if userInput == "q" or userInput == "Q":
            print("Leaving from the application...")
            sys.exit()
        else:
            os.system('cls')
            continue

    except FileNotFoundError:
        print("File did not found!")
        print("\nPlease press any key to re-sort new tabel, or press Q key to leave from the application.")
        input()
        os.system('cls')
        continue

    except ValueError:
        print("Please enter only numbers.")
        print("\nPlease press any key to re-sort new tabels, or press Q key to leave from the application.")
        input()
        os.system('cls')
        continue


