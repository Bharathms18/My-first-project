x=['Banglore','Chennai','Delhi']
print("The cities are:",x)
ans=str(input("Do you wish to make any changes?Y/N"))

while ans=='Y':
    print("Menu-")
    print("1)Addition of city in the end.")
    print("2)Addition of city in between.")
    print("3)Modifying the cities.")
    print("4)Deleting a city.")
    print("5)Sorting the cities.")
    print("6)To display the list.")
    choice=int(input("Enter your choice:"))

    if choice == 1:
        a=input("Enter the city to be added:")
        x.append(a)
        print("The new list is:",x)
    elif choice == 2:
        a=str(input("Enter the city to be added:"))
        pos=int(input("Insert the city at which position:"))
        x.insert(pos,a)
        print("The new list is:",x)
    elif choice == 3 :
        pos=int(input("Enter the position of the city you want to modify:"))
        x.remove(x[pos])
        city=str(input("Enter the name of the city you want to replace with:"))
        x.insert(pos,city)
        print(x)    
    elif choice == 4:
        a=str(input("Enter the city to be deleted:"))
        x.remove(a)
        print(x)
    elif choice == 5:
        print("1.Ascending")
        print("2.Descending")
        ch=int(input("Enter your choice:"))
        if ch == 1:
            x.sort(reverse=False)
            print(x)
        else:
            x.sort(reverse=True)
            print(x)
    elif choice == 6:
        print(x)
    ans=str(input("Do you wish to continue?Y/N"))
else:
    print("Thank You!")




print('helllo word')


        

            
