import sys

if __name__ == "__main__":

    def rev_upp(input_strings):
        # Function to reverse and uppercase strings
        # Input must be a single string or a list

        output = []

        # Check if list:
        if type(input_strings) == list:

            for s in input_strings:

                if type(s) == str:

                    # Upper case:
                    uppercased = s.upper()

                    # Reverse:
                    n = len(uppercased)
                    reversed = uppercased[n::-1]

                    output.append(reversed)

                else:
                    print("Input argument has to be a string or a list of strings")
                    break

        elif type(input_strings) == str:

            # Upper case:
            uppercased = input_strings.upper()

            # Reverse:
            n = len(uppercased)
            reversed = uppercased[n::-1]

            output.append(reversed)

        else:
            print("Input argument has to be a string or a list of strings")

        return output

    f_input = sys.argv[1:]

    output = rev_upp(f_input)
    print(output)










