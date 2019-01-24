#Trung Nguyen prototype for Event
import random
class Event:
    def __init__(self, name):
        self.name=name

class Energy(Event):
    def __init__(self,name):
        super().__init__(name)
    def trigger(self,current_energy,increase_by):
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
        if rng==3:
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
        rng = random.randint(1, 3)
        if rng==1:
            print("In C++, how do you terminate a statement ?")
            answer = input()
            if answer ==';':
                print("Correct. Your energy is increased by: ", increase_by)
                current_energy=current_energy+increase_by
            else:
                print("Incorrect. You miss your chance")
        if rng == 2:
            print("In C++, how do you dereference a pointer ?")
            answer = input()
            if answer == '&':
                print("Correct. Your energy is increased by: ", increase_by)
                current_energy = current_energy + increase_by
            else:
                print("Incorrect. You miss your chance")
        if rng == 3:
            print("In C++, what is the symbol for pointer ?")
            answer = input()
            if answer == '*':
                print("Correct. Your energy is increased by: ", increase_by)
                current_energy = current_energy + increase_by
            else:
                print("Incorrect. You miss your chance")
        return current_energy


def main():
    Energy1 = Energy("Event")
    current_energy =50
    increase_by =15
    current_energy=Energy1.trigger(current_energy, increase_by)
    print("Your current energy is: ",current_energy)
if __name__ =="__main__":
    main()