# emails
emails = [
    'me@hotmail.com',
    'aaron@outlook.com',
    'ryan@gmail.com'
]

# check if email is gmail
for item in emails:
    if 'gmail' in item:
        print(item)

# example temperatures
temperatures=[10,-20,-289,100]

# converto from celsius to fahrenheit function
def c_to_f(c):
    if c > -273.15:
        f=c*9/5+32
        return f
    else:
        return "That temperature doesn't make sense!"

# aply to all temperatures that function
for t in temperatures:
    print(c_to_f(t))
