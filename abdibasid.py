# modules :

# print("hello world")
### loops :


# def multiplier(x, y):
#     num = x * y
#     return num


# def adder(x, y):
#     num = x + y
#     return num


# OOPs:classes and objects :

# abstruction :

# class remoteController:
#     def changeChennel(self, channel):
#         return f"the channel changed into {channel}"

#     def adjustVolume(self, adjust):
#         return f"the volume is adjusted to {adjust}"


# if __name__ == "__main__":

#     remote = remoteController()
#     print(remote.adjustVolume(2))

# Encapsulation:


# class bankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             return f"deposited ${amount}.your new balance is ${self.__balance}"
#         else:
#             return f"invalid deposit"

#     def withdrowal(self, amount):
#         if amount > self.__balance:
#             return f"insufficient balance "

#         elif amount <= 0 or amount == "":
#             return f"invalid input "
#         else:
#             self.__balance -= amount
#             return f"withdrowed ${amount}.the new balance is ${self.__balance}"


# # if __name__ == "__main__":
# bank = bankAccount("abdibasid", 100)
# print(bank._bankAccount__balance)
# print(bank.withdrowal(10))


# inheritance :

class car:
    def __init__(self, company, modal):
        self.company = company
        self.modal = modal

    def start_engine(self):
        return f"{self.company} ,{self.modal} is started"

    def stop_engine(self):
        return f"{self.company},{self.modal} is stopped"


class electricCar(car):
    def __init__(self, company, modal, batteryCapacity):
        super().__init__(company, modal)
        self.batteryCapacity = batteryCapacity

    def charge(self):
        return f"{self.company} ,{self.modal},{self.batteryCapacity}kwh is fully charged "


if __name__ == "__main__":
    Marcedes = car("marcedes", "modal4")
    print(Marcedes.start_engine())

    Tesla = electricCar("Tesla", "Modal_5", 1000)
    print(Tesla.start_engine())

# class Sports:
#     outdoor = True

#     def __init__(self, SportsName, SportsTeam):
#         self.sports_name = SportsName
#         self.sports_team = SportsTeam


# club = Sports("Golf", "America")
# print(club.sports_name)
# print(club.sports_team)
