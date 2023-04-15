#8.1a)
def counting_sort(arr):
    # find the range of input values
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    #initializing count array with zeros
    count = [0] * range_val
    
    #filling count array with frequency of input values
    for val in arr:
        count[val - min_val] += 1
        
    #modifying count array by adding previous counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    #creating the output array
    output = [0] * len(arr)
    
    #placing the input values in their sorted position
    for val in arr:
        output[count[val - min_val] - 1] = val
        count[val - min_val] -= 1
    
    return output

#sorting the given sequence and printing it
sequ = [9, 1, 6, 7, 6, 2, 1]
print("Before sorting:\n",sequ)
arr1 = counting_sort(sequ)
print("After sorting:\n",arr1)


