# 4.2 madlibs homework: create a song or functions that takes in names, adjectives and other parameters
# at least 8 parameters.

def madlibs(name1, name2, adj1, adj2, animal1, animal2, place, noun):
    print(f"As {name1} led the party through the dimly lit dungeon, ")
    print(f"They suddenly heard a high-pitched screech coming from behind them.")
    print(
        f"All of a sudden, they hear rumbling, and shortly after see a horde of {adj1} {animal1}s!")
    print(
        f"'Move closer to me!' yelled {name2}, 'im going to cast a protection spell!'")
    print(
        f"As the spell was being cast, {name2}'s {noun} wand was suddenly struck by a {animal1}")
    print(f"'No!' yelled {name2} as their {noun} wand fell to the floor")
    print(f"However, the spell was cast, but it wasn't something the party expected...")
    print(
        f"As the horde of {adj1} {animal1}s continued to rush through the tight corridor,")
    print(
        f"The party laid on the ground, trampled by the horde of {animal1}s,")
    print(f"'Where is {name1}??' asked {name2}, as the party looked around.")
    print(
        f"They saw a abnormally large {adj2} rubber duck on the dungeon floor, where {name1} was last seen.")
    print(f"'I think your spell turned {name1} into a {adj2} rubber duck!' ")
    print(f"'Whoops!' said {name2} 'Im sorry!'")
    print(
        f"'This is like that time I turned that {animal2} into a paperclip at {place} last week'")
    print(f"'I thought you did that at Walgreens?' quacked {name1}")
    print(f"'I would rather not be reminded of that, but that was the employee.'")
    print(f"'That's why we went on this adventure! I need money for the lawsuit!'")
    print(
        f"'Dammit I told you not to bring it up! You ruined the vibe!' screamed {name2}")
    print(f"'My bad. but you did turn me into a rubber duck' quacked {name1}")


input_name1 = input("Enter a name: ")
input_name2 = input("Enter another name: ")
input_adj1 = input("Enter an adjective: ")
input_adj2 = input("Enter another adjective: ")
input_animal1 = input("Enter an animal: ")
input_animal2 = input("Enter another animal: ")
input_place = input("Enter a place: ")
input_noun = input("Enter a noun: ")


madlibs(name1=input_name1, name2=input_name2, adj1=input_adj1, adj2=input_adj2,
        animal1=input_animal1, animal2=input_animal2, place=input_place, noun=input_noun)
