import random
import time



def difficulty_screen():
    print("/////////////////////////////////////////")
    while True:
        user_questions = input("How many questions would you like to complete?: ")
        try: 
            user_questions = int(user_questions)
            if user_questions > 0:
                break
            else: 
                print(f"'{user_questions}' is not a valid input. Please enter a positive integer.")
        except:
            print(f"'{user_questions}' is not a valid input. Please enter a positive integer.")

    print("There are three difficulties:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard :)")

    while True:
        user_difficulty = input("Please select your difficulty: ")
        try:
            user_difficulty = int(user_difficulty)
        except:
            print(f"'{user_difficulty}' is not a valid input. Please enter an integer input!")
            continue
        else:
            if user_difficulty<=3 and user_difficulty>=1: #Change this if added more conditions
                return [user_difficulty, user_questions] #Pass all conditions 
            else: 
                print(f"'{user_difficulty}' is not a valid input. Please enter an integer input within the ranges of 1 to 3.") #Change when add more question types
                continue



def run_questions(user_difficulty, user_questions):
    """
    run_question prompts the user with "x" questions. The question type is randomly generated (with bias) from the percentage calculations below.
    """
    user_score = 0
    incorrect_addition_subtraction_integer = 0 
    incorrect_multiplication_integer = 0
    incorrect_division_integer = 0

    print("/////////////////////////////////////////\nPlease only input numerical values.\nThe test will commence in 5 seconds.\n/////////////////////////////////////////")
    time.sleep(5)
    start_timer = time.time()

    for i in range(user_questions): 
        test_type = random.random()

        #This prompts the user with questions (Adjust this if added new question types)
        if test_type <= 0.33: #33% chance --> Run addition_subtraction_integer
            user_score_add, incorrect_addition_subtraction_integer_add = addition_subtraction_integer(user_difficulty)
            user_score += user_score_add
            incorrect_addition_subtraction_integer += incorrect_addition_subtraction_integer_add
        if  0.34 < test_type <= 0.66: #33% chance --> Run multiplication_integer
            user_score_add, incorrect_multiplication_integer_add = multiplication_integer(user_difficulty)
            user_score += user_score_add
            incorrect_multiplication_integer += incorrect_multiplication_integer_add
        if 0.67 < test_type <= 1: #33% chance --> Run division_integer
            user_score_add, incorrect_division_integer_add = division_integer(user_difficulty)
            user_score += user_score_add
            incorrect_division_integer += incorrect_division_integer_add

    #This readies the feedback to be returned.
    incorrect_list =[]
    if incorrect_addition_subtraction_integer >= incorrect_multiplication_integer and incorrect_addition_subtraction_integer >= incorrect_division_integer:
        incorrect_list.append("a.s")
        incorrect_list.append(incorrect_addition_subtraction_integer)
    if incorrect_multiplication_integer >= incorrect_division_integer and incorrect_multiplication_integer >= incorrect_addition_subtraction_integer:
        incorrect_list.append("m")
        incorrect_list.append(incorrect_multiplication_integer)
    if incorrect_division_integer >= incorrect_multiplication_integer and incorrect_division_integer >= incorrect_addition_subtraction_integer:
        incorrect_list.append("d")
        incorrect_list.append(incorrect_division_integer)
    

    stop_timer = time.time()
    elapsed_time = stop_timer - start_timer
    return user_score, elapsed_time, user_questions, incorrect_list



def addition_subtraction_integer(user_difficulty):
    """
    Perform either addition or subtraction on two integers depending on difficulty level:
    Easy --> (2) one digits numbers 
    Medium --> (2) two digits numbers 
    Hard :) --> (2) three digits numbers 
    """
    user_score_add = 0
    incorrect_addition_subtraction_integer = 0
    #Pick random either + or -
    if random.random() < 0.5:
        plus_minus = "+"
    else:
        plus_minus = "-"

    #Difficulty "Easy"
    if user_difficulty == 1: #Two, one digit numbers
        first_number = int(random.randint(1,9))
        second_number = int(random.randint(1,9))

        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {first_number} {plus_minus} {second_number} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                int(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if plus_minus == "+":
            answer = first_number + second_number
            if int(user_answer) == answer:
                user_score_add += 1 
                return user_score_add, incorrect_addition_subtraction_integer
            else: 
                incorrect_addition_subtraction_integer += 1
                return user_score_add, incorrect_addition_subtraction_integer
        else: 
            answer = first_number - second_number
            if int(user_answer) == answer:
                user_score_add += 1 
                return user_score_add, incorrect_addition_subtraction_integer
            else: 
                incorrect_addition_subtraction_integer += 1
                return user_score_add, incorrect_addition_subtraction_integer

    #Difficulty "Medium"
    if user_difficulty == 2: #Two, two digit numbers
        first_number = int(random.randint(10,99))
        second_number = int(random.randint(10,99))
        
        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {first_number} {plus_minus} {second_number} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                int(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if plus_minus == "+":
            answer = first_number + second_number
            if int(user_answer) == answer:
                user_score_add += 1 
                return user_score_add, incorrect_addition_subtraction_integer
            else: 
                incorrect_addition_subtraction_integer += 1
                return user_score_add, incorrect_addition_subtraction_integer
        else: 
            answer = first_number - second_number
            if int(user_answer) == answer:
                user_score_add += 1 
                return user_score_add , incorrect_addition_subtraction_integer
            else: 
                incorrect_addition_subtraction_integer += 1
                return user_score_add, incorrect_addition_subtraction_integer

    #Difficulty "Hard :)"
    if user_difficulty == 3: #Two, three digits numbers 
        first_number = int(random.randint(100,999))
        second_number = int(random.randint(100,999))
        
        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {first_number} {plus_minus} {second_number} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                int(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if plus_minus == "+": #Account for either a + or -
            answer = first_number + second_number 
            if int(user_answer) == answer:
                user_score_add += 1 
                return user_score_add, incorrect_addition_subtraction_integer
            else: 
                incorrect_addition_subtraction_integer += 1
                return user_score_add, incorrect_addition_subtraction_integer
        else: 
            answer = first_number - second_number
            if int(user_answer) == answer:
                user_score_add += 1 
                return user_score_add, incorrect_addition_subtraction_integer
            else: 
                incorrect_addition_subtraction_integer += 1
                return user_score_add, incorrect_addition_subtraction_integer



def multiplication_integer(user_difficulty):
    """
    Perform multiplication on two integers depending on the difficulty: 
    Easy --> (2) one digits numbers
    Medium --> (1) one digit, (1) two digit
    Hard :) --> (2) two digit  (value biased, only upto 50)
    """
    user_score_add = 0
    incorrect_multiplication_integer = 0 

    if user_difficulty == 1:
        first_number = random.randint(-9,9)
        second_number = random.randint(1,9)
        answer = first_number * second_number

        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {first_number} * {second_number} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                int(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if int(user_answer) == answer:
            user_score_add += 1
            return user_score_add, incorrect_multiplication_integer
        else:
            incorrect_multiplication_integer += 1
            return user_score_add, incorrect_multiplication_integer

    if user_difficulty == 2:
        first_number = random.randint(-9,9)
        second_number = random.randint(10,99)
        answer = first_number * second_number

        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {first_number} * {second_number} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                int(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if int(user_answer) == answer:
            user_score_add += 1
            return user_score_add, incorrect_multiplication_integer
        else:
            incorrect_multiplication_integer += 1
            return user_score_add, incorrect_multiplication_integer

    if user_difficulty == 3:
        first_number = random.randint(-10,50)
        second_number = random.randint(10,50)
        answer = first_number * second_number

        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {first_number} * {second_number} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                int(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if int(user_answer) == answer:
            user_score_add += 1
            return user_score_add, incorrect_multiplication_integer
        else:
            incorrect_multiplication_integer += 1 
            return user_score_add, incorrect_multiplication_integer

def division_integer(user_difficulty):
    """
    Perform division on an integer given another integer (single digit) depending on the difficulty:
    Easy --> Answer = (2) single digit
    Medium --> Answer = (1) single digit, (1) double digit (10 - 25)
    Hard :) --> Answer = (1) single digit, (1) double digit (26 - 50)
    """
    user_score_add = 0
    incorrect_division_integer = 0 
    #The method to calculate which number to be divided, is to find the expected answer first, then multiply them together to 
    #get the, "to_be_divided" value


    if user_difficulty == 1:
        divisor = random.randint(-9,9)
        calculate_to_be_divided = random.randint(1,9)
        to_be_divided = calculate_to_be_divided*divisor

        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {to_be_divided} / {divisor} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                int(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if int(user_answer) == calculate_to_be_divided:
            user_score_add += 1 
            return user_score_add, incorrect_division_integer
        else:
            incorrect_division_integer += 1
            return user_score_add, incorrect_division_integer

    if user_difficulty == 2:
        divisor = random.randint(-9,9)
        calculate_to_be_divided = random.randint(10,25)
        to_be_divided = calculate_to_be_divided*divisor

        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {to_be_divided} / {divisor} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                int(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break
        
        if int(user_answer) == calculate_to_be_divided:
            user_score_add += 1 
            return user_score_add, incorrect_division_integer
        else:
            incorrect_division_integer += 1
            return user_score_add, incorrect_division_integer

    if user_difficulty == 3:
        divisor = random.randint(-9,9)
        calculate_to_be_divided = random.randint(26,50)
        to_be_divided = calculate_to_be_divided*divisor

        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {to_be_divided} / {divisor} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                int(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if int(user_answer) == calculate_to_be_divided:
            user_score_add += 1 
            return user_score_add, incorrect_division_integer
        else:
            incorrect_division_integer += 1 
            return user_score_add, incorrect_division_integer


def addition_subtraction_decimal(user_difficulty): 
    """
    Perform addition on subtraction decimals depending on the difficulty: 
    Easy --> x.x += x.x
    Medium --> x.xx += x.xx
    Hard :) --> xx.xxx += xx.xxx
    """
    user_score = 0 
    incorrect_addition_subtraction_decimal = 0

    if user_difficulty == 1:
        pass
        # first_number_integer =
        # first_number_float = 
        # second_number_integer = 
        # second_number_float = 
    
    if user_difficulty == 2:
        pass

    if user_difficulty == 3:
        pass

def multiplication_decimal(): 
    """
    Perform multiplication on decimals depending on the difficulty:
    Easy --> x.x * integeer 
    Medium --> x.x * x.x
    Hard :) --> xx.x * xx.x (xx both numbers less than or equal to 15)
    """
    pass 

def division_decimal(): 
    """
    Perform divison on deciamls resulting in:
    Easy --> always give answer either no remainder or 0.5
    Medium --> always give answer of no remainder or 0.25, 0.5, 0.75
    Hard :) --> always give answer of no remainder or a multiple of 0.1
    """
    pass