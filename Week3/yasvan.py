import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s-%(lineno)d - %(funcName)s|%(message)s')


# kolz function: if even div by 2 if odd multiply by 3 and add 1
def kolz(num):
    counter = 0
    while num > 1:
        if num % 2 == 0:
            num /= 2
            counter += 1
        else:
            num = 3 * num + 1
            counter += 1
    return counter


num = 1
kolz_list = []
while num <= 1000:
    kolz_list.append(kolz(num))
    num += 1
print(kolz_list)
print(max(kolz_list))
