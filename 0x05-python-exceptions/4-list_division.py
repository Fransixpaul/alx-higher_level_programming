#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            dividend = float(my_list_1[i])  # Convert to float for division
            divisor = float(my_list_2[i])   # Convert to float for division

            if divisor == 0:
                result.append(0)  # Handle division by zero
                print("division by 0")
            else:
                division_result = dividend / divisor
                result.append(division_result)
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except (ValueError, TypeError):
            result.append(0)
            print("wrong type")
        except IndexError:
            result.append(0)
            print("out of range")
        finally:
            pass  # This block executes whether an exception occurs or not
    return result

