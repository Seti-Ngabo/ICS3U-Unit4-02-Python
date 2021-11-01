#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Oct 2021
# This program uses a while loop
#   with user input


def main():
    # this function uses a while loop
    loop_counter = 1
    total = 1

    # input
    user_number_as_string = input("Enter a positive integer: ")
    print("")

    # process & output
    try:
        user_number_as_integer = int(user_number_as_string)
        if user_number_as_integer < 0:
            print("You entered a negative integer, try again.")
        else:
            while loop_counter < user_number_as_integer:
                loop_counter = loop_counter + 1
                total = total * loop_counter
            print("{0}! = {1}".format(user_number_as_string, total))

    except Exception:
        print("Invalid input, try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
