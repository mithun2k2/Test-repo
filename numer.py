# name = "Mithun"
# age = 36

# print(f"Hello {name}, you are {age} years old.")
# print("Hello {}, You are {} years old.". format(name, age))
num = 5
num += 5
# print(num, end = "-")
# print("Jack")

# names = ["Jack", "Jill", "Jane", "John"]
# for i in range (len(names)): 
#     print(i, names[i], sep=": ")

# for i, name in enumerate(names, 1): # ((0, "Jack"), (1, "Jill"), (2, "Jane"), (3, "John"))
#     print(i, name, sep=": ")

my_str = "Welcome to the open class!"
print(my_str[::-1])

words_to_remove = ["to", "Open"]
our_str = "welcome to the open class!"
split_str = our_str.split()
for word in words_to_remove:
    split_str.remove(word)
our_str = " ".join(split_str)
print(our_str)