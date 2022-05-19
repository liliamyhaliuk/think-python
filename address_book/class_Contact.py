"""
Module that contains classes of the programm "address book".
"""
class Contact:
    """ The Class represents the contact from the address-book."""

    def __init__(self, name = 'Undefined',  email='', address='', phone_number=''):
        self.name = name
        self.email = email
        self.address = address
        self.phone_number = phone_number
  
    def __str__(self):
        return f"{self.name} - email: {self.email}, address: {self.address}, phone number: {self.phone_number}"
