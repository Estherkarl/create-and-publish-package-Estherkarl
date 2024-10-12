from calculations.addition import sum_operation as a
from calculations.substraction import minus_operation as s
from calculations.multiplication import multiply_operation as m
from calculations.division import divide_operation as d

if __name__ == "__main__":
    result_addition = a(5, 3)
    result_subtraction = s(5, 3)
    result_multiplication = m(5, 3)
    result_division = d(5, 3)

    print(f"Result of addition is {result_addition}")
    print(f"Result of subtraction is {result_subtraction}")
    print(f"Result of multiplication is {result_multiplication}")
    print(f"Result of division is {result_division}")
