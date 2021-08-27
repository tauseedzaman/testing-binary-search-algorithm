import time
import random

# In native search we compare the target item with earch element of the list 
def native_search(l,tartget):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# in binary search Algorithm all we do is we find's the mid point in compare with the target item tobe searched 
# if the item maches the mid point the game is over :). other wise at Algorithm will find out that does the element
# is greater them the mid point if yes then the next mid array is considered as the list and the Algorithm again
# find's the mid point and compare with the target item and son on till the target item is found in the list
def binary_search(l,target, low=None , high = None):
    if low is None:
        low=0
    
    if high is None:
        high= (len(l)-1)
    
    if high < low:
        return -1

    midPoint = (low+high) // 2
    if midPoint == target:
        return midPoint

    elif target < midPoint:
        return binary_search(l,target, low, midPoint-1)
    else:
        return binary_search(l,target, midPoint+1, high)


if __name__ == '__main__':

    length = 10000 #length of list is 10000 so that we can clearly see how binary search Algorithm is best then native search
    sorted_list =set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    #test native search Algorithm
    start = time.time()
    for target in sorted_list:
        native_search(sorted_list,target)
    end= time.time()
    print(f"Total time taken by native search function {(start - end)/length} seconds")

    #test binary search Algorithm
    start= time.time()
    for target in sorted_list:
        binary_search(sorted_list,target)
    end = time.time()
    print(f"Total time taken by binary serch algurithem is {(start - end)/length} seconds")

