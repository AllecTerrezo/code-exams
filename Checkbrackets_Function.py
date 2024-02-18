def check_brackets(text: str) -> bool:

    #Define variables that will serve as memory
    brackets_list = ["(",")","[","]","{","}"]
    open_brackets = ["(","[","{"]
    #Auxiliary list that will serve as stack data structure
    aux = []

    #Loop through the input data checking if the item is a bracket and if it is an aperture bracket
    for item in text:
        if item in brackets_list:
            if item in open_brackets:
                aux.append(item)
            else:
                #If the aux list has no items and the iterated item is a closing bracket, return False
                if len(aux)==0:
                    return False
                #If the closing bracket does not refer to the first last opening bracket in the aux list, then return false
                elif ((aux[len(aux)-1]=="(")and (item!=")")):
                    return False
                elif ((aux[len(aux)-1]=="[") and (item!="]")):
                    return False
                elif ((aux[len(aux)-1]=="{") and (item!="}")):
                    return False
                #If the closing bracket is related to the last opening bracket in the aux list, then delete the last item in the list
                else:
                    aux.pop(len(aux)-1)
        #If it's not a bracket, just pass it on
        else:
            pass
    #If the loop iterates until the end without errors, it returns the result of the empty list check
    return  len(aux)==0

assert check_brackets("{[]}")
assert not check_brackets("{(])}")
assert not check_brackets("{([)]}")
