from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value=None):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value  
    
        
class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)
        
    @property
    def value(self):
        return self.value
    
    @Field.value.setter
    def value(self, new_value):
        if self._is_valid_phone(new_value):
            self._value = new_value
        else:
            raise ValueError("Invalid phone number")
        
    def _is_valid_phone(phone):
        try:
            _ = int(phone)
            return True
        except ValueError:
            return False
        
        
class Birthday(Field):
    def __init__(self, birthday):
        super().__init__(birthday)
    
    @Field.value.setter
    def value(self, birthday):
        if self._is_valid_birthday(birthday):
            self.value = birthday
        else:
            raise ValueError("Wrong birthday date format. Try again in format dd.mm.yyyy")
        
    def _is_valid_birthday(self, birthday):
        try:
            day, month, year = map(int, birthday.split('.'))
            if day < 1 or day > 31 or month < 1 or month > 12 or len(year) != 4:
                return False
        except ValueError:
            return False

        return True
        
        
    
class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = name
        self.phones = []
        self.add_phone(phone)
        self.birthday = birthday

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break
            
    def days_to_birthday(self):
        today = datetime.date.today()
        user_birthday = self.birthday.value
        day, month, year = map(int, user_birthday.split('.'))
        next_birthday = datetime.date(today.year, month, day)

        if next_birthday < today:
            next_birthday = datetime.date(today.year + 1, month, day)

        days_left = (next_birthday - today).days
        return days_left
            

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}
        self.current_index = 0
        
    def add_record(self, record):
        self.data[record.name.value] = record
        
    def __iter__(self):
        return self.iterator()

    def __next__(self):
        if self.current_index >= len(self.entries):
            raise StopIteration

        entry = self.entries[self.current_index]
        self.current_index += 1
        return entry
        
    def iterator(self, n):
        
        
        