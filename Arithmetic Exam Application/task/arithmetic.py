# write your code here
import random


def choices():
    print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")
    choice_num = int(input())
    if choice_num == 1:
        task_generator()
    elif choice_num == 2:
        square()
    else:
        print('Incorrect format.')


def task_generator():
    i = 0
    score = 0
    while i < 5:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        list_operations = ['+', '*', "-"]
        ope = random.choice(list_operations)
        if ope == '+':
            print(str(num1) + ' + ' + str(num2))
            right_answer = num1 + num2
        elif ope == '-':
            print(str(num1) + ' - ' + str(num2))
            right_answer = num1 - num2
        elif ope == '*':
            print(str(num1) + ' * ' + str(num2))
            right_answer = num1 * num2

        repeat = True
        repeatCount = 0
        while repeat:
            try:
                ans = int(input())
                if ans == right_answer:
                    print("Right!")
                    score += 1
                    repeat = False
                else:
                    print("Wrong!")
                    repeat = False
            except ValueError:
                print("Incorrect format.")
                repeatCount += 1
                if repeatCount == 5:
                    repeat = False
        i += 1
    print("Your mark is " + str(score) + "/5")
    ans = input("Would you like to save the result? Enter yes or no.")
    if ans in ["yes", "y", "YES", "Yes"]:
        level_description = "simple operations with numbers 2-9"
        level = 1
        make_file(score, level, level_description)
    else:
        exit()


def square():
    i = 0
    score = 0
    while i < 5:
        num = random.randint(11, 29)
        print(num)
        answer = num ** 2
        #print(answer)
        repeat = True
        repeatCount = 0
        while repeat:
            try:
                ans = int(input())
                if ans == answer:
                    print("Right!")
                    score += 1
                    repeat = False
                else:
                    print("Wrong!")
                    repeat = False
            except ValueError:
                print("Incorrect format.")
                repeatCount += 1
                if repeatCount == 5:
                    repeat = False
        i += 1
    print("Your mark is " + str(score) + "/5")
    ans = input("Would you like to save the result? Enter yes or no.")
    if ans in ["yes", "y", "YES", "Yes"]:
        level_description = "integral squares of 11-29"
        level = 2
        make_file(score, level, level_description)
    else:
        exit()


def make_file(score, level, level_description):
    archivo = open("results.txt", "a")
    name = input('What is your name?')
    archivo.write(f"{name}: {score}/5 in level {level} ({level_description}).\n")
    print(f"The results are saved in \"results.txt\".")
    archivo.close()


if __name__ == '__main__':
    choices()



