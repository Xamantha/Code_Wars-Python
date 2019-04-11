seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
def find_it(seq):
    for i in seq:
        dupeCheck = seq.count(i)
        if dupeCheck % 2 != 0:
            answer = i
    return(answer)
if __name__ == '__main__':
    find_it(seq)
##BEST PRACTICES ####
##def find_it(seq):
##    for i in seq:
##        if seq.count(i)%2!=0:
##            return i
