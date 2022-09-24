# search an entire list for an element the regular way

myList = [1, 2, 3, 4, 5, 6]

def search(list, element):
    for i in range(len(list)):
        if list[i] == element:
            print(i)
    
    print("Element not in list.")
            
search(myList, 8)
            