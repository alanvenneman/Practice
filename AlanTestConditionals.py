# Script: TestConditionals.py
# Author: Alan Venneman
# Date: December 17, 2018
# Purpose: Prompts for an input and output datum and suggests a datum tranformation.
# Inputs: strInputDatum, strOutputDatum
# Outputs: Datum transformation method
##################################################
from past.builtins import raw_input

print("-" * 40)

# Prompt the user for input and output datums
strInputDatum = raw_input("Input Datum?")
strOutputDatum = raw_input("Output Datum?")
print(f"Transformation: {strInputDatum} to {strOutputDatum} ")
# Evaluate the input and print messages to the user
if strInputDatum == "" or strOutputDatum == "":
    print("You didn't enter two datums")
elif len(strInputDatum.split()) > 1 or len(strOutputDatum.split()) > 1:
    print("You need to use the one-word abbreviation for the datum")
elif strInputDatum.upper()== "NAD27":
    if strOutputDatum.upper() == "NAD83":
        print("Please use the NAD_1927_to_1983_NADCON")
    elif strOutputDatum.upper() == "WGS84":
        print("Please use the NAD_1927_to_WGS_1984_79_CONUS")
    elif strOutputDatum.upper() == strInputDatum.upper():
        print("There is no need for a transformation")
    else:
        print("This script doesn't work with the output datum")
else:
    print("This script doesn't work with the input datum!")
# Delete the variables
del strInputDatum, strOutputDatum                                                                                                                             
