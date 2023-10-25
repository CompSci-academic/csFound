# Hashing strings using the hash() function
string1 = "apple"
string2 = "banana"

hash_value1 = hash(string1)
hash_value2 = hash(string2)

print(f"Hash of '{string1}': {hash_value1}")
print(f"Hash of '{string2}': {hash_value2}")

# Hash collisions
collision_string = "orange"

hash_value_collision = hash(collision_string)

print(f"Hash of '{collision_string}': {hash_value_collision}")

# Hashing integers
integer1 = 42
integer2 = 100

hash_value_int1 = hash(integer1)
hash_value_int2 = hash(integer2)

print(f"Hash of {integer1}: {hash_value_int1}")
print(f"Hash of {integer2}: {hash_value_int2}")
