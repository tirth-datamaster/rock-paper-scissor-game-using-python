import random


rock = '''                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
                                            '''
                                            
                                            
                                            
paper = '''                                                          
                                                          
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88                                '''                                                


scissor = '''                     88                                                       
                     ""                                                       
                                                                              
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  
                                                                              
                                                                              '''
                                                                              
                                                                              
game_images = [rock,paper,scissor]    
                                                                          
# Print multiline instruction
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")


user_choice = int(input("What do you choose ? type 0 for rock, type 1 for paper,type 2 for scissor...: "))
print("User Choose: ")
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer Choose: ")
print(game_images[computer_choice])


if user_choice>=3 and user_choice < 0:
    print("You Typed invalid number.Please try again")
elif user_choice == 0 and computer_choice == 2:
    print("You win!..")
elif computer_choice == 0 and user_choice == 2:
    print("You Loseee..Computer Wins")
elif computer_choice > user_choice:
    print("You Loseee")
elif user_choice > computer_choice:
    print("You Win......")
elif user_choice == computer_choice:
    print("It's Draw....")