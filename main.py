
from power_digit_addition import PowerNumDigitsAddition

if __name__ == '__main__':
    PowerNumDigitsAddition_obj = PowerNumDigitsAddition()
    base_number = int(input("Please enter Base Number\n"))
    exponent_number = int(input("Please enter Exponent Number\n"))
    print("\nYou have entered expression:\tpow({}, {})".format(base_number, exponent_number))
    first_result = PowerNumDigitsAddition_obj.solve_expression(base_number, exponent_number)
    print("Result of given expression is:\t{}".format(first_result))
    second_result = PowerNumDigitsAddition_obj.digit_addition(first_result)
    print("Addition of digits of a number {} is {}".format(first_result, second_result))
