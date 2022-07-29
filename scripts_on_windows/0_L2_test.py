import random

L2_ETH_value = 0.14
pre_input_value = float(L2_ETH_value) - 0.009
point = random.randint(3, 4)  # 小数点最起码要有3位，不然会被向上取整，导致 orb 无法交易
input_value = round(pre_input_value, point)
print(input_value)