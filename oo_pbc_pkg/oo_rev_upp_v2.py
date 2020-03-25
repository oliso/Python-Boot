"""
Script for uppercasing and reversing lines in files.

Project: Python Boot Camp
Author: OO

"""

# Using argparse package for using cmd line arguments
import argparse
import os


def upp(input_string):
    """Upper case a string."""
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string!")

    return input_string.upper()


def rev(input_string):
    """Reverse a string."""
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string!")

    return input_string[::-1]


def rev_upp(rev_upp_option, input_string):
    """Reverse or uppercase a string (or both)."""
    output_string = ""

    if not isinstance(input_string, str):
        raise TypeError("Input must be a string!")

    output_string = input_string

    # Upper case:
    if rev_upp_option in [1, 3]:
        output_string = upp(output_string)

    # Reverse:
    if rev_upp_option in [2, 3]:
        output_string = rev(output_string)

    return output_string


if __name__ == "__main__":

    # Set up command line argument parser and define required arguments
    PARSER = argparse.ArgumentParser("Reverse and uppercase a string.")
    PARSER.add_argument("rev_upp_optionID",
                        help="Choose: 1 = uppercase, 2 = reverse, 3 = both.",
                        choices=[1, 2, 3],
                        type=int
                        )
    PARSER.add_argument("file_name",
                        help="Path/name of a text file (including extension).",
                        type=str
                        )
    PARSER.add_argument('directory',
                        help="Custom output file destination (optional). "
                        + "Uses current working directory by default. "
                        + "Expected format: Z:\\...\\DestinationFolder",
                        type=str,
                        nargs='?',
                        default=os.getcwd()
                        )

    ARGS = PARSER.parse_args()
    CHOSEN_OPTION = ARGS.rev_upp_optionID
    F_INPUT = ARGS.file_name
    DEST = ARGS.directory

    # Read lines of the file provided using with:
    with open(F_INPUT, "r") as READ_TXT:
        READ_LINES = READ_TXT.readlines()

    OUTPUT_FILE_STRING = DEST + "\\rev_upp_output.txt"

    print("Output:")
    print("=========================================================")

    for line in READ_LINES:
        OUTPUT_STRING = rev_upp(CHOSEN_OPTION, line)
        print(OUTPUT_STRING)

        # Write new line into an output txt file using with:
        with open(OUTPUT_FILE_STRING, "a") as WRITE_TXT:
            NewLine = WRITE_TXT.write("\n" + OUTPUT_STRING)

    print("=========================================================")
    print("The above output has been written into rev_upp_output.txt")
    print("and saved into " + DEST)
