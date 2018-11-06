
integers = [160, 3, 1719, 19, 11, 13, -21]

def find_outlier(integers):
    even = []                        #evens array
    odd = []                         #odds array
    answer = []                      #Stores answer in variable to return
    for checking in integers:        #Loop through an array,
        if checking % 2 == 0:        #Figure out if odd or even
            even.insert(0, checking) #Add to seperate array.
        else:
            odd.insert(0, checking)  #Add to seperate array.
    if len(even) > len(odd):         #If more odds than even "even is outlier"
        answer = odd[0]              #adds single item in array to answer variable
    else:
        answer = even[0]             #adds single item in array to answer variable
    return answer                    #returns answer variable to the function.

if __name__ == '__main__':
    find_outlier(integers)
