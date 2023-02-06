
number_iterations = 24
modulo = 24

def answer():
    answer = []
    for i in range(number_iterations):
        answer.append((i**2) - (i*6) + 8)
    return answer

def modulo_24(answer):
    my_dict = {}
    for i in range(number_iterations):
        #check to see if modulo == 0, if it does, add it to the hashtable
        if answer[i] % modulo == 0:
            my_dict[str(i)] = 0
    return my_dict


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(answer())
    print(modulo_24(answer()))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
