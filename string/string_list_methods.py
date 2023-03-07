# to see all string methods
dir("some string")

# loop all items
# for method in dir(" "):
#   print(method)

methods = []

# list all methods avoiding properties and enumerating items
for method in dir(" "):
    if not method.startswith("_"):
        methods.append(method)

for i, method in enumerate(methods):
    print(f"{i+1}. {method}")
