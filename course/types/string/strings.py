# python 3
message1 = 'mensaje entre comillas simples'
message2 = "mensaje entre comillas dobles"
message3 = ''' un
		mensaje
		multi
	lineas '''

print(message1)
print(message2)
print(message3)

# to see all string methods
dir(message1)

# to obtain help
help("".replace)

# concatenation
print("hello " + "world")

message4 = "Hello!"
message4[1] #e
message4[-1] #!
message4[0:3] # Hel
message4[1:] # ello!
message4[-3: -1]
message4[-3:] 


# conversion
print(str(5) + str(10)) #"510"
