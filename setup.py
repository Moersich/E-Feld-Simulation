WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

num_of_rows = 40
num_of_cols = 40

# q = 1 * 10 ** (-6)
epsilon_1 = 1


def charge_value():
    charge_val_as_string = input("Enter a value for charge: ")
    charge_as_float = float(charge_val_as_string)
    return charge_as_float


charge = charge_value()
