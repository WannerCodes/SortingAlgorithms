#Simple sorting algoritm, but slow.

def sort(list):
    n = len(list)
    for i in range(n-1):
        for j in range(n-i-1):
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]



#If you would like to test the algorithm, remove '#' from the lines beneath
#list = [1, 3, 6, 2, 4]
#sort(list)
#for e in range(len(list)):
    #print(list[e])
