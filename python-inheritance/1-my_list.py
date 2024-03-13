#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)

if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
