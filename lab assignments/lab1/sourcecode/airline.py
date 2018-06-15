# created a class representing book
class Book():
    def make_reservation111(self, **kwargsns):
        raise NotImplementedError
    def spam(self):
        print(1)
class time(Book):
    def spam(self):
        print(2)
        super().spam()
# using inheritnace class 'Air' acquiring the properties of class 'Book'
class Air(Book):

    # defining the types of booking
    CLASS_BUS = 'Business Class'
    CLASS_FT = 'First Class'
    CLASS_PREMIUM_EC = 'Premium Economy'
    CLASS_Emy = 'Regular Economy'

    # defining a default constructor
    def __init__(self, air_name):

        # calling the super class constructor
        super(Air, self).__init__()
        self.air_name= air_name

        # assigning no. of seats to each class
        self.seats = {
            self.CLASS_BUS: 50,
            self.CLASS_FT: 50,
            self.CLASS_PREMIUM_EC: 100,
            self.__CLASS_Emy: 150,#is private
        }

        # assigning the prices to each class
        self.prices = {
            self.CLASS_BUS: 2500,
            self.CLASS_FT: 2000,
            self.CLASS_PREMIUM_EC: 1800,
            self.CLASS_Emy: 1500,
        }

    # creating a function to check whether the no. of seats are greater than 0
    def is_ava(self, booking_class):
        return self.seats[booking_class] > 0

    def make_res(self, booking_class):
        if self.is_ava(booking_class):
            self.seats[booking_class] -= 1

    # finally it prints the no. of seats left and the price of that particular selected booking
    def show(self,booking_class):
            print(booking_class,"seats left:",self.seats[booking_class],"prices:",self.prices[booking_class])

airline = Air("Quantas")

# selecting the choice of booking out of 4
s=input("enter which type of booking : ")

# assigning the input to the booking class
booking_class = str(s)

# calling this function to print the no.of seats left and to know the prices
airline.show(booking_class)