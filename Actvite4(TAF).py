with open("Tabledemultiplication.txt", "w+") as file:
    for i in range(1,10):
        for j in range(1,10):
            file.write(f"{i} x {j} = {i * j}\n")
        file.write("\n")  

