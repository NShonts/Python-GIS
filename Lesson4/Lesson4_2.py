userName = ""
name_list = []

while userName != "":
    userName = input("Pleas enter a name (Leave blank and click Enter to quit): ")
    if userName != "":
        name_list.append(userName)
print(name_list)
sorted_list = sorted(name_list)
print(sorted_list)
