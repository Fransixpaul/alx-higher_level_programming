#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
                
            try:
                dividend = float(my_list_1[i])
                divisor = float(my_list_2[i])
                if divisor == 0:
                    raise ZeroDivisionError("division by 0")
                result.append(dividend / divisor)
            except ValueError:
                print("wrong type")
                result.append(0)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
        except IndexError as e:
            print(e)
            result.append(0)
        finally:
            pass
    return result
