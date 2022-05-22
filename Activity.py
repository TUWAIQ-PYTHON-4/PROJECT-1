class Activity:

    def __init__(self, name, start_date, duration, place, capacity,price):
        self._name = name
        self._start_date = start_date
        self._duration = duration
        self._place = place
        self._capacity = capacity
        self._price = price

    
    def get_name(self):
        return self._name

    def set_name(self, n):
        self._name = n

    def get_start_date(self):
        return self._start_date

    def set_start_date(self, sd):
        self._start_date = sd

    def get_duration(self):
        return self._duration

    def set_duration(self, d):
        self._duration = d

    def get_place(self):
        return self._place

    def set_place(self, p):
        self._place= p

    def get_capacity(self):
        return self._capacity

    def set_capacity(self, c):
        self._capacity= c

    def get_price(self):
        return self._price

    def set_price(self, p):
        self._price = p

    def print(self):
        print("\n")
        print("         -Activity Info-       ")
        
        print("{:<15} {:<15} ".format("Name:", self.get_name()))
        print("{:<15} {:<15} ".format("Start date:", self.get_start_date()))
        print("{:<15} {:<15} ".format("Duration:", self.get_duration()))
        print("{:<15} {:<15} ".format("Place:", self.get_place()))
        print("{:<15} {:<15} ".format("Capacity:", self.get_capacity()))
        print("{:<15} {:<15} ".format("Price:", self.get_price()))