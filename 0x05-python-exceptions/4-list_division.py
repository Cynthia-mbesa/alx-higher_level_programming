#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]

            if not all(isinstance(val, (int, float)) for
                       val in [dividend, divisor]):
                print("wrong type")
                result.append(0)
            elif divisor == 0:
                print("division by 0")
                result.append(0)
            else:
                result.append(dividend / divisor)
        except IndexError:
            print("out of range")
            result.append(0)
        except Exception:
            result.append(0)
        finally:
            pass
    return (result)
