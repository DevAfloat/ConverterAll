"""
converter_data.py

Holds all unit conversion tables as functions that return dicts.
Ratio-based conversions return a flat dict of {unit: factor_to_base}.
Temperature returns a dict of {unit: [(target_unit, formula_lambda)]}.

categories_table maps category names to their list of converter functions.
"""

# --- BASIC ---

def mass(): #conversion rate for mass
    """Returns conversion factors for mass units relative to kilograms."""
    unit_table = {
    "kg":    1,
    "g":     0.001,
    "ton":   1000,
    "mg":    0.000001,
    "lb":    0.453592,
    "oz":    0.0283495,
        
    }
    
    return unit_table

def length(): #conversion rate for length
    """Returns conversion factors for length units relative to kilometres."""
    
    unit_table = {
        
    "km":    1,
    "m":     0.001,
    "cm":    0.00001,
    "mm":    0.000001,
    "mi":    1.60934,
    "ft":    0.0003048,
    "in":    0.0000254,
        
    }
    
    return unit_table
    
def time():
    """Returns conversion factors for time units relative to seconds."""
    return {
        "s":   1,
        "ms":  0.001,
        "min": 60,
        "hr":  3600,
        "day": 86400,
        "wk":  604800,
        "yr":  31536000,
    }

# --- SCIENTIFIC ---

def temperature(): #conversion rate for temperature
    """Returns formula-based conversions for temperature units.
    Structure differs from ratio converters — each unit maps to a list of
    (target_unit, lambda) tuples rather than a flat factor."""
    
    unit_table = {
        "c":  [("f",  lambda x: (x * 9/5) + 32),
               ("k",  lambda x: x + 273.15),
               ("r",  lambda x: (x + 273.15) * 9/5),
               ("de", lambda x: (100 - x) * 3/2)],

        "f":  [("c",  lambda x: (x - 32) * 5/9),
               ("k",  lambda x: (x + 459.67) * 5/9),
               ("r",  lambda x: x + 459.67),
               ("de", lambda x: (212 - x) * 5/6)],

        "k":  [("c",  lambda x: x - 273.15),
               ("f",  lambda x: (x - 273.15) * 9/5 + 32),
               ("r",  lambda x: x * 9/5),
               ("de", lambda x: (373.15 - x) * 3/2)],

        "r":  [("c",  lambda x: (x - 491.67) * 5/9),
               ("f",  lambda x: x - 459.67),
               ("k",  lambda x: x * 5/9),
               ("de", lambda x: (671.67 - x) * 5/6)],

        "de": [("c",  lambda x: 100 - x * 2/3),
               ("f",  lambda x: 212 - x * 6/5),
               ("k",  lambda x: 373.15 - x * 2/3),
               ("r",  lambda x: 671.67 - x * 6/5)],    
    }
    
    return unit_table

def speed():
    """Returns conversion factors for speed units relative to metres per second."""
    return {
        "m/s":  1,
        "km/h": 0.277778,
        "mph":  0.44704,
        "knot": 0.514444,
        "ft/s": 0.3048,
    }

def pressure():
    """Returns conversion factors for pressure units relative to pascals."""
    return {
        "pa":  1,
        "kpa": 1000,
        "bar": 100000,
        "atm": 101325,
        "psi": 6894.76,
        "mmhg": 133.322,
    }
    
def energy():
    """Returns conversion factors for energy units relative to joules."""
    return {
        "j":    1,
        "kj":   1000,
        "cal":  4.184,
        "kcal": 4184,
        "wh":   3600,
        "kwh":  3600000,
        "ev":   1.60218e-19,
    }
    
    
# --- LIVING --- 

def volume(): #conversion rate for volume
    """Returns conversion factors for volume units relative to litres."""
    
    unit_table = {
        
    "l":     1,
    "ml":    0.001,
    "m3":    1000,
    "cup":   0.2366,
    "fl_oz": 0.029574,
    "gal":   3.78541,
        
        
    }
    
    return unit_table

def area():
    """Returns conversion factors for area units relative to square metres."""
    return {
        "m2":  1,
        "km2": 1000000,
        "cm2": 0.0001,
        "ft2": 0.092903,
        "in2": 0.00064516,
        "ac":  4046.86,
        "ha":  10000,
    }

def cooking():
    """Returns conversion factors for cooking measurements relative to teaspoons."""
    return {
        "tsp":  1,
        "tbsp": 3,
        "cup":  48,
        "fl_oz": 6,
        "ml":   0.202884,
        "l":    202.884,
    }

# --- MISC ---

def storage():
    """Returns conversion factors for digital storage units relative to bits."""
    return {
        "bit":  1,
        "byte": 8,
        "kb":   8000,
        "mb":   8000000,
        "gb":   8000000000,
        "tb":   8000000000000,
    }

def power():
    """Returns conversion factors for power units relative to watts."""
    return {
        "w":   1,
        "kw":  1000,
        "mw":  1000000,
        "hp":  745.7,
        "btu": 0.29307,
    }

#where the main menu lies
categories_table = {
        
    "basic":      [mass, length, time, speed],
    "scientific": [temperature, pressure, energy],
    "living":     [volume, area, cooking],
    "misc":       [storage, power]

    }
    