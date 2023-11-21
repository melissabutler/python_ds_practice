def list_manipulation(lst, command, location, value=None):

    if command == "remove":
        if location == "beginning":
            lst.remove(1)
            return lst
        elif location == "end":
            lst.pop(-1)
            return lst
        else:
            return None
    
    if command == "add":
        if location == "beginning":
            lst.insert(0, value)
            return lst
        elif location == "end":
            lst.append(value)
            return lst
        else:
            return None
   