data = [[45, 12],[55,21],[19, -2],[104, 20]]
def openOrSenior(data):
    finalized = []
    for person in data:
        if person[0] >= 55 and person[1] > 7:
            finalized.append("Senior")
        else:
            finalized.append("Open")
        person = person[+1]
    return(finalized)
if __name__ == '__main__':
    openOrSenior(data)
