import random


no = [1,2,3,4,5,6,7,8,9,0]

special_case = ['!','@','#','$']

def generatePassword(data,max):
    numeric_value_password = []
    length_userinput = len(data)
    special_word = random.choice(special_case)
    if length_userinput < max:
        remaining_length = max - (length_userinput + 1) 
        for i in range(0,remaining_length):
            numeric_value_password.append(random.choice(no))
    elif length_userinput == max:
        remaining_length = 3 
        for i in range(0,remaining_length):
            numeric_value_password.append(random.choice(no))
    else:
        remaining_length = 2 
        for i in range(0,remaining_length):
            numeric_value_password.append(random.choice(no))

    demo_password = generateExtraWord(data,numeric_value_password,special_word)
    final_password = [random.choice(demo_password) for i in range(1,max)]
    
    return ''.join(map(str,final_password))


def generateExtraWord(word,numeric,special):
    word_phase = [i.lower() for i in word]
    capital_word = [random.choice(word_phase).upper() for i in range(0,len(word_phase)//2)]
    for i in capital_word:
        try:
            word_phase.remove(i.lower())
        except:
            continue

    temp_password = capital_word + list(map(str,special)) + word_phase + list(map(str,numeric))
    return temp_password


if __name__ == "__main__":
    user_input = input('Enter The word that u want to create password without space : ')
    password_size = int(input('Enter the max digit password u want : '))
    password_generted = generatePassword(user_input,password_size)
    print(f'Your password is ------ {password_generted}')

