#Built off class_def.py
#Adding author, pages and price to class

class Book:
  def __init__(self, title,author,pages,price):
    self.title = title
    self.author = author
    self.pages = pages
    self.price = price
    self.__secret = "Secret"
    
  #create instance methods
  def getprice(self):
    if hasattr(self, "_discount"):
      return self.price - (self.price * self._discount)
    else:
      return self.price
    return self.price
    
  def setdiscount(self, amount):
    self._discount = amount
    
#Create instances

b1 = Book("Harry Potter","JK Rowling", 300, 20.00)

#Use instances
print(b1.getprice()) #print a price

print(b1.getprice())
b1.setdiscount(.25)
print(b1.getprice())

print(b1._Book__secret)