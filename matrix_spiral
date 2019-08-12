def MatrixSpiral(strArr):
    row_size = len(strArr)
    column_size = len(strArr[0][1:-1].split(","))
    # print(row_size)
    output = []
    
    rs = 0
    cs = 0
    rf = row_size
    cf = column_size
    # print(cf)
    counter = 0
    r = 0
    c = -1
    
    flag = True
    # while counter < (row_size * column_size):
    while flag:
        # print(counter)
        # print(c, r)
        for i in range(cs, cf):
            c += 1
            # print(strArr[r][1:-1].split(",")[c])
            output.append(strArr[r][1:-1].split(",")[c].strip())
            counter += 1
            if counter >= row_size * column_size:
                flag = False
                break
        if not flag:
            break
        rs += 1
        # print(c, r)
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
        # print(c, r)
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
        # print(c, r)
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
        # print(c, r)
    
    str_output = ",".join(output)
    
    return str_output
    
# keep this function call here  
print MatrixSpiral(raw_input())
