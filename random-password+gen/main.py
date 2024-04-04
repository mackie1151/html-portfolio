import random
from data import upper_case, lower_case, num, sym

print('Welcome to the random password generator!')


def up_case():
    upper_input = int(input('Number of upper case letters: '))
    return random.sample(upper_case, upper_input)


def lo_case():
    lower_input = int(input('Number of lower case letters: '))
    return random.sample(lower_case, lower_input)


def numbers():
    num_input = int(input('Number of digits: '))
    ran_nums = random.sample(num, num_input)
    for i in ran_nums:
        return str(i)


def symbols():
    sym_input = int(input('Number of symbols: '))
    return random.sample(sym, sym_input)


up_str = ''.join(up_case())
lo_str = ''.join(lo_case())
num_str = numbers()
sym_str = ''.join(symbols())


gen_password = up_str + lo_str + num_str + sym_str

gen_password_list = list(gen_password)
random.shuffle(gen_password_list)
final_password = ''.join(gen_password_list)
print(final_password)




