import random




class NumberGenerator:
    def __init__(self,mode):

        self.mode=mode



    def generate_random_int_number(self):

        if self.mode==0:
            return random.randint(1,10)
        if self.mode==1:
            return random.randint(1,100)
        if self.mode==2:
            return random.randint(1,500)
        if self.mode==3:
            return random.randint(1,1000)
        if self.mode==4:
            return random.randint(1,10000)

    def generate_random_float_number(self):
        if self.mode==0:
            return random.uniform(1.1,10.0)
        if self.mode==1:
            return random.uniform(1.1,100.0)
        if self.mode==2:
            return random.uniform(1.1,500.0)
        if self.mode==3:
            return random.uniform(1.1,1000.0)
        if self.mode==4:
            return random.uniform(1.1,10000.0)




class Game:
    def __init__(self,user):
        self.user=user
        self.games=[]
        self.level=0
        self.mode=0
        self.tries=0
    def set_difficulty(self):
        print("0.Embrion")
        print("1.Dziecko")
        print("2.Poczatkujacy")
        print("3.Miłosnik wyzwan")
        print("4.Diabeł 😈")
        level=int(input("Wybierz poziom trudnosci"))

        self.level=level
        print("1.Liczby calkowite")
        print("2.Liczb zmiennoprzecinkowe")

        self.mode=int(input("Wybierz tryb"))





    def start_game(self):



        keepGoing=True

        while keepGoing:
            self.set_difficulty()
            generator=NumberGenerator(self.level)

            if self.mode==1:
                random_num=generator.generate_random_int_number()
            elif self.mode==2:
                random_num=generator.generate_random_float_number()

            correct=True

            while correct:
                self.tries+=1
                guess=int(input("Zgadnij liczbe: "))
                if guess==random_num:
                    print(f"Brawo odgadłes za {self.tries} razem")
                    self.games.append(self.tries)
                    correct=False
                elif guess<random_num:
                    print("Liczba za mała")
                else:
                    print("Liczba zbyt duza")

            question=input("Do you want to play again? (y/n):")
            if question.lower()=='n':
                keepGoing=False

    def get_user(self):
        return self.user
    def get_games(self):
        return self.games




