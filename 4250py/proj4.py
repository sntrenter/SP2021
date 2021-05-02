#Sam Trenter
#4250
#Everything should be working according to the UML diagram, including the polymorphic/overrided functions
class Product:
    def __init__(self,name,price,discountPercent):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent
    def getDiscountAmount(self):
        return self.price - self.price * (1 - self.discountPercent)
    def getDiscountPrice(self):
        return self.price * (1 - self.discountPercent)
    def printDescription(self):
        print("name: ", self.name)
        print("price: ",self.price)
        print("discountPercent: ",self.discountPercent)

test = Product("name",10,.2)
print(test.getDiscountAmount())
print(test.getDiscountPrice())
test.printDescription()

class Book(Product):
    def __init__(self,author,name,price,discountPercent):
        self.author = author
        super().__init__(name,price,discountPercent)
    def printDescription(self):
        print("author: ",self.author)
        print("name: ", self.name)
        print("price: ",self.price)
        print("discountPercent: ",self.discountPercent)

test = Book("auth","title",10,.2)
print(test.getDiscountAmount())
print(test.getDiscountPrice())
test.printDescription()

class Movie(Product):
    def __init__(self,year,name,price,discountPercent):
        self.year = year
        super().__init__(name,price,discountPercent)
    def printDescription(self):
        print("year: ",self.year)
        print("name: ", self.name)
        print("price: ",self.price)
        print("discountPercent: ",self.discountPercent)

test = Movie(2000,"title",10,.2)
print(test.getDiscountAmount())
print(test.getDiscountPrice())
test.printDescription()