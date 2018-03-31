types_of_people= 10
# create a variable to store a string. The string accesses a previously created variable and displays its value
x=f"There are {types_of_people}types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"
print(x)
print(y)
print(f" I said : {x}")
print(f"I also said :{y} ")
hilarious = False
joke_evalution = "Isn't that joke so funny?!{}"
#pass hilarious into the empty parameter of joke_evalution
print(joke_evalution.format(hilarious))
w = "This is the left side..."
e="This is right side."
print(w+e)
