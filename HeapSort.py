
#Main method, returns a list sorted in a minHeap format. Utilize pop(list) function to get correct output
def sort(list):
    for i in range(len(list)):
        list = buildHeap(list, i)
    return list



def buildHeap(list, i):
    #finding necessary index's
    n = len(list)
    min = i
    left = i*2 + 1
    right = left + 1
    #Finding new min value, if exists
    if (left < n) and (list[left] < list[i]):
        min = left
    if (right < n) and (list[right] < list[i]):
        min = right
    #If a swap is needed
    if min != i:
        list[min], list[i] = list[i], list[min]
        #Changes the affected tree
        buildHeap(list, min)
    return list

#method to remove items in correct order, and fix heap on output
def pop(list):
    item = list.pop(0)
    buildHeap(list, 0)
    return item



#If you would like to test the algorithm, you can run this file. Otherwise just utilize its methods
list = [3, 1, 7, 5, 9, 4, 8, 13, 10, 15]
list = sort(list)
while len(list) > 0:
    print(pop(list))
print(list)
