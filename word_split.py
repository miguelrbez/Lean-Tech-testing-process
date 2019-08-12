def WordSplit(strArr):
    # get two word sequence and dictionary of words
    sequence = strArr[0]
    dic = strArr[1].split(',')
    
    # finish flag
    flag = False
    
    # check for word 1 in dictionary, then check if word 2 is also in dictionary
    for i in range(len(sequence)):
        word1 = sequence[0:i]
        if word1 in dic:
            word2 = sequence[i::]
            if word2 in dic:
                # output solution
                solution = word1 + "," + word2
                flag = True
                break
    
    if flag:
        return(solution)
    else:
        return "not possible"
    

# keep this function call here  
print WordSplit(raw_input())