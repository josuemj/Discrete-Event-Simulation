#Basics simpy

def generator(n):
    while True:
        for i in range(n):
            yield i #Pretty much this stops the loop

def function(n):
    for j in range(n):
        return j

my_generator = generator(3)

for i in range(1):
    print(i)
