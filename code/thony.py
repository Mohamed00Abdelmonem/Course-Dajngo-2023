
def solve(s):
    names = s.split()  # Split the full name into a list of names
    
    # Capitalize the first letter of each name
    capitalized_names = [name.capitalize() for name in names]
    if 0<len(capitalized_names)<1000:
        
        capitalized_full_name = ' '.join(capitalized_names)  # Join the capitalized names back into a string
        
        return capitalized_full_name

# Example usage

print(solve("hello   world  lol"))

