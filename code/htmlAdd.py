import sys
import re



def addButton(filename):
	f = open(filename, "r")
	lines = f.readlines()
	f.close()

	newFile = []

	count = 0
	count2 = 0

	for line in lines:
		newLine = ""
		if re.match(r".*\s*<embed src=\"start\.pdf\"\s*/>\s*.*", line):
			count+=1
			# print("OLD: " + line)
			newText = re.sub(r"\s*<embed src=\"start\.pdf\"\s*/>\s*", '<button type="button" class="btn btn-primary" onclick="toggleAnswer(\'ex' + str(count) + '\')">Click for Solution</button>\n<br><br>\n<div id="ex' + str(count) + '" style="display:none">\n', line)
			# print("NEW: " + newText)
			newFile.append(newText)
		# if "end.pdf" in line:
		# 	count2 += 1
		# 	# print("OLD: " + line)
		# 	newText = re.sub(r"\s*<embed\s*src=\"end\.pdf\"\s*/>\s*", "\n</div>", line)
		# 	print("NEW: " + newText)
		# 	newFile.append(newText)
		# if re.match(r"\s*</html>\s*", line):
		# 	# print("OLD: " + line)
		# 	newText = re.sub(r"\s*</html>\s*", '<script>\nfunction toggleAnswer(idName) {\nvar x = document.getElementById(idName);\nif (x.style.display === "none") {\nx.style.display = "block";\n} else {\nx.style.display = "none";\n}\n}</script>\n</html>', line)
		# 	# print("NEW: " + newText)
		# 	newFile.append(newText)
		# if ("start.pdf" not in line) or ("end.pdf" not in line) or ("/html" not in line):
		else:
			newFile.append(line) 

	f = open(filename[:-5]+"_button.html", "w")
	f.write("".join(newFile))
	f.close()

def addEnd(filename):
	f = open(filename, "r")
	lines = f.readlines()
	f.close()

	newFile = []

	count = 0
	count2 = 0

	for line in lines:
		newLine = ""
		# if re.match(r".*\s*<embed src=\"start\.pdf\"\s*/>\s*.*", line):
		# 	count+=1
		# 	# print("OLD: " + line)
		# 	newText = re.sub(r"\s*<embed src=\"start\.pdf\"\s*/>\s*", '<button type="button" class="btn btn-primary" onclick="toggleAnswer(\'ex' + str(count) + '\')>Click for Solution</button>\n<br><br>\n<div id="ex' + str(count) + '" style="display:none">\n', line)
		# 	# print("NEW: " + newText)
		# 	newFile.append(newText)
		# if "end.pdf" in line:
		if re.match(r".*\s*<embed\s*src=\"end\.pdf\"\s*/>\s*.*", line):
			count2 += 1
			# print("OLD: " + line)
			newText = re.sub(r"\s*<embed\s*src=\"end\.pdf\"\s*/>\s*", r"\n</div>", line)
			# print("NEW: " + newText)
			newFile.append(newText)
		# if re.match(r"\s*</html>\s*", line):
		# 	# print("OLD: " + line)
		# 	newText = re.sub(r"\s*</html>\s*", '<script>\nfunction toggleAnswer(idName) {\nvar x = document.getElementById(idName);\nif (x.style.display === "none") {\nx.style.display = "block";\n} else {\nx.style.display = "none";\n}\n}</script>\n</html>', line)
		# 	# print("NEW: " + newText)
		# 	newFile.append(newText)
		# if ("start.pdf" not in line) or ("end.pdf" not in line) or ("/html" not in line):
		else:
			newFile.append(line) 

	f = open(filename, "w")
	f.write("".join(newFile))
	f.close()

def addScript(filename):
	f = open(filename, "r")
	lines = f.readlines()
	f.close()

	newFile = []

	count = 0
	count2 = 0

	for line in lines:
		newLine = ""
		# if re.match(r".*\s*<embed src=\"start\.pdf\"\s*/>\s*.*", line):
		# 	count+=1
		# 	# print("OLD: " + line)
		# 	newText = re.sub(r"\s*<embed src=\"start\.pdf\"\s*/>\s*", '<button type="button" class="btn btn-primary" onclick="toggleAnswer(\'ex' + str(count) + '\')>Click for Solution</button>\n<br><br>\n<div id="ex' + str(count) + '" style="display:none">\n', line)
		# 	# print("NEW: " + newText)
		# 	newFile.append(newText)
		# if "end.pdf" in line:
		# 	count2 += 1
		# 	# print("OLD: " + line)
		# 	newText = re.sub(r"\s*<embed\s*src=\"end\.pdf\"\s*/>\s*", "\n</div>", line)
		# 	print("NEW: " + newText)
		# 	newFile.append(newText)
		if re.match(r"\s*</html>\s*", line):
			# print("OLD: " + line)
			newText = re.sub(r"\s*</html>\s*", '<script>\nfunction toggleAnswer(idName) {\nvar x = document.getElementById(idName);\nif (x.style.display === "none") {\nx.style.display = "block";\n} else {\nx.style.display = "none";\n}\n}</script>\n</html>', line)
			# print("NEW: " + newText)
			newFile.append(newText)
		# if ("start.pdf" not in line) or ("end.pdf" not in line) or ("/html" not in line):
		else:
			newFile.append(line) 

	f = open(filename, "w")
	f.write("".join(newFile))
	f.close()
	



if __name__ == "__main__":
	addButton(sys.argv[1])
	print("Done button")
	addEnd(sys.argv[1][:-5]+"_button.html")
	print("Done end")
	addScript(sys.argv[1][:-5]+"_button.html")
	print("Done script")