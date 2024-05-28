
def fibonnaci(number):
    if number <= 0:
        return 0
    elif number == 1 :
        return 1
    else :
        return fibonnaci(number - 1) + fibonnaci(number -2)
    