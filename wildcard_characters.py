def WildcardCharacters(str):
    
    # split input in wncoding pattern and sequence
    strings = str.split()
    pattern = strings[0]
    sequence = strings[1]

    # list of numbers representing number of equal continuous characters in sequence. Encoding "+", "*" and "+{N}" to integers
    code = []

    # character current position in for loop
    i = 0

    # encode characters of pattern to new code variable
    for char in pattern:
        
        # encode "+" char. 1 single letter in sequence
        if char == "+":
            code.append(1)

        # encode "*" char
        elif char == "*":
            # check if "*" is not last character of pattern.If True, two possibilities: Regular ¨*" or "*" followed by {N}
            if i+1 != len(pattern):
                # "*" followed by {N}. N number of equal letters in sequence
                if pattern[i+1] == "{":
                    code.append(int(pattern[i+2]))
                # Regular "*". 3 equal letters in sequence
                else:
                    code.append(3)

            # Regular "*" is last character of pattern. 3 equal letters in sequence
            else:
                code.append(3)
        
        # increase position index of character in pattern
        i += 1    
    

    # check if sequence follows code encoding
    
    # initialize sequence position index
    ini = 0
    # flag of result. If True maintains, the sequence matches the code
    flag = True
    # check ig sequence has the correct number of characters given by code
    if sum(code) == len(sequence):
        # check if the amount of same continuous characters given by each number in code is satisfied
        # If not break loop and set flag to False
        for num in code:
            for char in sequence[ini:ini+num]:
                if char != sequence[ini]:
                    flag = False
                    break
                if not flag:
                    break
            if not flag:
                break
            ini += num
            # print(ini)
    else:
        flag = False
    
    if flag:
        return "true"
    else:
        return "false"
    
# keep this function call here  
print WildcardCharacters(raw_input())