from projekty2.number_guessing import Game


class Records:
    def __init__(self):
        self.games={}


    def find_user_with_most_games(self):
        highest=0
        user=""
        for k,v in self.games.items():
            if len(v)>highest:
                highest=len(v)
                user=k

        return user

    def find_user_with_lowest_games(self):
        lowest=0
        user=""
        for k,v in self.games.items():
            if len(v)<lowest:
                lowest=len(v)
                user=k

        return user

    def add_user(self,user):
        if user not in self.games:
            self.games[user]=[]

    def show_records(self):
        for k,v in self.games.items():
            print(k.get_name(),v)
    def posortuj_wg_wieku(self):
        sorted(self.games.items(),key=lambda user:user.get_age())

    def posortuje_wg_imion(self):
        sorted(self.games.items(),key=lambda user:user.get_name())
class Engine:
    def __init__(self):
        self.users=[]
        self.rekordy=Records()
        pass

    def add_user(self,user):
        self.users.append(user)

    def menu(self):
        number=0
        print("1.Założ konto")
        print("2.Zagraj")
        print("3.Pokaz ranking")
        print("4.Wyjdz")

        number=int(input("Wpisz liczbe"))
        return number

    def create_account(self):
        name=input("Wpisz swoje imie: ")
        surname=input("Wpisz swoje nazwisko: ")
        wiek=int(input("Wpisz swoj wiek: "))

        uzytkownik=User(name,surname,wiek)

        self.rekordy.add_user(uzytkownik)
        self.users.append(uzytkownik)

        return uzytkownik
    def get_records(self):
        return self.rekordy


    def show_users(self):
        for index,user in enumerate(self.users):
            print(f"{index}:{user.get_name()}")


    def play(self):
        going=True
        while going:
            number=self.menu()
            if number==1:
                self.create_account()
            elif number==2:

                choicer=True
                while choicer:
                    question=input("Chcesz zagrac istniejacym uzytkownikiem? (y/n)")
                    if question.lower()=='y':
                        self.show_users()
                        gracz=int(input("Wpisz numer jakim graczem chcesz zagrac"))
                        user=self.users[gracz]
                    else:
                        user=self.create_account()

                    game = Game(user)
                    game.start_game()

                    gry = game.get_games()
                    for k, v in self.rekordy.games.items():
                        if k == user:
                            for i in gry:
                                self.rekordy.games[k].append(i)

                    question2=input("Chcesz zagrac ponownie? (y/n)")
                    if question2.lower()=='n':
                        choicer = False
            elif number==3:
                sortowanie=input("Sortowanie wg wieku, czy imion ")
                if sortowanie=="wiek":
                    self.rekordy.posortuj_wg_wieku()
                    self.rekordy.show_records()
                else:
                    self.rekordy.posortuje_wg_imion()
                    self.rekordy.show_records()
            else:
                keep=False

class User:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
    def get_name(self):
        return self.name+" "+self.surname

    def get_initials(self):
        return self.name[0]+"."+self.surname[0]

    def get_age(self):
        return self.age

    def __hash__(self):
        return hash((self.name, self.surname, self.age))

    def __eq__(self, other):
        if isinstance(other, User):
            return (self.name, self.surname, self.age) == (other.name, other.surname, other.age)
        return False

silnik=Engine()

silnik.create_account()

rekordy=silnik.get_records()

rekordy.show_records()

silnik.play()


rekordy.show_records()