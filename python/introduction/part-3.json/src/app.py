import os.path
import csv
import json

class Customer:
  def __init__(self, c="",f="",l=""):
    self.customerID = c
    self.firstName  = f
    self.lastName   = l
  def fullName(self):
    return f"{self.firstName} {self.lastName}"

def getCustomers():
  if not os.path.isfile("customers.json"):
    return {}
  with open('customers.json', newline='') as customerFile:
    data = customerFile.read()
    return json.loads(data)

def getCustomer(customerID):
  customer = getCustomers()
  return customer[customerID]

def updateCustomers(customers):
  with open('customers.json', 'w', newline='') as customerFile:
    customerJSON = json.dumps(customers)
    customerFile.write(customerJSON)
    
customers = {
    "a": Customer("a","James", "Baker"),
    "b": Customer("b", "Jonathan", "D"),
    "c": Customer("c", "Aleem", "Janmohamed"),
    "d": Customer("d", "Ivo", "Galic"),
    "e": Customer("e", "Joel", "Griffiths"),
    "f": Customer("f", "Michael", "Spinks"),
    "g": Customer("g", "Victor", "Savkov"),
    "h" : Customer("h", "Marcel", "Dempers")
}

customerDict = {id: customers[id].__dict__ for id in customers}
updateCustomers(customerDict)

customers = getCustomers()
customers["i"] = Customer("i", "Bob", "Smith").__dict__

updateCustomers(customers)
print(customers)