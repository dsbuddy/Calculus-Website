import sys
import re



def rewriteTex(filename):
	f = open(filename, "r")
	lines = f.readlines()
	f.close()

	newFile = []


	for line in lines:
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

			newText = re.sub(r'\s*\\ifans\s*', "\\includegraphics[scale=0.5]{start.pdf}\n", line)
			newText = re.sub(r'\s*\\fi', "\n\\includegraphics[scale=0.5]{end.pdf}\n", newText)
			newText = re.sub(r'\\\w*?box', '', newText)

			newFile.append(newText)
		else:
			newFile.append(line)

	f = open(filename[:-4]+"_revised.tex", "w")
	f.write("".join(newFile))
	f.close()


if __name__ == "__main__":
	rewriteTex(sys.argv[1])