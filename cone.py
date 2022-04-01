#!/usr/bin/env python3
# Created by: Hertz Antonella
# Created on: Mar 29, 2022
# This program asks the user for radius and height
# Then displays the surface area and volume in their units
import math


def main():
    # This function ask the user for hieght and radius
    r = float(input("Enter radius of a cone in (cm) :"))
    h = float(input("Enter height of a cone in (cm) :"))

    # This function is calculating surface area and volume
    area = math.pi*r*(math.sqrt(r**2+h**2))
    Volume = 1/3*math.pi*r**2*h

    # This function display the total of surface area and volume
    print("")
    print("\033[1;33mThe surface area={:,.2f} cm^2 ".format(area))
    print("\033[0;34mThe volume ={:,.2f} cm^3 ".format(Volume))


if __name__ == "__main__":
    main()
