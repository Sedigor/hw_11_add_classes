from collections import UserDict
from datetime import datetime


class Field:
    pass
        

class Name:
    def __init__(self, name):
        self.value = name


class Phone:
    def __init__(self, phone):
        self.value = phone
        
    @property
    def value(self):
        return self.value
    
    @value.setter
    def value(self, new_value):
        try:
            _ = int(new_value)
            self.value = new_value
        except ValueError:
            return "Wrong type of phone number. Phone number mast have only integers"
        
        
class Birthday:
    def __init__(self, value):
        self.day = value
    
    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, birthday):
        if self._is_valid_birthday(birthday):
            self.value = birthday
        else:
            raise ValueError("Wrong birthday date format. Try again in format dd/mm/yyyy")
        
    def _is_valid_birthday(self, birthday):
        try:
            day, month, year = map(int, birthday.split('/'))
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
            
    def days_to_birthday(self, birthday):
        if birthday:
            pass
            

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}
        
    def add_record(self, record):
        self.data[record.name.value] = record
        
        
if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')