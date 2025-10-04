## Read questions from file
def load_jewellery_questions():
    my_questions = []    
    with open('jewellery_questions.txt', 'r') as file:
        for line in file:
            my_questions.append(line.strip())
    return my_questions

# User welcome when entering quiz
user = input('What is your name? ')
print('Welcome to the quiz', user)

# Identifies how many options are available in the multiple choice questions, and handles it differently. 
for current_question in load_jewellery_questions():
    print(current_question)
    
    # Mixed questions (MC + free text option)
    if 'Other: [Please specify]' in current_question:
        valid_input = False
        while not valid_input:
            answer = input('Choose A, B, C, D, E, F: ')
            
            # Check for E first (needs elaboration)
            if answer in ('E', 'e'):
                answer = input('Please elaborate: ')   
                if answer.strip() != "":
                    valid_input = True
                    print('Thank you for your response!')
                else:
                    print('Please provide an explanation when choosing E.')
            
            # Then check for standard MC answers (A-D, F only)
            elif answer in ('A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'F', 'f'):
                valid_input = True
                print('Good choice')
            #kindly note I struggled from line 38 - 40, so I used ai guidance to ensure the idea and logic flow remains intact
            # Then accept free text with content
            elif answer.strip() != "":
                valid_input = True
                print('Thank you for your response!')
            
            else:
                print('Invalid choice, please try again.')
    
    # 5-option questions
    elif '(a)' in current_question and '(b)' in current_question and '(c)' in current_question and '(d)' in current_question and '(e)' in current_question:
        valid_input = False
        while not valid_input: 
            answer = input('Choose A, B, C, D, E: ')  
            
            if answer in ('A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e'):
                valid_input = True
                print('Good choice')
            else:
                print('Invalid choice, please try again.')
    
    # 4-option questions
    elif '(a)' in current_question and '(b)' in current_question and '(c)' in current_question and '(d)' in current_question and '(e)' not in current_question:
        valid_input = False
        while not valid_input: 
            answer = input('Choose A, B, C, or D: ')
            
            if answer in ('A', 'a', 'B', 'b', 'C', 'c', 'D', 'd'):
                valid_input = True
                print('Good choice')
            else:
                print('Invalid choice, please try again.')
    
    # 3-option questions
    elif '(a)' in current_question and '(b)' in current_question and '(c)' in current_question and '(d)' not in current_question:
        valid_input = False
        while not valid_input: 
            answer = input('Choose A, B or C: ')
            
            if answer in ('A', 'a', 'B', 'b', 'C', 'c'):
                valid_input = True
                print('Good choice')
            else:
                print('Invalid choice, please try again.')
    
    # 2-option questions
    elif '(a)' in current_question and '(b)' in current_question and '(c)' not in current_question:
        valid_input = False
        while not valid_input: 
            answer = input('Choose A or B: ')
            
            if answer in ('A', 'a', 'B', 'b'):
                valid_input = True
                print('Good choice')
            else:
                print('Invalid choice, please try again.')
    
   

   #For questions that contain both mulitple choice options AND free text

else:
        answer = input('Your answer: ')
        print('Thank you for your response!')
        
#I must say, if , elif and else conditions were hammered in especially with using elif for multiway decisions and structuring the logic of 'else', to catch everything else, which in this case is free text/ any other repsonse than the multiple choice

    #kindly note, AI was used to re-inforce certain concepts and fix syntax errors and correct some lines, cheers to many more projects and learnings and thanks for checking what's under the hood! Please complete the quiz to see what I do with it next and the insights drawn!