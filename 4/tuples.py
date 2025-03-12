# 4.6 Tuples homework: create a tuple named "programming classes", with classes in it. loop the program
# to print each class and use the len function to print how many courses there are in the tuple.

programming_classes = ('Intro to Python', 'Advanced Python', 'Database Essentials',
                       'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals')


def main():
    for item in programming_classes:
        print(item)


main()
print(f"This tuple has {len(programming_classes)} courses!")
