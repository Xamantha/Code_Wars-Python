inputStr = "abracadabra"

def getCount(inputStr):
    vowels = list("aeiou")
    answer = [i for i in list(inputStr) if i in vowels]
    return(len(answer))
if __name__ == "__main__":
    getCount(inputStr)
## BEST PRACTICES
## def getCount(inputStr):
##     return sum(1 for let in inputStr if let in "aeiouAEIOU")
