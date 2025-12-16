#! /home/qa/Labs/Labs/PY01/venv/bin/python3
# if __name__ == "__main__":
#     print("Hello World!")

if __name__ == '__main__':
    first_name = input("Enter a first name: ")
    last_name = input("Enter a last name: ")

    print(f"{last_name.upper()}, {first_name.capitalize()}")

    print(last_name.lower().endswith('son'))

    full_name = first_name.lower() + "," + last_name.lower()
    total_vowels = full_name.count('a') + full_name.count('e') + full_name.count('i') + full_name.count('o') + full_name.count('u')
    print(total_vowels)

    print((len(first_name) - len(last_name)) ** 2)

    # full_name = input("Enter a fullname in the format firstname,lastname")
    name_list = full_name.split(',')
    first = name_list[0]
    last = name_list[1]
    print(first)
    print(last)
