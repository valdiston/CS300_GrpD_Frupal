# Trung Nguyen prototype for Event
import random
random.seed()


class Event:
    def __init__(self, name):
        self.name = name


class Energy(Event):

    def __init__(self, name):
        super().__init__(name)

    # Randomly play 1 of the 3 type of event: Trivia, math or sudden death
    def trigger(self, current, increase_by, type):
        rng = random.randint(1, 4)
        if rng == 1:
            return self.trigger_math(current, increase_by, type)
        if rng == 2:
            return self.trigger_trivia(current, increase_by, type)
        if rng == 3:
            return self.trigger_rock_paper_scissor(current, increase_by, type)
        if rng == 4:
            return self.trigger_number(current, increase_by, type)

    # Randomly play 1 of the 2 type of even: Trivia or math
    def trigger_no_sudden_death(self, current, increase_by, type):
        rng = random.randint(1, 4)
        if rng == 1:
            return self.trigger_math(current, increase_by, type)
        if rng == 2:
            return self.trigger_trivia(current, increase_by, type)
        if rng == 3:
            return self.trigger_rock_paper_scissor(current, increase_by, type)
        if rng == 4:
            return self.trigger_number(current, increase_by, type)

    def trigger_math(self, current, increase_by, type):
        print(" This even will ask you to answer a math question")
        rng = random.randint(1, 3)
        if rng == 1:
            number1 = random.randint(1, 100)
            number2 = random.randint(1, 100)
            print(" What is ", number1, " + ", number2)
            answer = input("> ")
            while not answer.isnumeric():
                print(" Please enter a number")
                print(" What is ", number1, " + ", number2)
                answer = input("> ")
            answer = int(answer)
            if answer == number1 + number2:
                print(" Correct. Your " + type + " is increase by: ", increase_by)
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" Incorrect, you miss your chance")
                input("Press enter to continue > ")
        if rng == 2:
            number1 = random.randint(1, 100)
            number2 = random.randint(1, 100)
            print(" What is ", number1, " - ", number2)
            answer = input("> ")
            while not answer.isnumeric():
                print(" Please enter a number")
                print(" What is ", number1, " + ", number2)
                answer = input("> ")
            answer = int(answer)
            if answer == number1 - number2:
                print(" Correct. Your " + type + " is increase by: ", increase_by)
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" Incorrect, you miss your chance")
                input("Press enter to continue > ")
        if rng == 3:
            number1 = random.randint(1, 100)
            number2 = random.randint(1, 100)
            print(" What is ", number1, " * ", number2)
            answer = input("> ")
            while not answer.isnumeric():
                print(" Please enter a number")
                print(" What is ", number1, " * ", number2)
                answer = input("> ")
            answer = int(answer)
            if answer == number1 * number2:
                print(" Correct. Your " + type + " is increase by: ", increase_by)
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" Incorrect, you miss your chance")
                input("Press enter to continue > ")
        return current

    def trigger_trivia(self, current, increase_by, type):
        rng = random.randint(1, 10)
        if rng == 1:
            print(" In C++, what symbol you must put at the end of a statement ?")
            answer = input("> ")
            if answer == ';':
                print(" Correct. Your " + type + " is increase by: ", increase_by)
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" Incorrect. You miss your chance")
                input("Press enter to continue > ")
        if rng == 2:
            print(" In C++, how do you dereference a pointer ?")
            answer = input("> ")
            if answer == '*':
                print(" Correct. Your " + type + " is increase by: ", increase_by)
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" Incorrect. You miss your chance")
                input("Press enter to continue > ")
        if rng == 3:
            print(" In C++, what is the symbol for pointer ?")
            answer = input("> ")
            if answer == '->':
                print(" Correct. Your "+type+" is increase by: ", increase_by)
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" Incorrect. You miss your chance")
                input("Press enter to continue > ")
        if rng == 4:
            print(" In Counter Strike: Global Offensive, how much does the SG 553 cost ?")
            answer = input("> ")
            while not answer.isnumeric():
                print(" Please enter a number")
                answer = input("> ")
            answer = int(answer)
            if answer == 2750:
                print(" Correct. Your " + type + " is increase by: ", increase_by)
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" Incorrect. You miss your chance")
                input("Press enter to continue > ")
        if rng == 5:
            print(" Which bird can fly backward ?")
            answer = input("> ")
            if answer.capitalize() == "Hummingbird":
                print(" Correct. Your " + type + " is increase by: ", increase_by)
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" Incorrect. You miss your chance")
                input("Press enter to continue > ")

        if rng == 6:
            print(" What type of animal is a wahoo?")
            answer = input("> ")
            if answer.capitalize() == "Fish":
                print(" Correct. Your " + type + " is increase by: ", increase_by)
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" Incorrect. You miss your chance")
                input("Press enter to continue > ")

        if rng == 6:
            print(" What type of animal is a horny toad?")
            answer = input("> ")
            if answer.capitalize() == "Lizard":
                print(" Correct. Your " + type + " is increase by: ", increase_by)
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" Incorrect. You miss your chance")
                input("Press enter to continue > ")

        if rng == 7:
            print(" What type of animal is a mountain chicken ?")
            answer = input("> ")
            if answer.capitalize() == "Frog":
                print(" Correct. Your " + type + " is increase by: ", increase_by)
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" Incorrect. You miss your chance")
                input("Press enter to continue > ")

        if rng == 8:
            print(" What letter is defined as the square root of -1?")
            answer = input("> ")
            if answer == "i":
                print(" Correct. Your " + type + " is increase by: ", increase_by)
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" Incorrect. You miss your chance")
                input("Press enter to continue > ")

        if rng == 9:
            print(" What is the weight of 1 liter of water in kilogram ?")
            answer = input("> ")
            if answer == "1":
                print(" Correct. Your "+type+" is increase by: ", increase_by)
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" Incorrect. You miss your chance")
                input("Press enter to continue > ")

        if rng == 9:
            print(" What is the name of the university that Bill Gate dropped out of")
            answer = input("> ")
            if answer.capitalize() == "Harvard":
                print(" Correct. Your " + type + " is increase by: ", increase_by)
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" Incorrect. You miss your chance")
                input("Press enter to continue > ")

        if rng == 10:
            print(" In a regular deck of cards, which is the only king without a moustache ?")
            answer = input("> ")
            if answer.capitalize() == "Heart":
                print(" Correct. Your " + type + " is increase by: ", increase_by)
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" Incorrect. You miss your chance")
                input("Press enter to continue > ")

        return current

    def trigger_death(self, current,increase_by):
        rng = random.randint(1, 3)
        print(" You triggered a sudden death. If you answer wrong, the game will be over")
        if rng == 1:
            print(" A cute fuzzy animal comes up to you. Do you touch it or not. Y/N")
            answer = input("> ")
            if answer.capitalize() == "Y":
                print(" You got brutally murdered by the animal. Game over")
                current = 0
                input("Press enter to continue > ")
            else:
                print(" The cute animal turns out to be a poisonous. You are lucky")
                input("Press enter to continue > ")
        if rng == 2:
            print(" You found the game developers. Do you want to die? Y/N")
            answer = input("> ")
            if answer.capitalize() == "N":
                print(" You got brutally murdered . Game over")
                current = 0
                input("Press enter to continue > ")
            else:
                print(" The game developers blessed you with: ", increase_by, " energy")
                current = current + increase_by
                input("Press enter to continue > ")
        if rng == 3:
            print(" Say the alphabet backward in LOWER CASE and NO space between them")
            answer = input("> ")
            if answer == "zyxwvutsrqponmlkjihgfedcba":
                print(" Correct! Your energy just got double !!")
                current = current * 2
                input("Press enter to continue > ")
            else:
                print(" Incorrect. Game over")
                input("Press enter to continue > ")
                current = 0
        return current

    def trigger_rock_paper_scissor(self, current, increase_by, type):
        print(" In this event, you have to play a game of rock, paper, scissor")
        print(" Please choose what you would like to play. R for rock. P for paper. Anything else for scissor")
        answer = input("> ")

        # Assign hand for user
        if answer.capitalize() == "R":
            user = "Rock"
        elif answer.capitalize() == "P":
            user = "Paper"
        else:
            user = "Scissor"

        # Assign hand for computer
        rng = random.randint(1, 3)
        if rng == 1:
            computer = "Rock"
        if rng == 2:
            computer = "Paper"
        if rng == 3:
            computer = "Scissor"

        # Compare the result
        if user == "Rock":
            if computer == "Rock":
                print(" It's a draw but you still get " + type + " for your effort")
                current = current + increase_by
                input("Press enter to continue > ")
            elif computer == "Paper":
                print(" You played Rock and the computer played Paper. You lose ")
                input("Press enter to continue > ")
            else:
                print(" You played Rock and the computer played Scissor. You win")
                current = current + increase_by
                input("Press enter to continue > ")

        elif user == "Paper":
            if computer == "Paper":
                print(" It's a draw but you still get " + type + " for your effort")
                current = current + increase_by
                input("Press enter to continue > ")
            elif computer == "Rock":
                print(" You played Paper and the computer played Rock. You win !!")
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" You played Paper and the computer played Scissor. You lose")
                input("Press enter to continue > ")

        if user == "Scissor":
            if computer == "Scissor":
                print(" It's a draw but you still get "+type+" for your effort")
                current = current + increase_by
                input("Press enter to continue > ")
            elif computer == "Paper":
                print(" You played Scissor and the computer played Paper. You win !!")
                current = current + increase_by
                input("Press enter to continue > ")
            else:
                print(" You played Scissor and the computer played Rock. You lose")
                input("Press enter to continue > ")

        return current

    def trigger_number(self, current, increase_by, type):
        print(" This even will make you guess a random number")
        print(" Choose your difficult: ")
        print("     1-Easy. Half the reward")
        print("     2-Medium. No modification to the reward")
        print("     3-Hard. Double the reward")
        print(" If you enter a number smaller than 1 or larger than 3, you will lose this event immediately!!")
        choice = input("> ")
        while not choice.isnumeric():
            print(" Please enter a number")
            choice = input("> ")
        choice = int(choice)
        if choice < 1 or choice > 3:
            print(" Haha, just kidding. You are a dare devil. Your reward is:", increase_by, "" + type)
            current = current + increase_by
            input("Press enter to continue > ")
        if choice == 1:
            print(" You chose Easy difficult")
            rng = random.randint(1, 2)
            print(" I'm thinking a number between 1 and 2. Guess which number I'm thinking of")
            answer = int(input("> "))
            if answer == rng:
                print(" Correct ! Your " + type + " is increase by: ", int(increase_by/2))
                current = current + int(increase_by/2)
                input("Press enter to continue > ")
            else:
                print(" Incorrect! You missed your chance")
                input("Press enter to continue > ")

        if choice == 2:
            print(" You chose Medium difficult")
            rng = random.randint(1, 3)
            print(" I'm thinking a number between 1 and 3. Guess which number I'm thinking of")
            answer = int(input("> "))
            if answer == rng:
                print(" Correct. Your " + type + " is increase by: ", increase_by)
                current += increase_by
                input("Press enter to continue > ")
            else:
                print(" Incorrect! You missed your chance")
                input("Press enter to continue > ")

        if choice == 3:
            print(" You chose Hard difficult")
            rng = random.randint(1, 4)
            print("I'm thinking a number between 1 and 4. Guess which number I'm thinking of")
            answer = int(input("> "))
            if answer == rng:
                print(" Correct. Your " + type + " is increase by: ", increase_by * 2)
                current = current + increase_by * 2
                input("Press enter to continue > ")
            else:
                print(" Incorrect! You missed your chance")
                input("Press enter to continue > ")

        return current


def test():
    energy1 = Energy("Event")
    current = 50
    increase_by = 15
    current = energy1.trigger_math(current, increase_by, "health")
    print("Your current energy is: ", current)
    if current == 0:
        print("You're dead")


if __name__ == "__main__":
    test()
    exit()
