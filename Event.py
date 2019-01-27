#Trung Nguyen prototype for Event
import random
class Event:
    def __init__(self, name):
        self.name=name

class Energy(Event):
    def __init__(self,name):
        super().__init__(name)
    def trigger(self,current_energy,increase_by): #Randomly play 1 of the 3 type of event: Trivia, math or sudden death
        rng = random.randint(1, 3)
        if rng ==1:
            return self.trigger_math(current_energy,increase_by)
        if rng == 2:
            return self.trigger_trivia(current_energy,increase_by)
        if rng == 3:
            return self.trigger_death(current_energy,increase_by)

    def trigger_no_sudden_death(self,current_energy,increase_by):#Randomly play 1 of the 2 type of even: Trivia or math
        rng = random.randint(1, 2)
        if rng ==1:
            return self.trigger_math(current_energy,increase_by)
        if rng == 2:
            return self.trigger_trivia(current_energy,increase_by)

    def trigger_math(self,current_energy,increase_by):
        rng=random.randint(1,3)
        if rng==1:
            number1= random.randint(1,100)
            number2= random.randint(1,100)
            print("What is ", number1," + ", number2 )
            answer=int(input())
            if answer== number1+number2:
                print("Correct. Your energy is increase by: ", increase_by)
                current_energy= current_energy+increase_by
            else:
                print("Incorrect, you miss your chance")
        if rng==2:
            number1= random.randint(1,100)
            number2= random.randint(1,100)
            print("What is ", number1," - ", number2 )
            answer=int(input())
            if answer== number1-number2:
                print("Correct. Your energy is increase by: ", increase_by)
                current_energy = current_energy + increase_by
            else:
                print("Incorrect, you miss your chance")
        if rng == 3:
            number1= random.randint(1,100)
            number2= random.randint(1,100)
            print("What is ", number1," * ", number2 )
            answer=int(input())
            if answer== number1*number2:
                print("Correct. Your energy is increase by: ", increase_by)
                current_energy = current_energy + increase_by
            else:
                print("Incorrect, you miss your chance")
        return current_energy

    def trigger_trivia(self, current_energy,increase_by):
        rng = random.randint(1, 4)
        if rng==1:
            print("In C++, what symbol you must put at the end of a statement ?")
            answer = input()
            if answer ==';':
                print("Correct. Your energy is increased by: ", increase_by)
                current_energy=current_energy+increase_by
            else:
                print("Incorrect. You miss your chance")
        if rng == 2:
            print("In C++, how do you dereference a pointer ?")
            answer = input()
            if answer == '*':
                print("Correct. Your energy is increased by: ", increase_by)
                current_energy = current_energy + increase_by
            else:
                print("Incorrect. You miss your chance")
        if rng == 3:
            print("In C++, what is the symbol for pointer ?")
            answer = input()
            if answer == '->':
                print("Correct. Your energy is increased by: ", increase_by)
                current_energy = current_energy + increase_by
            else:
                print("Incorrect. You miss your chance")
        if rng == 4:
            print("In Counter Strike: Global Offensive, how much does the SG 553 cost ?")
            answer = int(input())
            if answer == 2750:
                print("Correct. Your energy is increased by: ", increase_by)
                current_energy = current_energy + increase_by
            else:
                print("Incorrect. You miss your chance")
        if rng == 5 :
            print("Which bird can fly backward ?")
            answer =input()
            if answer.upper() == "Hummingbird":
                print("Correct. Your energy is increased by: ", increase_by)
                current_energy = current_energy + increase_by
            else:
                print("Incorrect. You miss your chance")

        if rng == 6:
            print("What type of animal is a wahoo?")
            answer = input()
            if answer.upper() == "Fish":
                print("Correct. Your energy is increased by: ", increase_by)
                current_energy = current_energy + increase_by
            else:
                print("Incorrect. You miss your chance")

        if rng == 6:
            print("What type of animal is a horny toad?")
            answer = input()
            if answer.upper() == "Lizard":
                print("Correct. Your energy is increased by: ", increase_by)
                current_energy = current_energy + increase_by
            else:
                print("Incorrect. You miss your chance")

        if rng == 7:
            print("What type of animal is a mountain chicken ?")
            answer = input()
            if answer.upper() == "Frog":
                print("Correct. Your energy is increased by: ", increase_by)
                current_energy = current_energy + increase_by
            else:
                print("Incorrect. You miss your chance")

        if rng == 8:
            print("WWhat letter is defined as the square root of -1?")
            answer = input()
            if answer == "i":
                print("Correct. Your energy is increased by: ", increase_by)
                current_energy = current_energy + increase_by
            else:
                print("Incorrect. You miss your chance")

        if rng == 9:
            print("What is the weight of 1 liter of water in kilogram ?")
            answer = input()
            if answer == "1":
                print("Correct. Your energy is increased by: ", increase_by)
                current_energy = current_energy + increase_by
            else:
                print("Incorrect. You miss your chance")

        if rng == 9:
            print("What is the name of the university that Bill Gate dropped out of")
            answer = input()
            if answer.upper() == "Havard":
                print("Correct. Your energy is increased by: ", increase_by)
                current_energy = current_energy + increase_by
            else:
                print("Incorrect. You miss your chance")

        if rng == 10:
            print("In a regular deck of cards, which is the only king without a moustache ?")
            answer = input()
            if answer.upper() == "Heart":
                print("Correct. Your energy is increased by: ", increase_by)
                current_energy = current_energy + increase_by
            else:
                print("Incorrect. You miss your chance")

        return current_energy
    def trigger_death(self, current_energy,increase_by):
        rng = random.randint(1, 3)
        print("You triggered a sudden death. If you answer wrong, the game will be over")
        if rng == 1:
            print("A cute fuzzy animal comes up to you. Do you touch it or not. Y/N")
            answer = input()
            if answer.upper() == "Y":
                print("You got brutally murdered by the animal. Game over")
                current_energy = 0
            else:
                print("The cute animal turns out to be a poisonous. You are lucky")
        if rng == 2:
            print("You found the game developers. Do you want to die? Y/N")
            answer = input()
            if answer.upper() == "N":
                print("You got brutally murdered . Game over")
                current_energy = 0
            else:
                print("The game developers blessed you with: ",increase_by," energy")
                current_energy=current_energy+increase_by
        if rng == 3:
            print("Say the alphabet backward in LOWER CASE and NO space between them")
            answer = input()
            if answer == "zyxwvutsrqponmlkjihgfedcba":
                print("Correct! Your energy just got double !!")
                current_energy = current_energy*2
            else:
                print("Incorrect. Game over")
                current_energy = 0
        return current_energy

    def trigger_rock_paper_scissor(self, current_energy, increase_by):
        print("In this event, you have to play a game of rock, paper, scissor")
        print("Please choose what you would like to play. R for rock. P for paper. Anything else for scissor")
        answer=input();

        #Assign hand for user
        if answer.upper() == "R":
            user = "Rock"
        elif answer.upper() == "P":
            user = "Paper"
        else:
            user = "Scissor"

        #Assign hand for computer
        rng = random.randint(1, 3)
        if rng == 1:
            computer= "Rock"
        if rng == 2:
            computer = "Paper"
        if rng == 3:
            computer = "Scissor"

         #Compare the result
        if user =="Rock":
            if computer == "Rock":
                print("It's a draw but you still get energy for your effort")
                current_energy = current_energy+increase_by
            elif computer == "Paper":
                print("You played Rock and the computer played Paper. You lose ")
            else:
                print("You played Rock and the computer played Scissor. You win")
                current_energy = current_energy + increase_by

        elif user == "Paper":
            if computer == "Paper":
                print("It's a draw but you still get energy for your effort")
                current_energy=current_energy+increase_by
            elif computer =="Rock":
                print("You played Paper and the computer played Rock. You win !!")
                current_energy = current_energy + increase_by
            else:
                print("You played Paper and the computer played Scissor. You lose")


        if user == "Scissor":
            if computer == "Scissor":
                print("It's a draw but you still get energy for your effort")
                current_energy=current_energy+increase_by
            elif computer =="Paper":
                print("You played Scissor and the computer played Paper. You win !!")
                current_energy = current_energy + increase_by
            else:
                print("You played Scissor and the computer played Rock. You lose")
        return current_energy




def main():
    Energy1 = Energy("Event")
    current_energy =50
    increase_by =15
    current_energy=Energy1.trigger_rock_paper_scissor(current_energy, increase_by)
    print("Your current energy is: ",current_energy)
    if current_energy == 0:
        print("You're dead")
if __name__ =="__main__":
    main()