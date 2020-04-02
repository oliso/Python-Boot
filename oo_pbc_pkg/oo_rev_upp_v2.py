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


def rev_upp_file(chosen_option, file_input, destination):
    """Reverse or uppercase files, save output."""
    try:
        with open(file_input, "r") as read_txt:
            read_lines = read_txt.readlines()
    except IOError:
        print("Unable to open input file.")
        raise

    output_file_path = os.path.join(destination, "rev_upp_output.txt")

    output_text = ""

    print("Output:")
    print("=========================================================")

    for line in read_lines:
        output_string = rev_upp(chosen_option, line)
        print(output_string)

        try:
            # Write new line into an output txt file using with:
            with open(output_file_path, "a") as write_txt:
                write_txt.write("\n" + output_string)
                output_text += output_string
        except IOError:
            print("Unable to open output file.")
            raise

    print("=========================================================")
    print("The above output has been written into rev_upp_output.txt")
    print("and saved into " + destination)

    return output_text


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
                        help="Custom output file destination path (optional). "
                        + "Uses current working directory by default. ",
                        type=str,
                        nargs='?',
                        default=os.getcwd()
                        )

    ARGS = PARSER.parse_args()
    CHOSEN_OPTION = ARGS.rev_upp_optionID
    FILE_INPUT = ARGS.file_name
    DEST = ARGS.directory

    # Read lines of the file provided using with:
    rev_upp_file(CHOSEN_OPTION, FILE_INPUT, DEST)
