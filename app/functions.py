def is_valid_input(value):
    # check if the value is an positive integer
    return isinstance(value, int) and value > 0


def get_valid_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            if is_valid_input(num):
                return num
            else:
                print("Please enter a valid positive integer")
        except ValueError:
            print("Invalid input , please enter a number.")
