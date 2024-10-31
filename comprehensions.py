integer = [0, 1, 2, 3, 4]
binary = ["0", '1', '10', '11', '100']

binary_dict = {(k, v) for (k,v) in zip(integer, binary)}
print(binary_dict)

def additive_inverse_list(int_list):
    return [-i for i in int_list]

# Example usage
original_list = [1, -2, 3, -4, 5]
inverse_list = additive_inverse_list(original_list)
print("Original List:", original_list)
print("Additive Inverse List:", inverse_list)

integer = [1, -1, 2, -2, 3, -3]
squre_int = {i*i for i in integer}
print(squre_int)