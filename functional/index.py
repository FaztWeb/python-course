def lower(elements): return elements.lower()

names = ["JOE", "RYAN", "JENNY"]

print(list(map(lower, names)))

print([name.lower() for name in names])

# HIGH ORDER FUNCTIONS

def greet(idiom):
    def greet_es():
        print("Hola")
    def greet_en():
        print("Hello")
    idiom_func = {
        "es": greet_es,
        "en": greet_en
    }
    return idiom_func[idiom]

mygreet = greet("es")
mygreet()
