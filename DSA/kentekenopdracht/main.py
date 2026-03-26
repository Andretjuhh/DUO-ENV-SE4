import LinkedList as ll

x = ["4", "7", "8", "4", "4", "7", "8", "4", "4", "7", "8"]

nummers = ll.LinkedListEmpty()
i = 0
for n in x:
    if i < x.__len__() - 1: 
            print(n)

    nummers = nummers.addFirst(n)
    i += 1
    
print(nummers.toString())