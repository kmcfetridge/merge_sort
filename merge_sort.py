##Kenneth McFetridge
##5/26/2014
##kmcfetridge89@gmail.com
##any feedback is appreciated

count = 0

def merge_sort( list ):
    ## declare variables
	length = len(list)
    A = []
    B = []
    global count
	
	## split array "list" in half if it is even, if it is odd splits in half plus one into array A and and the rest into B
    if length > 1:
        for i in range(len(list)):
            if i < (length / 2):
                A.append(list[i])
            else:
                B.append(list[i])
		## using recursion to continue spliting the array into smaller chunks of size 2 or 1
        A = merge_sort(A)
        B = merge_sort(B)
		## take A and B and combines them back into a single array in order from least to greatest
        j = 0
        k = 0
        for i in range(len(list)):
            if k < len(B) and j < len(A):
                if A[j] < B[k]:
                    list[i] = A[j]
                    j = j + 1
                else:
                    list[i] = B[k]
                    k = k + 1
                    count = count + (len(A) - j)
            else:
                if j < len(A):
                    list[i] = A[j]
                    j = j + 1
                else:
                    list[i] = B[k]
                    k = k + 1
           
    return (list)
 
## opens a file, scans file as a string, converts string into an array of integers 
f = open('IntegerArray.txt', 'r')
d = f.readlines()
d = [int(x.strip())for x in d]
f.close() 
f.close()

print(merge_sort(d))
print(count)
