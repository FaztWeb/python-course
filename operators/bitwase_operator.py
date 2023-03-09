# bitwase and

x = 18 # 10010
y = 12 # 01100

result = x & y
print(result) # 00000

# bitwase or
result = x | y
print(result) # 11110

# bitwase xor
result = x ^ y
print(result) # 11110

# bitwase not
result = ~x # 01101
print(result) # -19, -10011

# bitwase left shift
result = x << 2 # 10010000
print(result) # 72

# bitwase right shift
result = x >> 2 # 00100
print(result) # 4, 0b100

