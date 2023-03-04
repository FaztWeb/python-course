def show_scores(**information):
    print(information) # {'name': 'John', 'age': 25, 'score': 100}
    print(type(information)) # dict
    print("student name:", information["name"])
    print("student score:", information["score"])

show_scores(name="John", score=100)
show_scores(name="Mary", score=90, age=20)

def show_points(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

show_points(name="John", score=100)
show_points(name="Mary", score=90, age=20)
