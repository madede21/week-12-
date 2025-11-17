# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)

# coolextions are used to store multiple items in a single variable 
# lists are ordered collections of items
# lists are mutable, meaning you can changetheir context
# lists are created using square bractes []

list_of_fruit = ["apple", "banana", "cherry", "date"]
print(list_of_fruit)
print(type(list_of_fruit))

# accesing items in your list

print(list_of_fruit[0])
print(list_of_fruit[2])
print(list_of_fruit[-1])
print(list_of_fruit[1:3])

# reverse the list 
list_of_fruit.reverse()

print(list_of_fruit[::-1])

# appending items to a lists
list_of_fruit.append("alderberry")
print(list_of_fruit)


list_of_fruit.append("mango")
list_of_fruit.append("strawberry")

print(list_of_fruit)

list_of_fruit.extend(["oreos", "my ex"] )
print(list_of_fruit)


list_of_fruit.reverse()

print(list_of_fruit)
# popping items from the list
popped_item = list_of_fruit.pop()

print(popped_item)
print(list_of_fruit)

list_of_fruit.insert(1, "blueberry")
print(list_of_fruit)


# removing items 
list_of_fruit.remove("my ex")
print(list_of_fruit)





# insert
list_of_fruit.insert(3, "banana")
print(list_of_fruit)


list_of_fruit.sort()
print(list_of_fruit)


# Create a list with 5 of your favorite foods.
list_of_items = list(range(1,1001))
print(list_of_items)
print(len(list_of_items))


list_of_items.extend(range(1001,2001))
print(len(list_of_items))
# Print the second and last item.


# Add a new item using .append().


# Remove the first item using .pop(0).


# Reverse your list using .reverse().


# Create a list of 3 lists (matrix), and access the middle element.

