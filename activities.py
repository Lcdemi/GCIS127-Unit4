import random

def tuples(a_tuple):
    print(len(a_tuple))
    print(a_tuple)
    for element in a_tuple:
        print(element)

def scale(a_list, scalar):
    for element in range(len(a_list)):
        a_list[element] *= scalar
    return a_list

def cat(a_list, b_list):
    return a_list + b_list

def extender(a_list, b_list):
    a_list + b_list
    return a_list

def inserter(a_list, value):
    middle_index = len(a_list) // 2
    a_list.insert(middle_index, value)

def popper(a_list):
    if len(a_list) == 0:
        return
    else:
        index = random.randrange(len(a_list))
        value = a_list.pop(index)
        print(a_list, value)
        popper(a_list)

def swapper(a_list):
    half_index = len(a_list) // 2
    left_list = a_list[:half_index]
    right_list = a_list[half_index:]
    return right_list + left_list

def comprehension():
    print([letters for letters in "foobar"])
    print([0 for _ in range(15)])
    print([nums for nums in range(13)])
    print([even for even in range(21) if even % 2 == 0])
    print([integer for integer in range(51) if integer % 5 == 0 or integer % 3 == 0])

def make_table(rows, columns, value):
    table = []
    for row in range(rows):
        row = []
        for col in range(columns):
            row.append(value)
        table.append(row)
    return table

def sevens_key(number):
    number = str(number)
    if number[0] == "7":
        return 0
    else:
        return 9
    
def lucky_7s(a_list):
    print(a_list)
    a_list.sort(key=sevens_key)
    print(a_list)

    
def main():
    #tuples((1, 2, 3, 4, 5))
    #tuples((6, "U", 5.0))
    #tuples(("?", True, "Sauce"))
    #new_list = [8, 5, 7.0, 6]
    #print(scale(new_list, 3))
    #even_newer_list = [9, 5, 8]
    #newest_list = cat(new_list, even_newer_list)
    #print(new_list)
    #print(even_newer_list)
    #print(newest_list)
    #empty_list = []
    #for i in range(5):
        #inserter(empty_list, i)
        #print(empty_list)
    #popper(empty_list)
    #a_list = [1, 3, 5, 2, 4, 6]
    #b_list = swapper(a_list)
    #print(b_list)
    #comprehension()
    #table = make_table(4, 3, 'b')
    #for row in table:
    #    print(row)
    #print(table)
    #a = [x for x in range(100) if x % 7 == 0]
    #lucky_7s(a)

    count_up(20000)

if __name__ == "__main__":
    main()

    #[10, 3, 5, 6, 1, 4, 8, 7]
    #[3, 5, 6, 1, 4, 8, 7][10]
    #[1, 3, 4, 5, 6, 7, 8][10]
    #[1, 3, 4, 5, 6, 7, 8, 10]