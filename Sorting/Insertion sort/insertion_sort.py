"""
Insertion Sort: sorting in increasing order
"""
def insertionSort(a: list) -> list:
    """
    Function of insertion sort sorting numbers in ascending order
    """

	# for loop generated the indexes from 1 to length of array
    for j in range(1,len(a)):
        key= a[j]             
        i= j- 1

	    # comparing the key with subarray a[0 - j-1] and moving the elements one step forward if key is less
	    # than the element in subarray

        while i > -1 and key < a[i]: 
            a[i+1]= a[i]      
            i= i- 1  

        # assigning key to proper location	         
        a[i+1]= key           
    return a   

def main():
    x=insertionSort([5,2,4,6,1,3])
    print(x)    

if __name__ == '__main__':
    main()


