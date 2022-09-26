# class MyClass:
#     """A simple example class"""
#     i = 12345
    
#     def f(self):
#         return 'hello world'

# print(MyClass.i) # return the int
# print(MyClass.f) # returns a function object
# print(MyClass.__doc__) # magic method/dunder method that return the text literal

# x = MyClass() #instantiates the class
# print(x.i) # return the int
# print(x.f()) # calls the class method

# class Bookstore:
#     total_books = 0
    
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         Bookstore.total_books += 1

#     def bookInfo(self):
#         print("Book title: ", self.title)
#         print("Book author: ", self.author,"\n")

# book1 = Bookstore("What", "Winny Git")
# book2 = Bookstore("Never", "Hanna Doe")
# book3 = Bookstore("Bang", "Helen Bong")
# book4 = Bookstore("Bing", "Helen Bang")

# book1.bookInfo()
# print(Bookstore.total_books)


# class Student:
#     school = 'freeCodeCamp.org'

#     def __init__(self, name, course):
#         self.name = name
#         self.course = course

# student1 = Student('Jane', 'JS')
# student2 = Student('Ed', 'C')

# print(student1.school, student2.school)

# class Player:
#     game = 'tictactoe'

#     def __init__(self, name, capital):
#         self.name = name
#         self.capital = capital

#     def addCapital(self):
#         while self.capital < 10:
#             self.capital += 1
#             print(self.name, self.capital)
        
# playerA = Player('Anne', 5)
# playerB = Player('Helen', 3)
# playerC = Player('Tom', 2)

# playerA.addCapital()
# playerB.addCapital()
