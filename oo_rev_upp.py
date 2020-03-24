"""

Script for uppercasing and reversing strings.

Project: Python Boot Camp
Author: OO

"""

# Using sys package for using cmd line rguments
import sys


def rev_upp(input_strings):
    """Input must be a single string or a list."""
    output_list = []

    # Check if list:
    if isinstance(input_strings, list):

        for input_string in input_strings:

            if isinstance(input_string, str):

                # Upper case:
                uppercased = input_string.upper()

                # Reverse:
                rev = uppercased[::-1]

                output_list.append(rev)

                if input_string == input_strings[-1]:
                    return output_list

            else:
                raise Exception("Input arg must be a list of strings!")

    # Check if string:
    elif isinstance(input_strings, str):

        # Upper case:
        uppercased = input_strings.upper()

        # Reverse:
        rev = uppercased[::-1]

        output_list.append(rev)

        return output_list

    else:
        raise Exception("Input arg must be a string!")


if __name__ == "__main__":

    F_INPUT = sys.argv[1:]

    OUTPUT_LIST = rev_upp(F_INPUT)
    print(OUTPUT_LIST)
