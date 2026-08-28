print("1) Add to file \n2) View all records \n3) Delete a record \n4) Quit program")
#example 2D array of names and salaries
salaries = [["name1", 1000],["name2", 2000],["name3", 3000]]
#add a record
def addRecord(array):
    name = input("Enter your name:")
    salary = int(input("Enter your salary:"))
    array.append([name, salary])
    return array
#delete a record
def deleteRecord(array, name, salary):
    record_index = salaries.index([name, salary])
    #if user has entered a name and salary pair that doesn't exist, an error occurs
    del array[record_index]
    return array
while True:
    choice = int(input("Enter your number of selection:"))
    if choice == 1:
        addRecord(salaries)
    elif choice == 2:
        #view the records
        print(salaries)
    elif choice == 3:
        n = input("Enter the name:")
        s = int(input("Enter the salary"))
        deleteRecord(salaries, n, s)
    elif choice == 4:
        #quit program
        break
    else:
        print("Invalid input")
