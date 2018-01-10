with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.write("\nLine6")

