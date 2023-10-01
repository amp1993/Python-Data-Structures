def list_manipulation(lst, command, location, value):
    if command == 'add':
        if location == 'beginning' and value is not None:
            lst.insert(0, value)
        elif location == 'end' and value is not None:
            lst.append(value)
        else:
            return None
    elif command == 'remove':
        if location == 'beginning':
            if len(lst) > 0:
                return lst.pop(0)
        elif location == 'end':
            if len(lst) > 0:
                return lst.pop()
        else:
            return None
    else:
        return None

lst = [1, 2, 3]
print(list_manipulation(lst, 'add', 'end', 30))  # Output: [1, 2, 3, 30]
