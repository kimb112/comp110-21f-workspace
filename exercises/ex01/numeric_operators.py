"""Numeric Operators (exponents, decimal division, floor division, modulus) for EX01"""

__author__ = 730481343

left_number_input: str = input("Left-hand side: ")
right_number_input: str = input("Right-hand side: ")

left_number: int = int(left_number_input)
right_number: int = int(right_number_input)

exponent_value: int = left_number ** right_number
decimal_division_value: float = left_number / right_number
floor_division_value: int = left_number // right_number
modulus_value: int = left_number % right_number

exponent_value_string: str = str(exponent_value)
decimal_division_value_string: str = str(decimal_division_value)
floor_division_value_string: str = str(floor_division_value)
modulus_value_string: str = str(modulus_value)


exponent_string: str = " ** "
decimal_division_string: str = " / "
floor_division_string: str = " // "
modulus_string: str = " % "

is_statement_string: str = " is "

print(left_number_input + exponent_string + right_number_input + is_statement_string + exponent_value_string)
print(left_number_input + decimal_division_string + right_number_input + is_statement_string + decimal_division_value_string)
print(left_number_input + floor_division_string + right_number_input + is_statement_string + floor_division_value_string)
print(left_number_input + modulus_string + right_number_input + is_statement_string + modulus_value_string)