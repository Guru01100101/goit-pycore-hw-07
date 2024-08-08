from cli_bot_classes import AddressBook, Record, Phone

book = AddressBook()

john_record = Record('John')
john_record.add_phone('+380992572719')
john_record.add_phone('0552-237-519')

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("0987654321")  # Number must begin with 0 or +380 and have 9 digits after 0
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find('John')

john.edit_phone('0552-237-519', '0552-250-520')

print(john)

found_phone = john.search_phone('0552-250-520')
print(f"{john.name}\n{found_phone}")

book.delete_record('Jane')

print(book)
