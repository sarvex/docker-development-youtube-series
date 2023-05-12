class Customer:
  def __init__(self, c="",f="",l=""):
    self.customerID = c
    self.firstName  = f
    self.lastName   = l
  def fullName(self):
    return f"{self.firstName} {self.lastName}"

def getCustomers():
  return {
      "a": Customer("a", "James", "Baker"),
      "b": Customer("b", "Jonathan", "D"),
      "c": Customer("c", "Aleem", "Janmohamed"),
      "d": Customer("d", "Ivo", "Galic"),
      "e": Customer("e", "Joel", "Griffiths"),
      "f": Customer("f", "Michael", "Spinks"),
      "g": Customer("g", "Victor", "Savkov"),
      "h": Customer("h", "Marcel", "Dempers"),
  }

def getCustomer(customerID):
  customer = getCustomers()
  return customer[customerID]


customers = getCustomers()
for customerID in customers:
  print(customers[customerID].fullName())