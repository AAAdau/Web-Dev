def cigar_party(cigars, is_weekend):
    # Check if it's the weekend and the number of cigars is at least 40,
    # or if it's not the weekend and the number of cigars is between 40 and 60 (inclusive)
    return (is_weekend and cigars >= 40) or (not is_weekend and 40 <= cigars <= 60)

# Test cases
print(cigar_party(30, False))  # Output: False
print(cigar_party(50, False))  # Output: True
print(cigar_party(70, True))   # Output: True
