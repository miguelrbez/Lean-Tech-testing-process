def MatrixSpiral(strArr):
    # get size of matrix
    row_size = len(strArr)
    column_size = len(strArr[0][1:-1].split(","))
    
    # list of numbers in spiral order
    output = []
    
    # rs: row start, cs: column start, rf: row final, cf: column final
    rs = 0
    cs = 0
    rf = row_size
    cf = column_size
    
    # counter: adds up untill reaching matrix number of elements
    counter = 0
    
    # r: current position row, c: current position column (starts at -1 due to sum start later in code)
    r = 0
    c = -1
    
    # while loop finish flag
    flag = True
    
    # loop of four movements: right, downwards, left, upwards
    while flag:
        # for loop for right movement
        for i in range(cs, cf):
            c += 1
            output.append(strArr[r][1:-1].split(",")[c].strip())
            counter += 1
            if counter >= row_size * column_size:
                flag = False
                break
        if not flag:
            break
        rs += 1
        
        # for loop for downwards movement
        for i in range(rs, rf):
            r += 1
            # print(strArr[r][1:-1].split(",")[c])
            # print(i)
            output.append(strArr[r][1:-1].split(",")[c].strip())
            counter += 1
        if counter >= row_size * column_size:
                flag = False
                break
        if not flag:
            break
        cf -= 1

        # for loop for left movement
        for i in reversed(range(cs, cf)):
            c -= 1
            # print(strArr[r][1:-1].split(",")[c])
            output.append(strArr[r][1:-1].split(",")[c].strip())
            counter += 1
        if counter >= row_size * column_size:
                flag = False
                break
        if not flag:
            break
        rf -= 1

        # for loop for upwards movement
        for i in reversed(range(rs, rf)):
            r -= 1
            # print(strArr[r][1:-1].split(",")[c])
            # print(i)
            output.append(strArr[r][1:-1].split(",")[c].strip())
            counter += 1
        if counter >= row_size * column_size:
                flag = False
                break
        if not flag:
            break
        cs += 1
    

    # string output
    str_output = ",".join(output)
    
    return str_output
    
# keep this function call here  
print MatrixSpiral(raw_input())