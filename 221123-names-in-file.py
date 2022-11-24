
lNames = []
file_name = "names.txt"

action = input("(i)nput Name or (l)ist? ")

file = open(file_name,"w")
lines = file.read()
lNames = lines.split()

match action:
    case 'i':
        name = input("Enter name: ")
        if not name in lNames:
            lNames.append(name)
            lNames.sort()
            for name in lNames:
                file.write(name + "\n")

    case 'l':     
        print(lNames)

file.close()