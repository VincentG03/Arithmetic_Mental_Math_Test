import random
import time
import decimal as dec
import fractions


def difficulty_screen():
    print("/////////////////////////////////////////")
    valid_number_of_questions = False
    while valid_number_of_questions == False:
        user_questions = input("How many questions would you like to complete?: ")

        #Verifying valid user input.
        try:
            user_questions = int(user_questions)
        except ValueError:
            print(f"'{user_questions}' is not a valid input. Please enter a positive integer.")
        else: 
            valid_number_of_questions = True 

    if user_questions == 0: #TO BE ADDED AFTER GUI 
        print("going to add an easter egg here later ")
        exit()

    print("There are three difficulties:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    valid_user_difficulty = False
    while valid_user_difficulty == False:
        user_difficulty = input("Please select your difficulty: ")
        try:
            user_difficulty = int(user_difficulty)
        except ValueError:
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

    #Update this when adding new question types 
    incorrect_addition_subtraction_integer_total = 0 
    incorrect_multiplication_integer_total = 0
    incorrect_division_integer_total = 0
    incorrect_addition_subtraction_decimal_total = 0
    incorrect_multiplication_decimal_total = 0 
    incorrect_division_decimal_total = 0 

    print("/////////////////////////////////////////\nPlease only input numerical values.\nThe test will commence in 3 seconds.\n/////////////////////////////////////////")
    time.sleep(3)
    start_timer = time.time()

    for i in range(user_questions): 
        test_type = random.random()
        test_type = 0.9

        #This prompts the user with questions (Adjust this if added new question types)
        if test_type <= 0.1666: #Run addition_subtraction_integer
            user_score_add, incorrect_addition_subtraction_integer_add = addition_subtraction_integer(user_difficulty)
            user_score += user_score_add
            incorrect_addition_subtraction_integer_total += incorrect_addition_subtraction_integer_add
        elif  0.1666 < test_type <= 0.3333: #Run multiplication_integer
            user_score_add, incorrect_multiplication_integer_add = multiplication_integer(user_difficulty)
            user_score += user_score_add
            incorrect_multiplication_integer_total += incorrect_multiplication_integer_add
        elif 0.33333 < test_type <= 0.49999: #Run division_integer
            user_score_add, incorrect_division_integer_add = division_integer(user_difficulty)
            user_score += user_score_add
            incorrect_division_integer_total += incorrect_division_integer_add
        elif 0.49999 < test_type <=0.6666: #Run addition_subtraction_decimal
            user_score_add, incorrect_addition_subtraction_decimal_add = addition_subtraction_decimal(user_difficulty)
            user_score += user_score_add
            incorrect_addition_subtraction_decimal_total += incorrect_addition_subtraction_decimal_add
        elif 0.6666 < test_type <= 0.83333: #Run multiplication_decimal
            user_score_add, incorrect_multiplication_decimal_add = multiplication_decimal(user_difficulty)
            user_score += user_score_add
            incorrect_multiplication_decimal_total += incorrect_multiplication_decimal_add
        else: #Run division_decimal 
            print('runngin div dec ')
            user_score_add, incorrect_division_decimal_add = division_decimal(user_difficulty)
            user_score += user_score_add
            incorrect_division_decimal_total += incorrect_division_decimal_add



    #This readies the feedback to be returned (if any)
    incorrect_list =[]
    if incorrect_addition_subtraction_integer_total != 0:
        incorrect_list.append("integer addition subtraction")
        incorrect_list.append(incorrect_addition_subtraction_integer_total)

    if incorrect_multiplication_integer_total != 0:
        incorrect_list.append("integer multiplication")
        incorrect_list.append(incorrect_multiplication_integer_total)

    if incorrect_division_integer_total != 0:
        incorrect_list.append("integer division")
        incorrect_list.append(incorrect_division_integer_total)

    if incorrect_addition_subtraction_decimal_total != 0:
        incorrect_list.append("decimal addition subtraction")
        incorrect_list.append(incorrect_addition_subtraction_decimal_total)

    if incorrect_multiplication_decimal_total != 0: 
        incorrect_list.append("decimal multiplication")
        incorrect_list.append(incorrect_multiplication_decimal_total)

    if incorrect_division_decimal_total != 0: 
        incorrect_list.append("decimal division")
        incorrect_list.append(incorrect_division_decimal_total)
   
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
            user_answer = input(f"Compute: {first_number} × {second_number} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
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
            user_answer = input(f"Compute: {first_number} × {second_number} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
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
            user_answer = input(f"Compute: {first_number} × {second_number} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
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
    incorrect_division_integer_add = 0 
    #The method to calculate which number to be divided, is to find the expected answer first, then multiply them together to 
    #get the, "to_be_divided" value

    if user_difficulty == 1:
        pos_neg = random.random()
        if pos_neg > 0.5:
            divisor = random.randint(1,9) * (-1)
        else: 
            divisor = random.randint(1,9)

        calculate_to_be_divided = random.randint(1,9)
        to_be_divided = calculate_to_be_divided*divisor

        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {to_be_divided} ÷ {divisor} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
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
            return user_score_add, incorrect_division_integer_add
        else:
            incorrect_division_integer_add += 1
            return user_score_add, incorrect_division_integer_add


    if user_difficulty == 2:
        pos_neg = random.random()
        if pos_neg > 0.5:
            divisor = random.randint(1,9) * (-1)
        else: 
            divisor = random.randint(1,9)
        calculate_to_be_divided = random.randint(10,25)
        to_be_divided = calculate_to_be_divided*divisor

        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {to_be_divided} ÷ {divisor} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
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
            return user_score_add, incorrect_division_integer_add
        else:
            incorrect_division_integer_add += 1
            return user_score_add, incorrect_division_integer_add


    if user_difficulty == 3:
        pos_neg = random.random()
        if pos_neg > 0.5:
            divisor = random.randint(5,19) * (-1)
        else: 
            divisor = random.randint(5,19)

        calculate_to_be_divided = random.randint(10,19)
        to_be_divided = calculate_to_be_divided*divisor

        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {to_be_divided} ÷ {divisor} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
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
            return user_score_add, incorrect_division_integer_add
        else:
            incorrect_division_integer_add += 1 
            return user_score_add, incorrect_division_integer_add


def addition_subtraction_decimal(user_difficulty): 
    """
    Perform addition on subtraction decimals depending on the difficulty: 
    Easy --> x.x += x.x
    Medium --> x.xx += x.xx
    Hard :) --> xx.xxx += xx.xxx
    """
    user_score_add = 0 
    incorrect_addition_subtraction_decimal_add = 0

    #Pick random either + or -
    if random.random() < 0.5:
        plus_minus = "+"
    else:
        plus_minus = "-"

    #Pick if positive or negative numbers 
    pos_neg = random.random()
    if pos_neg > 0.5:
        pos_neg_value = 1
    else: 
        pos_neg_value = -1


    if user_difficulty == 1:
        first_number = float(dec.Decimal(str(random.randint(1,9)*pos_neg_value+round(random.random(),1))))
        second_number = float(dec.Decimal(str(random.randint(1,9)+round(random.random(),1))))
        
        if plus_minus == "+":
            answer = first_number + second_number
        else: 
            answer = first_number - second_number 

        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {first_number} {plus_minus} {second_number} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                float(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if float(user_answer) == float(answer):
            user_score_add += 1 
            return user_score_add, incorrect_addition_subtraction_decimal_add
        else:
            incorrect_addition_subtraction_decimal_add += 1 
            return user_score_add, incorrect_addition_subtraction_decimal_add


    if user_difficulty == 2:
        first_number = float(dec.Decimal(str(random.randint(1,19)*pos_neg_value+round(random.random(),2))))
        second_number = float(dec.Decimal(str(random.randint(1,9)+round(random.random(),2))))
        
        if plus_minus == "+":
            answer = first_number + second_number
        else: 
            answer = first_number - second_number 

        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {first_number} {plus_minus} {second_number} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                float(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if round(float(user_answer),2) == round(float(answer),2):
            user_score_add += 1 
            return user_score_add, incorrect_addition_subtraction_decimal_add
        else:
            incorrect_addition_subtraction_decimal_add += 1 
            return user_score_add, incorrect_addition_subtraction_decimal_add

    if user_difficulty == 3:
        first_number = float(dec.Decimal(str(random.randint(1,19)*pos_neg_value+round(random.random(),3))))
        second_number = float(dec.Decimal(str(random.randint(1,19)+round(random.random(),3))))
        
        if plus_minus == "+":
            answer = first_number + second_number
        else: 
            answer = first_number - second_number 

        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {first_number} {plus_minus} {second_number} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                float(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if round(float(user_answer),3) == round(float(answer),3):
            user_score_add += 1 
            return user_score_add, incorrect_addition_subtraction_decimal_add
        else:
            incorrect_addition_subtraction_decimal_add += 1 
            return user_score_add, incorrect_addition_subtraction_decimal_add

def multiplication_decimal(user_difficulty): 
    """
    Perform multiplication on decimals depending on the difficulty:
    Easy --> x.xx * integer 
    Medium --> xx.x * x.x
    Hard --> xx.xx * x.xx 
    """
    user_score_add = 0 
    incorrect_multiplication_decimal_add = 0

    #Pick if positive or negative numbers 
    pos_neg = random.random()
    if pos_neg > 0.5:
        pos_neg_value = 1
    else: 
        pos_neg_value = -1

    if user_difficulty == 1: 
        first_number = float(random.ranint(1,9)+dec.Decimal(str(pos_neg_value*round(random.random(),2))))
        second_number = int(random.randint(1,9))
        answer = first_number * second_number

        while True:
            user_answer = input(f"Compute: {first_number} × {second_number} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                float(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if round(float(user_answer),1) == round(float(answer),1):
            user_score_add += 1 
            return user_score_add, incorrect_multiplication_decimal_add
        else:
            incorrect_multiplication_decimal_add += 1 
            return user_score_add, incorrect_multiplication_decimal_add


    if user_difficulty == 2: 
        first_number = float(random.randint(10,49)+dec.Decimal(str(pos_neg_value*round(random.random(),1))))
        second_number = float(random.randint(1,9)+dec.Decimal(str(pos_neg_value*round(random.random(),1))))
        answer = first_number * second_number

        while True:
            user_answer = input(f"Compute: {first_number} × {second_number} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                float(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if round(float(user_answer),1) == round(float(answer),1):
            user_score_add += 1 
            return user_score_add, incorrect_multiplication_decimal_add
        else:
            incorrect_multiplication_decimal_add += 1 
            return user_score_add, incorrect_multiplication_decimal_add

    if user_difficulty == 3: 
        first_number = float(random.randint(10,49)+dec.Decimal(str(pos_neg_value*round(random.random(),2))))
        second_number = float(random.randint(1,9)+dec.Decimal(str(pos_neg_value*round(random.random(),2))))
        answer = first_number * second_number

        while True:
            user_answer = input(f"Compute: {first_number} × {second_number} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                float(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if round(float(user_answer),2) == round(float(answer),2):
            print("correct)")
            user_score_add += 1 
            return user_score_add, incorrect_multiplication_decimal_add
        else:
            incorrect_multiplication_decimal_add += 1
            print("incorrect") 
            return user_score_add, incorrect_multiplication_decimal_add

    

def division_decimal(user_difficulty): 
    """
    Perform divison on decimals resulting in:
    Easy --> always give answer either no remainder or 0.5
    Medium --> always give answer of no remainder or 0.25, 0.5, 0.75
    Hard --> always give answer of no remainder or a multiple of 0.1
    """
    user_score_add = 0
    incorrect_division_integer_add = 0 
    list_1 = [0.5, 0.5, 1]
    list_2 = [0.25, 0.5, 0.75, 0.2, 0.6, 0.8]
    list_3 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6 , 0.7, 0.8, 0.9]

    if user_difficulty == 1:
        pos_neg = random.random()
        if pos_neg > 0.5:
            divisor = random.randint(1,9) * (-1)
        else: 
            divisor = random.randint(1,9)

        calculate_to_be_divided =random.choice(list_1) + random.randint(1,9)
        to_be_divided = calculate_to_be_divided*divisor

        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {to_be_divided} ÷ {divisor} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                float(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if round(float(user_answer),1) == round(calculate_to_be_divided,1):
            user_score_add += 1 
            return user_score_add, incorrect_division_integer_add
        else:
            incorrect_division_integer_add += 1
            return user_score_add, incorrect_division_integer_add


    if user_difficulty == 2:
        pos_neg = random.random()
        if pos_neg > 0.5:
            divisor = random.randint(1,9) * (-1)
        else: 
            divisor = random.randint(1,9)

        calculate_to_be_divided =random.choice(list_2) + random.randint(1,9)
        to_be_divided = calculate_to_be_divided*divisor

        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {to_be_divided} ÷ {divisor} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                float(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if round(float(user_answer),2) == round(calculate_to_be_divided,2):
            user_score_add += 1 
            return user_score_add, incorrect_division_integer_add
        else:
            incorrect_division_integer_add += 1
            return user_score_add, incorrect_division_integer_add


    if user_difficulty == 3:
        pos_neg = random.random()
        if pos_neg > 0.5:
            divisor = random.randint(1,9) * (-1)
        else: 
            divisor = random.randint(1,9)

        calculate_to_be_divided =random.choice(list_3) + random.randint(1,9)
        to_be_divided = round(calculate_to_be_divided*divisor,1)

        #Verify user answer is a number 
        while True:
            user_answer = input(f"Compute: {to_be_divided} ÷ {divisor} = ").replace("−", "-") #Negative sign on your keyboard is not the "proper" minus sign
            value_position_start = user_answer.find("=")
            user_answer_value = user_answer[value_position_start+1:] 

            try: 
                float(user_answer_value)
            except ValueError:
                print(f"'{user_answer}' is not a valid response. Please enter a numerical value!")
            else: 
                break

        if round(float(user_answer),2) == round(calculate_to_be_divided,2):
            user_score_add += 1 
            return user_score_add, incorrect_division_integer_add
        else:
            incorrect_division_integer_add += 1
            return user_score_add, incorrect_division_integer_add


def addition_subtraction_fraction(user_difficulty): #Haven't added to game yet 
    """
    Perform addition and subtraction of fractions:
    Easy --> x/x and x/x (denominator is a simple common factor)
    Medium --> x/x and x/x (denonminator is not a common factor)
    Hard --> x/xx and xx/x (denominator is not a commoon factor)
    
    """
    user_score_add = 0 
    incorrect_addition_subtraction_fraction_add = 0
    
    if random.random() > 0.5: 
        plus_minus = "-"
    else:
        plus_minus = "+" 


    if user_difficulty == 1: 
        random_denominator = [0.5, 2, 3, 4, 5]
        first_denom = random.random(1,9)
        second_denom = first_denom * random.choice(random_denominator)

        first_number = fractions.Fraction(random.randint(1,9),first_denom)
        second_number = fractions.Fraction(random.randint(1,9), second_denom)

        if plus_minus == "+":
            answer = first_number + second_number
        else:
            answer = first_number - second_number 

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

        if str(answer) == user_answer: 
            user_score_add += 1 
            return user_score_add, incorrect_addition_subtraction_fraction_add 
        else:
            incorrect_addition_subtraction_fraction_add  += 1
            return user_score_add, incorrect_addition_subtraction_fraction_add 


    if user_difficulty == 2: 
        random_denominator = [0.5, 2, 3, 4, 5, 6, 7, 8, 9]
        first_denom = random.random(1,9)
        second_denom = first_denom * random.choice(random_denominator)

        first_number = fractions.Fraction(random.randint(1,9),first_denom)
        second_number = fractions.Fraction(random.randint(1,9), second_denom)

        if plus_minus == "+":
            answer = first_number + second_number
        else:
            answer = first_number - second_number 

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

        if str(answer) == user_answer: 
            user_score_add += 1 
            return user_score_add, incorrect_addition_subtraction_fraction_add 
        else:
            incorrect_addition_subtraction_fraction_add  += 1
            return user_score_add, incorrect_addition_subtraction_fraction_add 


def multiplication_fraction(user_difficulty):
    """
    Perform multiplication of fractions:
    Easy --> fraction * integer
    Medium --> (x/x) * (x/x)
    Hard --> (x/x) * (x/x) (multiplied by a common factor diagonally) or (multiplied by a common factor vertically)
    """
    user_score_add = 0 
    incorrect_multiplication_fraction_add = 0 

    #Random multiplication (top left to bottom right, reverse of that, second number vertically, reverse of that)


    pass 

def division_fraction(user_difficulty): 
    pass