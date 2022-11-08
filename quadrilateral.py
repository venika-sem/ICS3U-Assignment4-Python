#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: Nov 2022
# This program tells the month quadrilateral on the inputted side

import math


def main():
    # this function tells the month quadrilateral on the inputted side

    # input
    month_number = int(input("Enter a number of sides: "))
    print("")

    # process & output
    match month_number:
        case 1:
            print("January")
        case 2:
            print("February")
        case 3:
            print("March")
        case 4:
            print("April")
        case 5:
            print("May")
        case 6:
            print("June")
        case 7:
            print("July")
        case 8:
            print("August")
        case 9:
            print("September")
        case 10:
            print("October")
        case 11:
            print("November")
        case 12:
            print("December")
        case _:
            print("Invalid input, not a month")

    print("\nDone.")


if __name__ == "__main__":
    main()
