import random as rnd

def is_crit_or_fail(number):
    if number == 20:
        return "Critical! "
    elif number == 1:
        return "Failure! "
    else:
        return ""

def roll_d20(text):

    if text.split("d")[0] == "" or  text.split("d")[0] == "1":

        result_string = ""
        result = 0

        dice_modifier = 0
        dice_modifier_string = ""
        critical = ""
        result_1 = rnd.randint(1, 20)
        result_2 = rnd.randint(1, 20)

        if "+" in text:
            dice_modifier = text.split("+")[1]
            
            try:
                dice_modifier = int(dice_modifier)
                dice_modifier_string = f" + {dice_modifier}"
            except ValueError as e:  
                return f"Invalid modifier. ({e})"
        
        dice_modifier_string = dice_modifier_string.removesuffix(" + 0")

        # Advantage
        if "d20a" in text:
            result = max(result_1, result_2)
            critical = is_crit_or_fail(result)
            result = result + dice_modifier
            result_string += f"{critical}Result: {result} ({result_1} | {result_2}{dice_modifier_string})"
        
        # Disadvantage
        elif "d20d" in text:
            result = min(result_1, result_2)
            critical = is_crit_or_fail(result)
            result = result + dice_modifier
            result_string += f"{critical}Result: {result} ({result_1} | {result_2}{dice_modifier_string})"

        # Straight roll
        else:
            result = result_1
            critical = is_crit_or_fail(result)
            result = result + dice_modifier
            result_string += f"{critical}Result: {result} ({result_1}{dice_modifier_string})"

        return result_string
    
    else:
        return roll_ndn(text)

def roll_ndn(text):
    
    result_string = ""
    result = 0
    dice_amount = 1
    dice_type = 0
    dice_modifier = 0

    dice_amount = text.split("d")[0]
        
    if "+" in text:
        dice_type = text.split("d")[1]
        
        dice_modifier = dice_type.split("+")[1]
        dice_type = dice_type.split("+")[0]

    else:
        dice_type = text.split("d")[1]
    
    try:
        dice_amount = int(dice_amount)
    except ValueError as e:
        return f"Invalid number of dice. ({e})"
    
    try:
        dice_type = int(dice_type)
    except ValueError as e:
        return f"Invalid type of dice. ({e})"
    
    try:
        dice_modifier = int(dice_modifier)
    except ValueError as e:
        return f"Invalid modifier. ({e})"
    
    print(f"Amount: {dice_amount}")
    print(f"Type: {dice_type}")
    print(f"Modifier: {dice_modifier}")

    if  1 <= dice_amount <= 50:
        for i in range(dice_amount):
            roll = rnd.randint(1, dice_type)
            result += roll
            result_string += f"{roll} + "
    else: 
        return "That's too many dice!"
    
    result += dice_modifier
    
    result_string = result_string.rstrip(" +")
    
    if dice_modifier == 0:
        return f"Result: {result} ({result_string})"
    else:
        return f"Result: {result} (({result_string}) + {dice_modifier})"

def roll(text):
    if "d20" in text:
        return f"Rolling {text}\n{(roll_d20(text))}"
    
    elif "d" in text:
        return f"Rolling {text}\n{(roll_ndn(text))}"
    
    elif "help" in text:
        return "/r roll 2d6+3 for damage dice. Can roll dice in this format: <amount>d<type>+<modifier.\n/r roll d20a+4 for D20 with advantage.\n/r roll d20d+4 for D20 with disadvantage."
    
    else:
        return("Something went wrong...")
        
                
#usr_input = input("Roll ")
#print(roll(usr_input))