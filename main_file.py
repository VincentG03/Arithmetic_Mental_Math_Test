from functions import *

if __name__ == "__main__":      
    continue_check = 1 

    while continue_check == 1:
        #Print difficulty screen
        user_difficulty, user_questions = difficulty_screen() 

        #Run questions and retrieve player data 
        user_score, elapsed_time, number_of_questions, incorrect_list =  run_questions(user_difficulty, user_questions)

        #Print ending/feedback messages
        print("/////////////////////////////////////////")
        print(f"You have scored {int((user_score/number_of_questions)*100)}% ({user_score} out of {number_of_questions}).") #Run the questions with difficulty set to user input
        print(f"Your total time taken was {round(elapsed_time, 2)} seconds.")
        average_question_time = elapsed_time/number_of_questions
        print(f"You spent an average of {round(average_question_time, 2)} seconds on each question.")

        #If all correct, not specific feedback is needed
        if len(incorrect_list) == 0: 
            all_correct = 1 
        else:
            all_correct = 0 

        #If everything was not all correct, determine the areas of mistakes
        if all_correct == 0:
            for i in range(len(incorrect_list)):
                if incorrect_list[i] == "integer addition subtraction":
                    number_qs_wrong = incorrect_list[i+1]
                    if number_qs_wrong == 1: 
                        print("You may wish to revise addition and subtraction of integers as you got a question wrong.")
                    else:
                        print(f"You may wish to revise addition and subtraction of integers as you got {number_qs_wrong} questions wrong.")
                if incorrect_list[i] == "integer multiplication":
                    number_qs_wrong = incorrect_list[i+1]
                    if number_qs_wrong == 1: 
                        print("You may wish to revise multiplication of integers as you got a question wrong.")
                    else:
                        print(f"You may wish to revise multiplication of integers as you got {number_qs_wrong} questions wrong.")
                if incorrect_list[i] == "integer division":
                    number_qs_wrong = incorrect_list[i+1]
                    if number_qs_wrong == 1: 
                        print("You may wish to revise division of integers as you got a question wrong.")
                    else:
                        print(f"You may wish to revise division of integers as you got {number_qs_wrong} questions wrong.")
                if incorrect_list[i] == "decimal addition subtraction":
                    number_qs_wrong = incorrect_list[i+1]
                    if number_qs_wrong == 1: 
                        print("You may wish to revise addition and subtraction of decimals as you got a question wrong.")
                    else:
                        print(f"You may wish to revise addition and subtraction of decimals as you got {number_qs_wrong} questions wrong.")

                if incorrect_list[i] == "decimal multiplication":
                    number_qs_wrong = incorrect_list[i+1]
                    if number_qs_wrong == 1: 
                        print("You may wish to revise multiplication of decimals as you got a question wrong.")
                    else:
                        print(f"You may wish to revise multiplication of decimals as you got {number_qs_wrong} questions wrong.")
                
        else:
            print("Congratulations on getting every single question correct!")
        
        print("/////////////////////////////////////////")

        #Print concluding message
        play_again = input("Would you like to play again? (Y/N): ")
        if play_again == "N" or play_again == "n":
            print("Thank you for playing, stay smart :)")
            continue_check = 0  
