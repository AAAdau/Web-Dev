def cat_dog(str):
    return str.count('cat') == str.count('dog')

# Test cases
print(cat_dog('catdog'))      # Output: True
print(cat_dog('catcat'))      # Output: False
print(cat_dog('1cat1cadodog'))# Output: True
