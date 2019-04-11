array = [2, 4, 6 ]
def find_average(array):
    if len(array)< 1:
        return 0
    else:
        return sum(array)/len(array)
if __name__ == '__main__':
    find_average(array)
    ## BEst PRACTICES
    ##def find_average(array):
    ##return sum(array) / len(array) if array else 0
