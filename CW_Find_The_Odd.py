##to find out which one of the given numbers differs from the others
numbers = "2 4 7 8 10"
def iq_test(numbers):
        for i in numbers.split():
            newArray = [int(i) for i in numbers.split()]
            even = [newArray.index(i) for i in newArray if i %2==0]
            odd = [newArray.index(i) for i in newArray if i %2!=0]
        combined = even+odd
        for i in combined:
             if i not in newArray:
                 print(newArray.index(newArray[i]))
        print(newArray)
        print(even)
        print(odd)
        #print(combined)
if __name__ == "__main__":
    iq_test(numbers)
