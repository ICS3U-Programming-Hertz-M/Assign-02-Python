#!/usr/bin/env python3
# Created by: Hertz Antonella
# Created on: Mar 29, 2022
# This program asks the user for radius and hieght
# Then displays the surface area and volume in their units
import math


def main():
    # This function ask the user for hieghtand radius
    r = float(input("Enter radius of a cone in (cm) :"))
    h = float(input("Enter height of a cone in (cm) :"))
    
    # This function is calculating surface area and volume
    area =math.pi*r*(math.sqrt (r**2+h**2))
    Volume= 1/3*math.pi*r**2

    # This function display the total of surface area and volume
    print("")
    print("The surface area={:,.2f} cm ".format(area))
    print("The volume ={:,.2f} cm ".format(volume))


if __name__ == "__main__":
    main()
