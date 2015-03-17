#Linear Search

def Linear_search(List, search):
    found = False
    counter = 0
    while not found and counter <len(List):
        if List[counter] == search:
            found = True
        else:
            counter += 1
    return found


#main program

List = ["john", "James", "billy", "Ashley"]
search = input("Please enter a name: ")
found = Linear_search(List, search)

if found:
    print("Found")
else:
    print("Not Found")
