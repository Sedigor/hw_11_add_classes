import json
from fake_users import user_1, user_2

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
            raise ValueError("Wrong birthday date format. Try again in format yyyy-mm-dd")
        
    def _is_valid_birthday(self, birthday):
        try:
            year, month, day = map(int, birthday.split('-'))
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
        _, month, day = map(int, user_birthday.split('-'))
        next_birthday = datetime.date(today.year, month, day)

        if next_birthday < today:
            next_birthday = datetime.date(today.year + 1, month, day)

        days_left = (next_birthday - today).days
        return days_left
            
        
class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def iterator(self, n):
        records = list(self.data.values())
        num_records = len(records)
        start_index = 0

        while start_index < num_records:
            end_index = start_index + n
            yield records[start_index:end_index]
            start_index = end_index
            
    def find(self, sample):
        result = {}
        for k, v in self.data.items():
            name = v.name.value
            phones = ", ".join([p.value for p in v.phones])
            birthday = v.birthday.value
            
            if name.find(sample) > -1 or phones.find(sample) > -1 or birthday.find(sample) > -1:
                contact = {k: v}
                result.update(contact)
        
        if not result:
            return "No match"
        
        return result
            
            
if __name__ == '__main__':
    
    name_1 = Name(user_1["name"])
    phone_1 = Phone(user_1["phone"])
    birthday_1 = Birthday(user_1["birthday"])
    
    name_2 = Name(user_2["name"])
    phone_2 = Phone(user_2["phone"])
    birthday_2 = Birthday(user_2["birthday"])
    
    record_1 = Record(name_1, phone_1, birthday_1)
    record_2 = Record(name_2, phone_2, birthday_2)
    
    ab = AddressBook()
    ab.add_record(record_1)
    ab.add_record(record_2)
    
    sample_1 = user_1["name"][1: 3]
    sample_2 = user_2["phone"][5: 8]
    
    print(ab.find(sample_1))
    print(ab.find(sample_2))