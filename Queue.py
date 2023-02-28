myQueue = []

while True:
    print("a to add, r to remover")
    s = input("Introduce: ")
    

    if s == "a":
        element = input("Introduce adding element")
        myQueue.append(element)
    
    elif s == "r":
        print("Removing element")
        myQueue.pop(0)



    print(myQueue)
