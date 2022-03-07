#!/usr/bin/env python3
# Created by: Ferdous Sediqi
# Created on: March 1st, 2022
# This program asks the user for the diameter of the
# pizza. then, calculates and displays the total cost of the pizza with tax


import constants


def main():
    # input
    
    diameter = int(input("Enter the diameter of the pizza (inches): "))
    
    # clculate
    
    subtotal = constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST * diameter
    tax = constants.HST * subtotal
    total = subtotal + tax
    
    # output the answer
    
    print("")
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
