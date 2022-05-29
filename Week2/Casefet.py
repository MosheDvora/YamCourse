def check_code (user_code):
    counte_digite = 0
    if  user_code[0] == "4":
        counte_digite += 1
    if  user_code[1] == "8":
        counte_digite +=1
    if  user_code[2] == "1":
        counte_digite += 1
    if  user_code[3] == "2":
        counte_digite += 1
    return counte_digite




user_code = input("Enter a 4 digit code :")

print( "you open the safe bos" if
       (check_code(user_code)) == 4 else " only " +  str(check_code(user_code)) + " digit was right")

