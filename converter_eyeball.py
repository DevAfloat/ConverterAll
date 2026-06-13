"""
converter_eyeball.py
DO NOT MODIFY!!!

Visual inspection script for converter_data.py — FOR DEVS ONLY.
Prints all conversions to stdout so you can eyeball whether the data looks right.
"""

import converter_data as data
import converter_print_conversion as conversion 

test_table = {
    #basic
    data.mass:        ["kg",  1],
    data.length:      ["km",  1],
    data.time:        ["hr",  1],
    data.speed:       ["m/s", 1],
    
    # scientific
    data.temperature: ["c", 37],
    data.pressure:    ["atm", 1],
    data.energy:      ["j",   1],
    
    # living
    data.volume:      ["l",   1],
    data.area:        ["m2",  1],
    data.cooking:     ["cup", 1],
    
    # misc
    
    data.storage:     ["gb",  1],
    data.power:       ["kw",  1],
}
    

for unit_table, (unit, number) in test_table.items(): #this prints out all the ratios from covertor_data.py
    
    if unit_table == data.temperature:
        print(unit_table.__name__)
        conversion.print_conversion_for_temperature(unit, number, unit_table())
    
    else:
        print(str(unit_table.__name__))
        conversion.print_conversion(unit, number, unit_table())