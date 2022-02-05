#Relativly fast sorting algorithm, worst case: "O(n*log(n))"

def sort(list):
    #if statements splits the list, until it is one item, then merges lists together
    if len(list) >= 2 :
        mid = (len(list)//2)
        #print(mid, list)
        first = sort(list[:mid])
        second = sort(list[mid:])
        return merge(first, second)
    #If there is only one item in the list, the list is returned to be merged
    return list


    #Merges two lists together in increasing order
def merge(first, second):
    i = j = 0
    tmp = [None]*(len(first)+len(second))
    # Puts items in increasing order from both lists
    while (i <= len(first)-1) and (j <= len(second)-1):
        if first[i] < second[j] :
            tmp[i+j] = first[i]
            i += 1
        else :
            tmp[i+j] = second[j]
            j += 1
    #If there are any items left in either list, they will be filled in by these while-loops
    while i < len(first):
        tmp[i+j] = first[i]
        i += 1
    while j < len(second):
        tmp[i+j] = second[j]
        j += 1
    return tmp


#If you would like to test the algorithm, remove '#' from the lines beneath
#list = [3, 1, 7, 5, 4, 9]
#list = sort(list)
#print(list)
