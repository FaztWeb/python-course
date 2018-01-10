def writer(temperatures):
    with open("temps.txt", "w") as file:
        for c in temperatures:
            if c > -273.15:
                f = c * 9 / 5 + 32
                file.write(str(f) + "\n")

temperatures = [10, -20, -289, 100]
writer(temperatures)
