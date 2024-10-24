def bubble_sort(unsorted): # Creating a function that runs bubble sort
    for i in range(1,len(unsorted)+1): # Loop it for the length of the list given
        swaps = 0 # It will be a new pass so swaps resets
        for j in range(len(unsorted)-i): # We don't need to check the end elements as we know they are complete, so the length of list - i
            if unsorted[j] > unsorted[j+1]: # Checking if the value before is greater than the one after
                holding = unsorted[j]
                unsorted[j] = unsorted[j+1] # If it is then we swap them
                unsorted[j+1] = holding
                swaps += 1 # We did a swap so increase swaps by 1
        if swaps == 0: # Break the for loop if no swaps are completed, since list is sorted
            break
    return unsorted

example = [36, 730, 97, 314, 596] # Running the bubble sort function
sorted = bubble_sort(example)
print (sorted)

print ('\n')

def quick_sort(unsorted): # Making a function for the quick sort algorithm
    if len(unsorted) <= 1: # If the list is less than 1 or equal to 1, we know it is sorted
        return unsorted
    else:
        pivot = unsorted[0]
        below_pivot = [x for x in unsorted[1:] if x <= pivot] # Spliting into two lists, above and below the pivot
        above_pivot = [x for x in unsorted[1:] if x > pivot]
        return quick_sort(below_pivot) + [pivot] + quick_sort(above_pivot) # Repeat with the new lists until sorted

example = [36, 730, 97, 314, 596]
sorted = quick_sort(example) # Running the quick sort
print (sorted)

print ('\n')

def insertion_sort(unsorted): # Creating a function for the insertion sort
    for i in range(1, len(unsorted)): # Run through the list
        key = unsorted[i]
        j = i - 1
        while j >= 0 and unsorted[j] > key: # Checking for location to place the key
            unsorted[j + 1] = unsorted[j]
            j -= 1
        unsorted[j + 1] = key # Once found we slot the key into that location
    return unsorted

example = [36, 730, 97, 314, 596] # Running the insertion sort
sorted = insertion_sort(example)
print (sorted) 

print ('\n')

example = [36, 730, 97, 314, 596] # Using the sort function
sorted = example.sort() # Empty brackets will place the list in ascending order
print (sorted)

print ('\n')

def linear_search(example, element): # Function for the linear search
    for i in range(len(example)): # Run through every value in the list
        if example[i] == element: # Checking if that value is the one we are looking for 
            return i # If it is, end the function and return the index
    return -1  # If not found, return -1

example = [14, 12, 15, 11, 22]
location = linear_search(example, 14) # Running the linear search function
print ('The index of 14 in the list is:', location)

print ('\n')

def binary_search(example, element): # Function for the binary search algorithm
    low = 0 # Lowest index in the list
    high = len(example) - 1 # Highest index in the list

    while low <= high:
        mid = (low + high) // 2 # Finding the index of the mid point in the list
        if example[mid] == element: # Checking if we have found the element in the list
            return mid # Found the element's index, returning it
        elif example[mid] < element: # If we haven't found it, are we gonna look at above it or under it
            low = mid + 1 # Now we compare the lower half of the list
        else:
            high = mid - 1 # Now we compare the upper half of the list

    return -1

example = [10, 11, 12, 14, 22]
location = binary_search(example, 14) # Running the binary search function
print ('The index of 14 in the list is:', location)

print ('\n')

example = [10, 11, 12, 14, 22]
location = example.index(14) # Using the index function
print ('The index of 14 in the list is:', location)


print ('\n')

# Testing the speeds of all the algorithms:

import time

def bubble_sort(unsorted):
    for i in range(1,len(unsorted)+1):
        swaps = 0
        for j in range(len(unsorted)-i):
            if unsorted[j] > unsorted[j+1]:
                holding = unsorted[j]
                unsorted[j] = unsorted[j+1]
                unsorted[j+1] = holding
                swaps += 1
        if swaps == 0:
            break
    return unsorted


example = [36, 730, 97, 314, 596]
start = time.time() # Time before the functions begin
for i in range(10000): # Repeat the algorithms 10,000 times
    sorted = bubble_sort(example)
end = time.time() # Time once the functions have finished
timing = end-start # Get the time it takes to complete 10,000 functions
timing *= 100000 # Getting average speed of the functions in nano seconds
timing = int(timing)
print ('Time to output bubble sort:',str(timing) + 'ns')

print ('\n')

def quick_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted
    else:
        pivot = unsorted[0]
        below_pivot = [x for x in unsorted[1:] if x <= pivot]
        above_pivot = [x for x in unsorted[1:] if x > pivot]
        return quick_sort(below_pivot) + [pivot] + quick_sort(above_pivot)

example = [36, 730, 97, 314, 596]
start = time.time()
for i in range(10000):
    sorted = quick_sort(example)
end = time.time()
timing = end-start
timing *= 100000
timing = int(timing)
print ('Time to output quick sort:',str(timing) + 'ns')

print ('\n')

def insertion_sort(unsorted):
    for i in range(1, len(unsorted)):
        key = unsorted[i]
        j = i - 1
        while j >= 0 and unsorted[j] > key:
            unsorted[j + 1] = unsorted[j]
            j -= 1
        unsorted[j + 1] = key
    return unsorted

example = [36, 730, 97, 314, 596]
start = time.time()
for i in range(10000):
    sorted = insertion_sort(example)
end = time.time()
timing = end-start
timing *= 100000
timing = int(timing)
print ('Time to output insertion sort:',str(timing) + 'ns')

print ('\n')

example = [36, 730, 97, 314, 596]
start = time.time()
for i in range(10000):
    sorted = example.sort()
end = time.time()
timing = end-start
timing *= 100000
timing = int(timing)
print ('Time to output sort function:',str(timing) + 'ns')

print ('\n')

def linear_search(example, element):
    for i in range(len(example)):
        if example[i] == element:
            return i 
    return -1  

example = [10, 11, 12, 14, 22]
start = time.time()
for i in range(10000):
    location = linear_search(example, 14)
end = time.time()
timing = end-start
timing *= 100000
timing = int(timing)
print ('Time to output linear search:',str(timing) + 'ns')

print ('\n')

def binary_search(example, element):
    low = 0
    high = len(example) - 1

    while low <= high:
        mid = (low + high) // 2
        if example[mid] == element:
            return mid 
        elif example[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    return -1

example = [10, 11, 12, 14, 22]
start = time.time()
for i in range(10000):
    location = binary_search(example, 14)
end = time.time()
timing = end-start
timing *= 100000
timing = int(timing)
print ('Time to output binary search:',str(timing) + 'ns')

print ('\n')

example = [10, 11, 12, 14, 22]
start = time.time()
for i in range(10000):
    location = example.index(14)
end = time.time()
timing = end-start
timing *= 100000
timing = int(timing)
print ('Time to output for the index function:',str(timing) + 'ns')
