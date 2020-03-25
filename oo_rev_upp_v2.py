"""
Script for uppercasing and reversing strings (version 2).

Project: Python Boot Camp
Author: OO

"""

# Using sys package for using cmd line arguments
import argparse


def upp(input_string):
    """Upper case a string."""
    if not isinstance(input_string, str):
        raise Exception("Input must be a string!")

    return input_string.upper()


def rev(input_string):
    """Reverse a string."""
    if not isinstance(input_string, str):
        raise Exception("Input must be a string!")

    return input_string[::-1]


def rev_upp(rev_upp_option, input_string):
    """Reverse or uppercase a string (or both)."""
    output_string = ""

    if not isinstance(input_string, str):
        raise Exception("Input must be a string!")

    output_string = input_string

    # Upper case:
    if rev_upp_option in [1, 3]:
        output_string = upp(output_string)

    # Reverse:
    if rev_upp_option in [2, 3]:
        output_string = rev(output_string)

    return output_string


if __name__ == "__main__":

    PARSER = argparse.ArgumentParser("Reverse and uppercase a string.")
    PARSER.add_argument("rev_upp_optionID",
                        help="Choose: 1 = uppercase, 2 = reverse, 3 = both.",
                        type=int)
    PARSER.add_argument("string", help="String input.")

    ARGS = PARSER.parse_args()

    F_INPUT = ARGS.string
    CHOSEN_OPTION = ARGS.rev_upp_optionID

    OUTPUT_LIST = rev_upp(CHOSEN_OPTION, F_INPUT)
    print(OUTPUT_LIST)
