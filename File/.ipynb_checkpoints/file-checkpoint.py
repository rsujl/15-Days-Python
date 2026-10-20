
with open("sujal.txt","a+") as fs:
    while True:
        data=input("Enter data in file")
        fs.write(data + "\n")
        fs.seek(0)
        for lines in fs:
            lines.strip()
            if lines.strip().lower().startswith("sujal"):
                print("matching found")
                break
            else:
                print("Not found")
        fs.seek(0)
        fs.truncate(0)
