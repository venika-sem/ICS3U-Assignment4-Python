#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: Nov 2022
# This program tells user what polygon it is based on side


def main():
    # this function tells user what polygon it is based on side

    # input
    side_as_string = input("Enter a number of sides: ")
    print("")

    # process & output
    try:
        side_as_number = int(side_as_string)
        # process & output
        match side_as_number:
            case 3:
                print("A polygon with {0} sides is a triangle.".format(side_as_number))
            case 4:
                print("A polygon with {0} sides is a quadrilateral.".format(side_as_number))
            case 5:
                print("A polygon with {0} sides is a pentagon.".format(side_as_number))
            case 6:
                print("A polygon with {0} sides is a hexagon.".format(side_as_number))
            case 7:
                print("A polygon with {0} sides is a heptagon.".format(side_as_number))
            case 8:
                print("A polygon with {0} sides is a octagon.".format(side_as_number))
            case 9:
                print("A polygon with {0} sides is a nonagon.".format(side_as_number))
            case 10:
                print("A polygon with {0} sides is a decagon.".format(side_as_number))
            case _:
                print("Invalid input, sides must ONLY be between 3 and 10!")
    except ValueError:
        print("{0} is not a valid input".format(side_as_string))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
