# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("instructions", "-")

    print('''
To use this program simply enter an integer between 1 and 200. 
The program will show the factors of your chosen integer.

It will also tell you if your chosen number...
- is a prime number (ie: it has two factors)
- is a perfect square

To exit the program, please type 'xxx".
    ''')


# Ask user for an integer between 1 and 200
def num_check(question):
    error = "please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = int(response)

            # check that the number is more than zero
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def factor(var_to_factor):
    factors_list = []
    # to_factor = num_check("To factor: ")

    # square root the number to work out when to stop looping.
    stop = var_to_factor ** 0.5
    stop = int(stop)

    for item in range(1, stop + 1):

        # check to see if the item is a factor
        if to_factor % item == 0:
            factors_list.append(item)

            # calculate partner
            partner = to_factor // item

            # add partner to the list (but prevent duplicates)
            if partner not in factors_list:
                factors_list.append(partner)

    # return sorted list
    factors_list.sort()
    return factors_list


# Main Routine Goes Here

statement_generator("The Ultimate Factor Finder", "-")

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue")

if want_instructions == "":
    instructions()

while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break
