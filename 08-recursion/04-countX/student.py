
def countX(text):
    if len(text) <1:
        return 0
    if text[-1] == "x":
        return 1 + countX(text[:-1])
    else : 
        return countX(text[:-1])
    
    