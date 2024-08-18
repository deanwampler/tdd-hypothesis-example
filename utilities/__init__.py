# Utilities

# See comparisons of methods here for checking if a string is an integer:
# https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
def check_int(s: str) -> bool:
    if len(s) == 0:
        return False
    elif s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()    
