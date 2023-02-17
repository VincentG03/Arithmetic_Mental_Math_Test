Author: Vincent Giang 
Created: 02-12-2022
Status: runnable, improvements continue to be added and are outlined below 


Program process:
- Ask for user input for the number of questions and difficulty 
- Depending on the input (number_of_user_questions, user_difficulty), prompt user (while factoring in desired difficuly) for answers to math questions of type:
    - Addition and subtraction of integers (2x chance)
    - Multiplication of integers 
    - Division with integer results 
    - Addition and subtraction of decimals (2x chance)
    - Multiplication of decimals 
    - Division of decimals
    - Addition and subtraction of fractions (2x chance)
    - Multipication of fractions 
    - Division of fractions
- Print result along with useful statistics and feedback 


To be added:
[ ] Fraction stuff (fractional adding)
[ ] Interface (tkinter)
[ ] Timer for each type of question (i.e you may) (which section they look the longest on)
[ ] Have an option of what question types they want 
[ ] Make the text not just appear, but type it out. 
[ ] Easter egg, number of questions = 0 (check line 21 functions file)

Known issues:
- (FIXED) When accepting input answers, does not catch error of when its not a number - assuming we would need try except statements but the body would be too long (read elsewhere that you should keep try statemnts as small as possible)
- Need to change the chace so its correct how it says in the program process 


