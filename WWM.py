import sys
playerName = input("Hello and Welcome to the show Who want to be millionaire\nmay I get your name please?\n\n")

def introduction():
    print("\nRules and Regulations:"
            "\n\nQuestion 1 (30 Second time limit) \n $500"
            "\n\nQuestion 2 (30 Second time limit) \n $2500"
            "\n\nBARAGE $1000"
            "\n\nQuestion 3 (30 Second time limit) \n $5000"
            "\n\nQuestion 4 (30 Second) \n $10.000"
            "\n\nBARAGE $5000"
            "\n\nQuestion 5 (30 Second time limit) \n $50.000"
            "\n\nQuestion 6 (30 Second time limit) \n $100.000"
            "\n\nQuestion 7 (30 Second time limit) \n $150.000"
            "\n\nQuestion 8 (30 Second time limit) \n $250.000"
            "\n\nQuestion 9 (30 Second time limit) \n $500.000"
            "\n\nQuestion 10 (No time limit) \n $1.000.000"
            "\n\nYou can answer personal by only typing 'Yes' or ''No"
            "\n\nIn order to answer the questions properly\nJust type the letter of the answer you choose"
            "\n\nYou can always retreat from the competition by typing 'Quite' to the input")


def Question1():
    # Question and Answers
    compQuestion = str(input("\n\nAre you ready to start?\n"))
    if(str.lower(compQuestion) == "yes"):
        print("Which one is the capital city of Canada?")
        print("A) Toronto      C) Montreal")
        print("B) Vancover     D) Ottowa")
    #Cheat_Code
    elif(compQuestion == "Copy_Sheet"):
        print("Q1 = D \nQ2 = C \nQ3 = A \nQ4 = A \nQ5 = A \nQ6 = A \nQ7 = A \nQ8 = A \nQ9 = A \nQ10 = A")
        print("Which one is the capital city of Canada?")
        print("A) Toronto      C) Montreal")
        print("B) Vancover     D) Ottowa")
    else:
        print("Creator Burak Yildirim")

    # User Answer
    answer = str(input("\nMy final answer is "))
    if(str.upper(answer) == "D" ):
        print("\nYou are CORRECT\nYou earned $500") 
    elif(str.lower(answer) == "quite"):
        print(f"Thanks for Playing {playerName}\nYou earned $0")
        sys.exit()
    else:
        print("YOU LOST")

def Question2():
    # Question and Answers
    print("When is the next USA Presidental Elections?")
    print("A)2023    C)2020")
    print("B) 2021   D)2022")

    # User Answer
    answer = str(input("\nMy final answer is "))
    if(str.upper(answer) == "C" ):
        print("\nYou are CORRECT\nYou earned $1000")
        print("\nYou passed $1000 dolar barage now at least you will be leaving with 1000 dolar")
    elif(str.lower(answer) == "quite"):
        print(f"Thanks for Playing{playerName}\nYou earned $500")
        sys.exit()
    else:
        print("YOU LOST")

def Question3():
    # Question and Answers
    print("What is the result of this calculation 4/1+4*4 ")
    print("A) 20      B) 16")
    print("C) 24      D) 8")

    # User Answer
    answer = str(input("\nMy final answer is "))
    if(str.upper(answer) == "A" ):
        print("\nYou are CORRECT\nYou earned $5000")
    elif(str.lower(answer) == "quite"):
        print(f"Thanks for Playing{playerName}\nYou earned $1000")
        sys.exit()
    else:
        print("YOU LOST")

    

#Main   
introduction()
Question1()
Question2()
Question3()

                