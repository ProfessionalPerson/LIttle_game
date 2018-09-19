import os

class set_data:
    iscontinue = False
    number = None
    max = None
    min = None
    condition = None

    iscontinue_default = False
    number_default = False
    max_default = False
    min_default = False
    condition_default = False

    first_game = True

    #set/get game data start
    def set_iscontinue(self):
        while 1:
            continueornot = input("Do you want to continue?(y/n)")
            if continueornot == "y":
                self.iscontinue = True
                break
            elif continueornot == "n":
                self.iscontinue = False
                break
            else:
                print("Please input y/n")
                continue

    def set_number(self):
        while 1:
            try:
                self.number = int(input("Please set number:"))
                break
            except ValueError:
                print("Please input int")

    def set_max(self):
        while 1:
            try:
                while 1:
                    self.max = int(input("Please set max scope:"))
                    if self.max > self.number:
                        break
                    else:
                        print("Please input data large than " + str(self.number) + "!")
                        continue
                break
            except ValueError:
                print("Please input int")

    def set_min(self):
        while 1:
            try:
                while 1:
                    self.min = int(input("Please set min scope:"))
                    if self.min < self.number:
                        break
                    else:
                        print("Please input data less " + str(self.number) + "!")
                        continue
                break
            except ValueError:
                print("Please input int")

    def set_condition(self):
        while 1:
            try:
                while 1:
                    self.condition = int(input("Please set failure condition:"))
                    if self.condition > 0:
                        break
                    else:
                        print("Please input data large than 0!")
                        continue
                break
            except ValueError:
                print("Please input int")

    def get_iscontinue(self):
        return self.iscontinue

    def get_number(self):
        return self.number

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def get_condition(self):
        return self.condition
    #set/get game data end

    #set/get/display data default start
    def set_iscontinue_default(self):
        while 1:
            isdefault = input("Do you want to iscontinue default?(y/n)")
            if isdefault == "y":
                self.iscontinue_default = True
                self.set_iscontinue()
                break
            elif isdefault == "n":
                self.iscontinue_default = False
                break
            else:
                print("Please input y/n")
                continue

    def set_number_default(self):
        while 1:
            isdefault = input("Do you want to number default?(y/n)")
            if isdefault == "y":
                self.number_default = True
                self.set_number()
                break
            elif isdefault == "n":
                self.number_default = False
                break
            else:
                print("Please input y/n")
                continue

    def set_max_default(self):
        while 1:
            isdefault = input("Do you want to max default?(y/n)")
            if isdefault == "y":
                self.max_default = True
                self.set_max()
                break
            elif isdefault == "n":
                self.max_default = False
                break
            else:
                print("Please input y/n")
                continue

    def set_min_default(self):
        while 1:
            isdefault = input("Do you want to min default?(y/n)")
            if isdefault == "y":
                self.min_default = True
                self.set_min()
                break
            elif isdefault == "n":
                self.min_default = False
                break
            else:
                print("Please input y/n")
                continue

    def set_condition_default(self):
        while 1:
            isdefault = input("Do you want to condition default?(y/n)")
            if isdefault == "y":
                self.condition_default = True
                self.set_condition()
                break
            elif isdefault == "n":
                self.condition_default = False
                break
            else:
                print("Please input y/n")
                continue

    def get_iscontinue_isdefault(self):
        return self.iscontinue_default

    def get_number_isdefault(self):
        return self.number_default

    def get_max_isdefault(self):
        return self.max_default

    def get_min_isdefault(self):
        return self.min_default

    def get_condition_isdefault(self):
        return self.condition_default

    def set_first_game_False(self):
        self.first_game = False

    def get_first_game(self):
        return self.first_game

    def display_all_data_isdefault(self):
        print("This is default info:")
        print("iscontinue default: " + str(self.get_iscontinue_isdefault()))
        print("number default: " + str(self.get_number_isdefault()))
        print("max default: " + str(self.get_max_isdefault()))
        print("min default: " + str(self.get_min_isdefault()))
        print("condition default: " + str(self.get_condition_isdefault()))

        print("This is game data info:")
        print("iscontinue data: " + str(self.get_iscontinue()))
        print("number data: " + str(self.get_number()))
        print("max data: " + str(self.get_max()))
        print("min data: " + str(self.get_min()))
        print("condition data: " + str(self.get_condition()))
    #set/get/display data default end

    def set_game_data(self):
        if self.get_iscontinue_isdefault() == False and \
                self.get_first_game() == False:
            self.set_iscontinue()

        if self.get_number_isdefault() == False and \
                self.get_iscontinue() == False:
            self.set_number()
        elif self.get_number_isdefault() == False and \
                self.get_first_game() == True:
            self.set_number()

        if self.get_max_isdefault() == False and \
                self.get_iscontinue() == False:
            self.set_max()
        elif self.get_max_isdefault() == False and \
                self.get_first_game() == True:
            self.set_max()

        if self.get_min_isdefault() == False and \
                self.get_iscontinue() == False:
            self.set_min()
        elif self.get_min_isdefault() == False and \
                self.get_first_game() == True:
            self.set_min()

        if self.get_condition_isdefault() == False and \
                self.get_iscontinue() == False:
            self.set_condition()
        elif self.get_condition_isdefault() == False and \
                self.get_first_game() == True:
            self.set_condition()

    def set_data_default(self):
        self.display_all_data_isdefault()
        print("")

        self.set_iscontinue_default()
        self.set_number_default()
        self.set_max_default()
        self.set_min_default()
        self.set_condition_default()

def game_main(number,max,min,condition):
    for item in range(1000):
        print("\n")
    print("Game start now!\n")

    winorfail = False

    #game start
    for frequency in range(condition):
        chances = condition - frequency - 1
        data = int(input("Please input data:"))
        if data >= max:
            print("Please input data less than " + str(max))
            print("You still have " + str(chances) + " chances")
            continue
        elif data <= min:
            print("lease input data large than " + str(min))
            print("You still have " + str(chances) + " chances")
            continue
        elif data > number:
            print("Its too big")
            print("You still have " + str(chances) + " chances")
            continue
        elif data < number:
            print("Its too small")
            print("You still have " + str(chances) + " chances")
            continue
        else:
            winorfail = True
            break
    #game end

    if winorfail == False:
        print("You are fail")
    else:
        print("You are win")

    print("Game over")

    set_data.set_first_game_False()

set_data = set_data()

while 1:
    playornot = input("Do you want to play?(y/s/n)")
    if playornot == "y":
        set_data.set_game_data()
        game_main(set_data.get_number(),set_data.get_max(),
                  set_data.get_min(),set_data.get_condition())
        continue
    elif playornot == "s":
        set_data.set_data_default()
        continue
    elif playornot == "n":
        print("Bye Bye!")
        os._exit()
    else:
        print("Please input y/n")
        continue