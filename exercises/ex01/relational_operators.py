"""Using relational operators (less than, greater than or equal, equal to, not equal to) to test the relationship between two numbers input by user."""

__author__ = "730481343"

left_number_input: str = input("Left-hand side: ")
right_number_input: str = input("Right-hand side: ")

left_number: int = int(left_number_input)
right_number: int = int(right_number_input)

less_than_value: bool = left_number < right_number
greater_than_or_equal_value: bool = left_number >= right_number
equal_to_value: bool = left_number == right_number
not_equal_to_value: bool = left_number != right_number

less_than_string: str = " < "
greater_than_or_equal_string: str = " >= "
equal_to_string: str = " == "
not_equal_to_string: str = " != "

less_than_value_string: str = str(less_than_value)
greater_than_or_equal_value_string: str = str(greater_than_or_equal_value)
equal_to_value_string: str = str(equal_to_value)
not_equal_to_value_string: str = str(not_equal_to_value)

is_statement_string: str = " is "

print(left_number_input + less_than_string + right_number_input + is_statement_string + less_than_value_string)
print(left_number_input + greater_than_or_equal_string + right_number_input + is_statement_string + greater_than_or_equal_value_string)
print(left_number_input + equal_to_string + right_number_input + is_statement_string + equal_to_value_string)
print(left_number_input + not_equal_to_string + right_number_input + is_statement_string + not_equal_to_value_string)