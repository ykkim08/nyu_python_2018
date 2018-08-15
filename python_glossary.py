# Read csv file into a dictionary

import csv, random, sys

def read(filename):
    out_dict = {}
    with open(filename, newline = '') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        out_dict = dict(reader)
    return out_dict

# Select Random sample of dictionary
def random_dictionary(sample_dic, num_items):
    random_dic = dict(random.sample(sample_dic.items(), num_items))
    return random_dic

# Print key of dictionary
def print_key(sample_dic):
    maxline = max(map(len, sample_dic))
    printmax = maxline*'*'
    print(printmax)
    for key in sample_dic.keys():
        print(key)
    print(printmax)

# Check valid integer input
def check_integer_input(message):
    while True:
        try:
            userinput = int(input(message))
        except ValueError:
            print("You entered non integer. Try again!")
            continue
        else:
            if userinput >= 2 and userinput <= 100 :
                return userinput
                break
            else:
                print("Wrong number. Choose a number between 2 and 100")
                continue

# Exit and compute stats
def exit_stats (correct, total):
    print('\nYou answered {} terms correctly out of {} '.format(correct, total))
    print("So, your score is {}. {}% correct!".format(correct*10, 100*correct/total))
    print("Good Bye!")


# Main program
def main():
    # python glossary
    python_glossary = read('python_glossary.csv')


    num_question = 1
    right = 0
    wrong = 0

    # Print welcome screen
    print('-------------------------------------------------------------------')
    print('Welcome to Python Glossary Game!')
    print('The screen will diplay a definition or description of a term ')
    print("from YK's Python Glossary. ")
    print('Among the terms shown in the screen, select the most appropriate one')
    print('If your answer is correct, you will receive 10 points. ')
    print('If your answer is incorrect, you will receve 0 point.')
    print('-------------------------------------------------------------------')

    message = "How many terms do you want to play? Choose a number between 2 and 100: "

    num_terms = check_integer_input(message)

    # Select sample questions
    num_terms = int(num_terms)
    random_question = random_dictionary(python_glossary, num_terms)
    print('You selected the following {} Python terms'.format(num_terms))
    print_key(random_question)


    for key, value in random_question.items():
        print('\nQuestion {}:'.format(num_question) + '"' + value + '"')
        answer = input("What is the Python term? (Enter 'q' if you want to exit the game): ")

        if answer == 'q':
            exit_stats (right, num_terms)
            sys.exit(0)
        elif answer == key:
            right = right + 1
        else:
            right = right
        num_question = num_question + 1

    exit_stats (right, num_terms)


# main()
if __name__ == '__main__':
    main()
