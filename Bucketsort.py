import math
import InsertionSort

def sort(lst):
    least = min(lst)
    biggest = max(lst)+1
    n = 5

    #Finds range to divide buckets into equal ranges
    rng = (biggest-least) / n
    tmp = []

    #Creates empty buckets
    for i in range(n):
        tmp.append([])

    #Places each element in correct bucket
    for e in lst:
        slot = rng
        while e > slot:
            slot += rng
        bucket = math.floor(slot/rng)-1
        tmp[bucket].append(e)

    #Resets list to append items increasing order
    lst = []
    for bucket in tmp:
        #Sort buckets with insertion sort
        bucket = InsertionSort.sort(bucket)
        #Append all items of sorted buckets into list
        for element in bucket:
            lst.append(element)
    #return sorted list
    return lst

lst = [1,3,4,56,7,8,8,5,3,21,23]
lst = sort(lst)
print(lst)
