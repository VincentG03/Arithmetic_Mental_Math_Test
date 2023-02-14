from functions import *

#[x] Add a timer in
#[x] Add something to keep track of score
#[x] Add a timer to the run_questions 
#[x] Add improvement message

if __name__ == "__main__":      
    while True:
        user_difficulty, user_questions = difficulty_screen() #Print difficulty screen
        user_score, elapsed_time, number_of_questions, incorrect_list =  run_questions(user_difficulty, user_questions)
        print("/////////////////////////////////////////")
        print(f"You have scored {user_score} out of {number_of_questions}.") #Run the questions with difficulty set to user input
        print(f"Your total time taken was {round(elapsed_time, 2)} seconds.")
        average_question_time = elapsed_time/number_of_questions
        print(f"You spent an average of {round(average_question_time, 2)} seconds on each question.")


        #Printing feedback 
        for i in range(len(incorrect_list)): #Check if everything was correct 
            all_correct = 1
            if incorrect_list[i] == 0:
                continue 
            else: 
                all_correct = 0 

        #If everything was not all correct, determine which was the area with the most mistakes.
        if all_correct == 0:
            for i in range(len(incorrect_list)):
                if incorrect_list[i] == "a.s":
                    number_qs_wrong = incorrect_list[i+1]
                    print(f"You may wish to revise addition and subtraction of integers as you got {number_qs_wrong} question/s wrong.")
                if incorrect_list[i] == "m":
                    number_qs_wrong = incorrect_list[i+1]
                    print(f"You may wish to revise multiplication of integers as you got {number_qs_wrong} question/s wrong.")
                if incorrect_list[i] == "d":
                    number_qs_wrong = incorrect_list[i+1]
                    print(f"You may wish to revise division of integers as you got {number_qs_wrong} question/s wrong.")
        else:
            print("Congratulations for getting every single question correct!")
        
        print("/////////////////////////////////////////")
        play_again = input("Would you like to play again? (Y/N): ")
        if play_again == "Y" or play_again == "y":
            continue
        else: 
            print("Thank you for playing, stay smart :)")
            break   
        