class Reservation:
    

    def __init__(self, name, activity, phone, number_tickets, totalPrice):
        self._customer_name = name
        self._activity = activity
        self._phone = phone
        self._number_tickets = number_tickets
        self._totalPrice = totalPrice


    #getter & setter
    def get_name(self):
        return self._customer_name

    def set_name(self, n):
        self._customer_name = n

    def get_activity(self):
        return self._activity

    def set_activity(self, a):
        self._activity = a

    def get_phone(self):
        return self._phone

    def set_phone(self, p):
        self._phone = p

    def get_number_tickets(self):
        return self._number_tickets

    def set_number_tickets(self, n):
        self._number_tickets = n

    def get_totalPrice(self):
        return self._totalPrice

    def set_totalPrice(self, p):
        self._totalPrice = p

    def print(self):
        print("{:<20} {:<15} ".format("Name:", self.get_name()))
        print("{:<20} {:<15} ".format("Activity name:", self.get_activity().get_name()))
        print("{:<20} {:<15} ".format("Phone number:", self.get_phone()))
        print("{:<20} {:<15} ".format("Number of tickets:", self.get_number_tickets()))
        print("{:<20} {:<15} ".format("Total price:", self.get_totalPrice()))