import random
import textwrap

if __name__ == '__main__':
    keep_playing = 'y'
    occupants = ['enemy', 'friend', 'unoccupied']
    width = 72
    dotted_line = '-' * width
    print(dotted_line)
    print("\033[1m" + "Attack of The Orcs v.0.01:" + "\033[0m")

    msg = (
        "The war between humans and their arch enemies, Orcs, was in the"
        "offing. Sir Foo, one of the brave knights guarding the southern "
        "plains began a long journey towards the east trough an unknown "
        "dense forest. On his way, he spotted a small isolated settlement."
        " Tired and hoping to replenish his food stock, he decide to take"
        " a detour. As he approached the village, he saw five huts. There"
        "was not one to be seen around. Hesitantly, he decide to enter.."
    )

    print(textwrap.fill(msg, width=width))
    print("\033[1m" + "Mission:" + "\033[0m")
    print("\tChoose a hut where Sir Foo can rest...")
    print("\033[1m" + "TIP:" + "\033[0em")
    print("Be careful as threre are enemies lurking around")
    print(dotted_line)

random.choice(occupants)
