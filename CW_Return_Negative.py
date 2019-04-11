number = -9
def make_negative( number ):
    return number-number*2 if number > 0 else:number
if __name__ == "__main__":
    make_negative( number )

##BEST PRACTICE
#def make_negative( number ):
#    return -abs(number
