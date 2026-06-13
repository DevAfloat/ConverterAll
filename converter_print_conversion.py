"""This file is responsible for the conversion and its printing."""

def print_conversion(unit, number, unit_table): #final print out for conversions
    """Prints the conversion of number from unit to all other units in unit_table.
    Uses ratio-based multiplication against a common base unit."""
    
    base = number * unit_table[unit]
    for u, factor in unit_table.items():
        print(f"{number}{unit} = {base / factor:.4f} {u}")
        
    print("\n \n")
    
def print_conversion_for_temperature(unit, number, unit_table):
    """Prints the conversion of number from unit to all other temperature units.
    Uses formula-based lambdas rather than ratio multiplication."""
    
    for target_unit, formula in unit_table[unit]:
        print(f"{number}{unit} = {formula(number):.4f} {target_unit}")