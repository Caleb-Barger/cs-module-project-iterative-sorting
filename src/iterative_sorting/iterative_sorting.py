def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # store a current boundry 
        cur_index = i

        # set the smallest value & it's location
        smallest_value = arr[cur_index]
        smallest_index = cur_index

        # iterate through the numbers that still need some sorting
        for unsorted_index in range(cur_index, len(arr)):
            
            # if a smaller value is found
            if arr[unsorted_index] < smallest_index:

                # update the smallest value & smallest index 
                # to current unsorted index
                smallest_value = arr[unsorted_index]
                smallest_index = unsorted_index
        
        # swap the bigger value with the smaller one
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr

def bubble_sort(arr):
    # iterate through each item 
    for i in range(len(arr) - 1):
        # for index that is not the last element (already sorted)
        for j in range(0, len(arr)-i-1):
            # if the current value is greator
            if arr[j] > arr[j+1]:
                # swap places
                arr[j], arr[j+1] = arr[j+1], arr[j]
         
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
