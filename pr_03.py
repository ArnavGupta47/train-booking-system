class train:
    def __init__(self, name, fare, seat):
        self.name=name
        self.fare=fare
        self.seat= seat
        self.l1=[]
        for i in range(1, self.seat+1):
            self.l1.append(i)

    #STATUS OF TRAIN
    def status(self):
        print(f"The train {self.name} has {self.seat} seats available.")
        if self.seat>0:
            print(f"The fare of the train is {self.fare}")
        print("*********")

    #BOOKING A TRAIN
    def bookticket(self):
        if self.seat>0:
            a=max(self.l1)
            print(f"The ticket has been booked. Your seat is at {a}")
            self.seat-=1
            self.l1.remove(a)
            print("*********")

        else:
            print("Sorry, No seats available.")
            print("*********")

    #CANCELING A TICKET
    def cancelticket(self, seat):
        choice1= input("There is a charge for canceling tickets. Are you sure you want to proceed?\n Type (Yes) or (No)")
        choice=choice1.lower()
        if choice=="yes":
            self.l1.append(seat)
            print("The ticket has been cancelled.")
            print("*********")
            self.seat+=1
        else:
            print("No ticket has been cancelled.")
            print("*********")
Train1=train("Rajdjani Express", 1000, 2)
Train1.status()
Train1.bookticket()
Train1.cancelticket(2)
Train1.status()