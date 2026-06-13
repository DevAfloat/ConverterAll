"""
converter_main.py

Entry point for the converter program.
Orchestrates user input and dispatches to the correct conversion function.

Flow: category selection -> converter selection -> unit selection -> value input -> output.
"""

import converter_data as data
import converter_control as control
import converter_history as history 
import converter_print_conversion as conversion 
'''
This program executes the main files.
Takes in the category input -> converter input -> unit selection -> number value -> output.

'''

#executes the program
def main():
    """Main loop. Prompts the user to select a category, converter, unit, and value.
    Routes to the appropriate conversion function and prints the result."""
    
    control.table_of_contents(data.categories_table)

    category = control.category_choice(data.categories_table)
    converters = data.categories_table[category]

    selected = converters[control.choice(converters)]  # just the function, no call

    func = selected()  # now call it to get the table
    unit = control.unit_selection(func)
    number = control.value()

    history.history_write(unit, number)

    if selected == data.temperature: #converts temperature to its other units only.
        # Temperature does not work with ratios, so it has its own dedicated print function.
        conversion.print_conversion_for_temperature(unit, number, func)
        
    else:   #converts to its other units
        conversion.print_conversion(unit, number, func)

if __name__ == "__main__": 
    try:
        
        navigation_table = {
        
        "conversion": main,
        "history": history.history_view,
        "quit": exit
        
        }
        
        while True: #menu system
            menu = control.navigation(navigation_table)
            navigation_table[menu]()

    except KeyboardInterrupt:
        print("\nExiting.")