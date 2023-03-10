# # In this kata, your job is to create a class Dictionary which you can add words to and their entries. Example:
# dictionary = {}
# def new_entry(key, item):
#     global dictionary
#     dictionary[key] = item
#
#
# cont = "Yes"
#
# while True:
#     new_entry(input("Enter a new key"), input("input a new item"))
#     cont = input("Continue? Yes or No: ")
#     if cont == "no".casefold():
#         print(dictionary)
#         break

class Dictionary(object):
    def __init__(self):
        self.my_dict = {}

    def look(self, key):
        try:
            print(self.my_dict[key])
        except KeyError:
            print(f"{key} not found!")


    def new_entry(self, key, value):
        self.my_dict[key] = value



d = Dictionary()

d.new_entry("Yarp", 'yes')
print(d.my_dict)
d.look('narp')
d.new_entry("narp", 'no')
print(d.my_dict)
d.look("narp")
