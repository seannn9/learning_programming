import os
import time
import random



# RANDOM NUMBER GUESSING
def random_number_guessing():
    
    loading()

    print("\n")
    print(" " * 21, "Random Number Guessing!")
    
    number_of_guesses = 0

    while True:
        if number_of_guesses == 0:
            limit = int(input("\nEnter a number: "))
            if limit < 1:
                print("Too few!")
                quit()
            
            random_num = random.randrange(0, limit + 1)
        
        player_guess = int(input(f"Guess the random number between 0 and {limit}: "))
        number_of_guesses += 1

        if player_guess > random_num:
            print(" " * 10, "Guess a lower number!")
        elif player_guess < random_num:
            print(" " * 10, "Guess a higher number!")
        else:
            print(f"\nYou guessed the random number ({random_num}) in {number_of_guesses} tries!\nCongrats!")
            play_again = input("\nDo you want to play again? y/n: ").lower()

            if play_again == 'y':
                number_of_guesses = 0
                limit = 0
                os.system("cls")
                print("\nLet's play again!")
                continue
            elif play_again == 'n':
                other = input("\nWould you like to play other games available? y/n: ").lower()
                if other == 'y':
                    os.system("cls")
                    main()
                elif other == 'n':
                    os.system("cls")
                    print("\nOkay! Thanks for playing!")
                    quit()
            else:
                os.system("cls")
                print("\nInvalid input!")
                quit()



# ROCK, PAPER, SCISSORS
def rock_paper_scissors():
    
    loading()

    print("\n")
    print(" " * 21, "Rock, Paper, Scissors!")

    while True:
        computer_attacks = ['rock', 'paper', 'scissors']
        player_score = 0
        computer_score = 0
        draw_score = 0

        number_of_rounds = int(input("\nHow many rounds do you want to play? "))
        if number_of_rounds < 1:
            print("Number of rounds too low! At least 1 round!")
            quit()
        else:
            print("Let's play!\n")

            for i in range(1, number_of_rounds + 1):
                computer_attack = random.choice(computer_attacks)
                player_attack = input("\nYour attack: ").lower()

                if player_attack == 'rock':
                    if computer_attack == 'rock':
                        print(f"Computer's Attack: {computer_attack}")
                        print("Draw!")
                        draw_score += 1
                    elif computer_attack == 'paper':
                        print(f"Computer's Attack: {computer_attack}")
                        print("Computer scored!")
                        computer_score += 1
                    elif computer_attack == 'scissors':
                        print(f"Computer's Attack: {computer_attack}")
                        print("You scored!")
                        player_score += 1

                elif player_attack == 'paper':
                    if computer_attack == 'rock':
                        print(f"Computer's Attack: {computer_attack}")
                        print("You scored!")
                        player_score += 1
                    elif computer_attack == 'paper':
                        print(f"Computer's Attack: {computer_attack}")
                        print("Draw!")
                        draw_score += 1
                    elif computer_attack == 'scissors':
                        print(f"Computer's Attack: {computer_attack}")
                        print("Computer scored!")
                        computer_score += 1

                elif player_attack == 'scissors':
                    if computer_attack == 'rock':
                        print(f"Computer's Attack: {computer_attack}")
                        print("Computer scored!")
                        computer_score += 1
                    elif computer_attack == 'paper':
                        print(f"Computer's Attack: {computer_attack}")
                        print("You scored!")
                        player_score += 1
                    elif computer_attack == 'scissors':
                        print(f"Computer's Attack: {computer_attack}")
                        print("Draw!")
                        draw_score += 1
                
                else:
                    print("Invalid attack!")
                    continue
            
            if player_score > computer_score:
                print(f"\nFINAL SCORES:\nYou: {player_score}\nComputer: {computer_score}\nDraw: {draw_score}")
                print("You won the game! Congrats!")
                play_again = input("\nWould you like to play again or play another game? again/another/no: ").lower()
                if play_again == 'again':
                    number_of_rounds = 0
                    os.system("cls")
                    continue
                elif play_again == 'another':
                    os.system("cls")
                    main()
                elif play_again == 'no':
                    quit()
            
            elif player_score < computer_score:
                print(f"\nFINAL SCORES:\nYou: {player_score}\nComputer: {computer_score}\nDraw: {draw_score}")
                print("The Computer won the game!")
                play_again = input("\nWould you like to play again or play another game? again/another/no: ").lower()
                if play_again == 'again':
                    number_of_rounds = 0
                    os.system("cls")
                    continue
                elif play_again == 'another':
                    os.system("cls")
                    main()
                elif play_again == 'no':
                    quit()
            
            else:
                print(f"\nFINAL SCORES:\nYou: {player_score}\nComputer: {computer_score}\nDraw: {draw_score}")
                print("It's a draw!")
                play_again = input("\nWould you like to play again or play another game? again/another/no: ").lower()
                if play_again == 'again':
                    number_of_rounds = 0
                    os.system("cls")
                    continue
                elif play_again == 'another':
                    os.system("cls")
                    main()
                elif play_again == 'no':
                    quit()



# TRIVA QUIZ
def quiz_game():
    
    loading()

    print("\n")
    print(" " * 21, "Quiz Game!")

    while True:
        score = 0
        print("\nCategories:")
        print(" " * 5, "Computer")
        print(" " * 5, "Science")
        print(" " * 5, "Geography")
        categories = input("\nPick a category of the quiz: ").lower()
        if categories == 'computer':
            print("\n")
            print(" " * 21, "Computer Category\n")
            question1 = input("1. What does RAM stand for? ").lower()
            if question1 == "random access memory":
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
            
            question2 = input("\n2. What is the main processing unit in a computer? ").lower()
            if question2 == 'cpu' or question2 == "central processing unit":
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")

            question3 = input("\n3. What does GPU mean? ").lower()
            if question3 == 'graphics processing unit':
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")

            question4 = input("\n4. What does ROM mean? ").lower()
            if question4 == 'read only memory':
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")

            question5 = input("\n5. Who invented the first computer? ").lower()
            if question5 == "charles babbage":
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
            
            question6 = input("\n6. What is the computer's main ciruit board? ").lower()
            if question6 == "motherboard":
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
            
            question7 = input("\n7. What does CRT mean? ").lower()
            if question7 == "cathode ray tube":
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
            
            question8 = input("\n8. Which computer hardware device performs the functions like click, point, drag, or select? ").lower()
            if question8 == "mouse":
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
            
            question9 = input("\n9. What software has their code publicy available to be edited or forked by any user? ").lower()
            if question9 == "open-source application" or question9 == "open source" or question9 == "open source apps":
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")

            question10 = input("\n10. What does CD-ROM mean? ").lower()
            if question10 == "compact disk read only memory" or question10 == "compact disk-read only memory":
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")

            print(f"\nQuiz over! Your final score is {score}/10!")
            if score < 5:
                play_again = input("You failed the quiz! Would you like to play again? y/n: ").lower()
                if play_again == 'y':
                    os.system("cls")
                    print("Okay! Let's play again! Goodluck!\n")
                    continue
                elif play_again == 'n':
                    other = input("Okay! Do you want to play other games? y/n: ").lower()
                    if other == 'y':
                        os.system("cls")
                        main()
                    elif other == 'n':
                        os.system("cls")
                        print("Okay! Thanks for playing!")
                        quit()
                    else:
                        print("Invalid input!")
                        quit()
            elif score == 10:
                print("You scored a perfect score! Congrats!\n")
                play_again = input("Would you like to answer another category or play another game? (game/category/no): ").lower()
                if play_again == 'game':
                    os.system("cls")
                    main()
                elif play_again == 'category':
                    os.system("cls")
                    continue
                elif play_again == 'no':
                    os.system("cls")
                    print("Okay! Thanks for playing!")
                    quit()
                else:
                    print("Invalid input!")
                    quit()
            else:
                print("You passed the quiz! Congrats!")
                play_again = input("Would you like to answer another category or play another game? (game/category/no): ").lower()
                if play_again == 'game':
                    os.system("cls")
                    main()
                elif play_again == 'category':
                    os.system("cls")
                    continue
                elif play_again == 'no':
                    os.system("cls")
                    print("Okay! Thanks for playing!")
                    quit()
                else:
                    print("Invalid input!")
                    quit()


        elif categories == 'science':
            print("\n")
            print(" " * 21, "Science Category\n")
            question1 = input("\n1. This essential gas is important so that we can breath. ").lower()
            if question1 == 'oxygen':
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
            
            question2 = input("\n2. What is the nearest planet to the sun? ").lower()
            if question2 == 'mercury':
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
            
            question3 = input("\n3. What is the largest planet in the solar system? ").lower()
            if question3 == 'jupiter':
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")

            question4 = input("\n4. What is the boiling point of water? ").lower()
            if question4 == "100 degrees celcius" or question4 == "100 degrees" or question4 == "100 celcius":
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
            
            question5 = input("\n5. What's the largest known animal? ").lower()
            if question5 == "blue whale":
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
                
            question6 = input("\n6. What do bees collect to create honey? ").lower()
            if question6 == "nectar" or question6 == "nectars":
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
            
            question7 = input("\n7. Animals that eat both plants and meat are called what? ").lower()
            if question7 == "omnivores" or question7 == "omnivore":
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
            
            question8 = input("\n8. True or False: Lightning is hotter than the sun. ").lower()
            if question8 == 'true':
                print("Correct!")
                score += 1
            elif question8 == 'false':
                print("Wrong answer!")
            else:
                print("Invalid answer!")
            
            question9 = int(input("\n9. How many teeth does the adult human have? "))
            if question9 == 32:
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")

            question10 = input("\n10. What is the hardest known natural material on earth? ").lower()
            if question10 == "diamond" or question10 == "diamonds":
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")

            print(f"\nQuiz over! Your final score is {score}/10!")
            if score < 5:
                play_again = input("You failed the quiz! Would you like to play again? y/n: ").lower()
                if play_again == 'y':
                    os.system("cls")
                    print("Okay! Let's play again! Goodluck!\n")
                    continue
                elif play_again == 'n':
                    other = input("Okay! Do you want to play other games? y/n: ").lower()
                    if other == 'y':
                        os.system("cls")
                        main()
                    elif other == 'n':
                        os.system("cls")
                        print("Okay! Thanks for playing!")
                        quit()
                    else:
                        print("Invalid input!")
                        quit()
            elif score == 10:
                print("You scored a perfect score! Congrats!\n")
                play_again = input("Would you like to answer another category or play another game? (game/category/no): ").lower()
                if play_again == 'game':
                    os.system("cls")
                    main()
                elif play_again == 'category':
                    os.system("cls")
                    continue
                elif play_again == 'no':
                    os.system("cls")
                    print("Okay! Thanks for playing!")
                    quit()
                else:
                    print("Invalid input!")
                    quit()
            else:
                print("You passed the quiz! Congrats!")
                play_again = input("Would you like to answer another category or play another game? (game/category/no): ").lower()
                if play_again == 'game':
                    os.system("cls")
                    main()
                elif play_again == 'category':
                    os.system("cls")
                    continue
                elif play_again == 'no':
                    os.system("cls")
                    print("Okay! Thanks for playing!")
                    quit()
                else:
                    print("Invalid input!")
                    quit()



        elif categories == 'geography':
            print(" " * 21 + "Geography Category\n")
            question1 = input("\n1. What is the tallest mountain in the world? ").lower()
            if question1 in ["mt. everest", "mt everest", "mount everest", "mountain everest", "everest"]:
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
            
            for i in range(1, 4):
                question2 = input("\n2. Name 3 continent of the world (only input one at a time): ").lower()
                if question2 in ["africa", "asia", "north america", "south america" , "antartica", "europe", "australia"]:
                    print("Correct!")
                    if i == 3:
                        score += 1
                else:
                    print("Wrong answer!")
                
            question3 = input("\n3. What is the longest river in the world? ").lower()
            if question3 in ["nile", "the nile river", "nile river"]:
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
            
            question4 = input("\n4. What is the largest country in the world? ").lower()
            if question4 == "russia":
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
            
            question5 = int(input("\n5. How many states does the United States consist of? "))
            if question5 == 50:
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
            
            question6 = input("\n6. What is the coldest place on Earth? ").lower()
            if question6 == "antartica":
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")

            question7 = input("\n7. What is the largest continent on Earth? ").lower()
            if question7 == "asia":
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")
            
            question8 = input("\n8. What is the capital of Mexico? ").lower()
            if question8 == 'mexico city':
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")

            question9 = input("\n9. True or False: Is Canada a part of United States? ").lower()
            if question9 == 'true':
                print("Wrong answer!")
            elif question9 == 'false':
                print("Correct!")
                score += 1
            else:
                print("Invalid answer!")

            question10 = input("\n10. What is the largest ocean in the world? ").lower()
            if question10 in ["pacific", "the pacific ocean", "pacific ocean"]:
                print("Correct!")
                score += 1
            else:
                print("Wrong answer!")


            print(f"\nQuiz over! Your final score is {score}/10!")
            if score < 5:
                play_again = input("You failed the quiz! Would you like to play again? y/n: ").lower()
                if play_again == 'y':
                    os.system("cls")
                    print("Okay! Let's play again! Goodluck!\n")
                    continue
                elif play_again == 'n':
                    other = input("Okay! Do you want to play other games? y/n: ").lower()
                    if other == 'y':
                        os.system("cls")
                        main()
                    elif other == 'n':
                        os.system("cls")
                        print("Okay! Thanks for playing!")
                        quit()
                    else:
                        print("Invalid input!")
                        quit()
            elif score == 10:
                print("You scored a perfect score! Congrats!\n")
                play_again = input("Would you like to answer another category or play another game? (game/category/no): ").lower()
                if play_again == 'game':
                    os.system("cls")
                    main()
                elif play_again == 'category':
                    os.system("cls")
                    continue
                elif play_again == 'no':
                    os.system("cls")
                    print("Okay! Thanks for playing!")
                    quit()
                else:
                    print("Invalid input!")
                    quit()
            else:
                print("You passed the quiz! Congrats!")
                play_again = input("Would you like to answer another category or play another game? (game/category/no): ").lower()
                if play_again == 'game':
                    os.system("cls")
                    main()
                elif play_again == 'category':
                    os.system("cls")
                    continue
                elif play_again == 'no':
                    os.system("cls")
                    print("Okay! Thanks for playing!")
                    quit()
                else:
                    print("Invalid input!")
                    quit()
            


# LOADING
def loading():
    loading = "\nLoading..."
    for i in loading:
        print(i, end="")
        time.sleep(0.25)



# MAIN FUNCTION          
def main():
    print("\nGames to play:\n\nRandom number guessing game (RNG)\nRock, paper, scissors (RPS)\nQuiz Game (QZ)")
    game_play  = input("\nWhat game would you like to play? ").lower()

    if game_play == 'rng' or game_play == 'random number guessing game':
        random_number_guessing()
    elif game_play == 'rps' or game_play == 'rock, paper, scissors' or game_play == 'rock paper scissors':
        rock_paper_scissors()
    elif game_play == 'qz' or game_play == 'quiz game':
        quiz_game()
    else:
        print("Game not (yet) available!")
        quit()



# INTRODUCTION
def introduction():
    name = input("\nEnter your username: ")
    print("\n")
    print(" " * 21 + f"Hello {name}!")


introduction()
main()