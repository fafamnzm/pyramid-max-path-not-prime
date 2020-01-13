""" 
    In this file we find the maximum possible summation of path to the bottom
    where the bellow one is not a prime number
"""

#implementation of 
#Sieve of Eratosthenes
def primeFinder(num):
    boolPrimes=[True for i in range(num+1)]
    p = 2
    primeList = []
    #eliminates the multiplications
    #until we reache the sqrt of numb
    while(p*p <= num):
        if(boolPrimes[p] == True):    
            for i in range(p*p, num+1, p):
                boolPrimes[i] = False
        p += 1
    
    #appends those who are still True
    #which means they are a prime number
    for i in range(2, num+1):
        if boolPrimes[i]:
            primeList.append(i)
    return primeList


#converts the data which is a multi line string 
# into a list of lists 
# just because I prefer it this way ;) =)
def data_getter(data):
    lst = []
    for row in data.splitlines():
        lst.append(row.split())
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = int(lst[i][j])
    return lst


#the actual function which finds the desired value
def maxSum(pyram, m):
    # finds a prime list up to the maximum element
    # in the imput data 
    mxm = 0
    for i in range(len(pyram)):
        if mxm < max(pyram[i]):
            mxm = max(pyram[i])
    primeList = primeFinder(mxm)

    # eliminates the prime number at the bottom row
    # as we don't check them 
    # and we start from the line above it
    #it equals the prime numbers to zero 
    # so eliminates them from getting added
    # to the above element
    j = 0
    for i in pyram[m]:
        if i in primeList:
            pyram[m][j] = 0
            j += 1
        else:
            j+=1
    
    # it starts from bottom and from the second to the last line 
    # and it works its way up 
    # and adds those who are not primes
    for i in range(m-1, -1, -1): 
        for j in range(i+1):
            if (pyram[i+1][j] > pyram[i+1][j+1]) and pyram[i][j] not in primeList: 
                pyram[i][j] += pyram[i+1][j] 
            elif pyram[i][j] not in primeList: 
                pyram[i][j] += pyram[i+1][j+1] 
    # return the top element as it is the maximum sum 
    # with the given criteria
    return pyram[0][0] 

# set of test data to check it is working properly
testPyram = []
testPyram.append([1])
testPyram.append([8, 4])
testPyram.append([2, 6, 9])
testPyram.append([8, 5, 9, 3])


# actual given data in the test
data = """  215
            193 124
            117 237 442
            218 935 347 235
            320 804 522 417 345
            229 601 723 835 133 124
            248 202 277 433 207 263 257
            359 464 504 528 516 716 871 182
            461 441 426 656 863 560 380 171 923
            381 348 573 533 447 632 387 176 975 449
            223 711 445 645 245 543 931 532 937 541 444
            330 131 333 928 377 733 17 778 839 168 197 197
            131 171 522 137 217 224 291 413 528 520 227 229 928
            223 626 34 683 839 53 627 310 713 999 629 817 410 121
            924 622 911 233 325 139 721 218 253 223 107 233 230 124 233 """

# it getes the desired list type of the data
dataList = data_getter(data)
# m is where we should start 
# which is the index of the last row
# which is one less than the length
m = len(dataList)-1

# to test with the test data
print("the maximum sum in the test data is :")
print(maxSum(testPyram, 3))

# actual data analysis
print("the maximum sum in the actual data is :")
print(maxSum(dataList, m))
