#Fast algorithm with few items, slow and bigger data stets
#Worst case + avg: O(n^2), best case O(n)

def sort(list):
    for i in range(len(list)) :
        j = i
        while (j > 0) and (list[j-1] > list[j]) :
            list[j-1], list[j] = list[j], list[j-1]
            j -= 1
    return list


#If you would like to test the algorithm, remove '#' from the lines beneath
#list = [3, 1, 7, 5, 9, 4]
#list = sort(list)
#print(list)
