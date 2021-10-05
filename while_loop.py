#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
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
        while loop_counter < user_number_as_integer:
            loop_counter = loop_counter + 1
            total = total * loop_counter
        print(
            "The multiplication from 1 to {0} is {1}.".format(
                user_number_as_string, total
            )
        )

    except Exception:
        print("Invalid input, try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
