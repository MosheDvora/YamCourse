import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s-%(lineno)d - %(funcName)s|%(message)s')

def get_code():
    return input("Please 4 digits code :")

def check_code(user_ins_code):
    if  user_ins_code == "4812":
        return True
    else:
        return False

def check_accuracy(code):
    counter = 0
    num_of_accuracy = 0
    checked_number = []
    while counter < 4:
        if code[counter] not in checked_number:
            if code[counter] in "4812":
                num_of_accuracy += 1
                checked_number.append(code[counter])
        counter += 1
    return  num_of_accuracy

def print_result(safe_state, number_of_success):
    if  safe_state:
        print("You open the safe ")
    else:
        print("It's Not the Code")
        print(f"You successed only {number_of_success}")


user_try = 3
iscode_success = ""
number_of_success = 0
# Get the first code form the user


#give the user 4 time to try
while user_try > 0:
    user_code = get_code()
    iscode_success =  check_code(user_code)
    if iscode_success:
        user_try = 0
    else:
            print(f"You success only: {check_accuracy(user_code)}")
    user_try -= 1

print_result(iscode_success, number_of_success)




