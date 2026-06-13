"""
converter_control.py

Handles all user input for the conversion.
"""

def choice(converters): #input selection for which converter section
    """Prompts the user to select a converter function from a list.
    Returns the index of the selected function."""
    while True:
        
        menu = "\n".join([f"{i}: {c.__name__}" for i, c in enumerate(converters)])
        
        try: #when user behaves as intended
                
            if (user := int(input(f'''Enter 0-{len(converters)-1} with: \n{menu} \n==> '''))) in range(len(converters)):
                return user
            
            print("Out of range, try again.")
            
        except ValueError: #if the user does a mistake
            print("Invalid input, try again.")

def unit_selection(unit_table): #input selection for units
    """Prompts the user to select a unit from the given unit table.
    Returns the selected unit as a string."""
    
    while (unit := input(f'''enter unit "{', '.join(unit_table.keys())}": ''').strip().lower()) not in unit_table:
        print("invalid \n")
    
    return unit
    
def category_choice(category_table):
    """Prompts the user to select a category from the categories_table dict.
    Returns the selected category name as a string."""
    
    items = list(category_table.keys())
    
    while True:
        
        menu = "\n".join([f"{i}: {name}" for i, name in enumerate(items)])
        
        try:
            if (user := int(input(f"Enter 0-{len(items)-1}:\n{menu}\n==> "))) in range(len(items)):
                return items[user]
            print("Out of range, try again.")
            
        except ValueError:
            print("Invalid input, try again.")
    
def value(): #input selection for numbers
    """Prompts the user to enter a numeric value.
    Returns the value as a float."""
    
    while True:
        try: #when user behaves as intended
            number = float(input("enter number: "))
            return number
            
        except ValueError: #if the user does a mistake
            print("Invalid")
        
def table_of_contents(categories_table):
    """Prints all available categories and their converters."""
    
    print("TABLE OF CONTENT")
    for category, converters in categories_table.items():
        print(f"{category}: {', '.join(c.__name__ for c in converters)}")
    
    print("\n")

def navigation(navigation_table):
    
    """ This exists to make the user have control on what they do.
    1. CONVERTER
    2. TO SEE HISTORY
    3. QUIT    
    """
    
    while (decision := input(f'''enter "{', '.join(navigation_table.keys())}": ''').strip().lower()) not in navigation_table:
        print("invalid \n")
    
    return decision 