"""This file contains the funtions to see and update history."""

import json

def history_write(unit, number): #for user history writing
    
    """
    This funtion writes funtion only.
    stores only the unit and value entered by the user
    
    """
    
    try: #if file exists
        with open("history.json", "r") as f:
            history = json.load(f)
            
    except FileNotFoundError: #if the file doesnt exist, creates it, and is in "read mode"
        history = []
       
    history.append({"unit": str(unit), "number": number}) #adds the unit and number to database/jsonfile
        
    with open("history.json", "w") as f: #the files is in "write" mode
        json.dump(history, f, indent=4)


def history_view(): #for history reading
    
    """This reads history only"""
    
    try:
        with open("history.json", "r") as f: #opens the file
            history = json.load(f)
        print(json.dumps(history, indent=4))   
           
    except FileNotFoundError: #incase file isnt found
        print("file not found")