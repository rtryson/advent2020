def validate_doc(doc):
	if len(doc) == 8:
		return 1
	if len(doc) == 7 and not "cid" in doc.keys():
		return 1
	return 0

def validate_doc_alt(doc):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.
    if validate_doc(doc):
    	if int(doc["byr"]) < 1920 or int(doc["byr"]) > 2002:
    		return 0
    	if int(doc["iyr"]) < 2010 or int(doc["iyr"]) > 2020:
    		return 0
    	if int(doc["eyr"]) < 2020 or int(doc["eyr"]) > 2030:
    		return 0
    	if doc["hgt"][-2:] not in ["cm","in"]:
    		return 0
    	if doc["hgt"][-2:] == "cm":
    		if int(doc["hgt"][:-2]) < 150 or int(doc["hgt"][:-2]) > 193:
    			return 0
    	if doc["hgt"][-2:] == "in":
    		if int(doc["hgt"][:-2]) < 59 or int(doc["hgt"][:-2]) > 76:
    			return 0
    	if len(doc["hcl"]) != 7:
    		return 0
    	for c in doc["hcl"][1:]:
    		if c not in ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
    			return 0
    	if doc["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
    		return 0
    	if len(doc["pid"]) != 9:
    		return 0
    	return 1
    return 0


currDoc = dict()
valid = 0
validAlt = 0
with open("input/p4") as f:
	for line in f.read().splitlines():
		if not line:
			# validate currDoc and reset
			valid += validate_doc(currDoc)
			validAlt += validate_doc_alt(currDoc)
			currDoc = {}
		else:
			for pair in line.split():
				kvTuple = pair.split(':')
				currDoc[kvTuple[0]] = kvTuple[1]
	valid += validate_doc(currDoc) #account for last one
	validAlt += validate_doc_alt(currDoc)

print(valid)
print(validAlt)