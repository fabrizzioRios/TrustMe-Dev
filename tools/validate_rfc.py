import re

with open("rfc.txt", "r") as file:
    data = file.read()

pattern = r'\b([A-Z]{4}\d{6}[A-Z0-9]{3})\b|(?<=RFC\s)([nv])'

matches = re.finditer(pattern, data)

prev_rfc = None

result = {}

for match in matches:
    rfc, status = match.groups()
    
    if rfc:
        prev_rfc = rfc
    elif status == 'n' and prev_rfc:
        result[prev_rfc] = 'n'
    elif status == 'v' and prev_rfc:
        result[prev_rfc] = 'v'