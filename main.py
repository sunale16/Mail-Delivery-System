# This is a sample Python script.

# Press Ctrl+Shift+Windows to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from  hashtable import HashTable, Item
from distance import
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

demo = HashTable()
input = {1:"first", 2:"second", 3:"third", 40:"forty"}


for key, value in input.items():
    item = Item(key, value)
    # print(item.key)
    demo.put(item)

print(demo.keys)
print(demo.size)
for i in range(len(demo.table)+4):
    bucket = demo.get_bucket(i)
    # for item in bucket:
    #     print(f"Key: {item.key}, Data: {item.data}")
    print(f"Bucket {i} : {' | '.join([f'Key: {item.key}, Data: {item.data}' for item in bucket])}")

# print(demo.get_bucket(0))

class Main:
    print("Hello, welcome to WGUPS Package Delivery System!")
    print("The current route was copmpleted in 8 hours and 15 minutes.")
    start = input("Please enter a time in HH:MM format: ")

# print(demo)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
