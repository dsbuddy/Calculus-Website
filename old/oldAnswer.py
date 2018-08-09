import sys
import re



def regexbois(text):
	newText = text

	# patBrace = r'\s*\\ifans\s*{.*}\s*\\fi'
	# pattern = re.compile(patBrace)
	# if pattern.search(text) != None:
	# 	# newText = re.sub(r'(\s*\\ifans\s*{|}\s*\\fi)', '', newText)
	# 	newText = re.sub(r'(\s*\\ifans\s*{\s*\\fbox|}\s*\\fi)', '', newText)
	# else:
	# (?# newText = re.sub(r'(\s*\\ifans\s*|\s*\\fi)', '', newText))
	newText = re.sub(r'(\s*\\ifans\s*|\s*\\fi|\\\D*?box)', '', newText)
	# (?# newText = re.sub(r'\\\D*box', '', newText))
	return newText

def rewriteTex(filename):
	f = open(filename, "r")
	lines = f.readlines()
	f.close()

	newFile = []


	for line in lines:
		# print("LINE: " + line)
		newLine = ""
		
		if "\\anstrue" in line:
			continue
		elif "\\ansfalse" in line:
			continue
		elif "\\ifans{\\newpage}\\fi" in line:
			continue
		elif "\\newif\\ifans" in line:
			continue
		elif "ifans" in line or "fi" in line:
			# pat = [r'(\s*\\ifans\s*|\s*\\fi)']
			# pat = [r'(\s*\\ifans\s*\\fbox\s*{|}\s*\\fi)']
			# print("OLD: " + line)
			# print("NEW: " + newLine)
			# newFile.append(newLine)

			newText= re.sub(r'\s*\\ifans\s*', "\\includegraphics[scale=0.5]{start.pdf}\n", line)
			newText= re.sub(r'\s*\\fi', "\n\\includegraphics[scale=0.5]{end.pdf}\n", newText)
			newText = re.sub(r'\\\w*?box', '', newText)


			# # continue
			# # print("LINE: " + line)
			# # answer = line[line.index("ifans")+5:-4]
			# answer = line[line.index("\\fbox")+5:-4]
			# # answer = line[line.rfind("box")+4:-5]
			# # answer = line[line.index("ifans")+11:-5]
			# # print("ANSWER: " + answer)

			# # # newLine = "\\item\\sqrt{\\frac{\\sum_{begn}^{b}}{drexel}}"
			# newLine += "\\includegraphics[scale=0.5]{start.pdf}"
			# newLine += "\n" + answer + "\n"
			# newLine += "\\includegraphics[scale=0.5]{end.pdf}"

			# # print(newLine)

			newFile.append(newText)
			# # # print("NEW LINE: " + newLine)
		else:
			newFile.append(line)

	f = open(filename[:-4]+"_revised.tex", "w")
	f.write("".join(newFile))
	f.close()

	#$ sed -i 's/\ifans{/\sqrt{\frac{\sum_begin^b x}{drexel}}/g' test.tex


if __name__ == "__main__":
	rewriteTex(sys.argv[1])