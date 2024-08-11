import re 

s = "#????"
matches = re.finditer(r'(?=([#?]{1}[.?]{1,}?[#?]{1}[.?]*$))', s)
results = [match.group(1) for match in matches]
print(f"{results}")