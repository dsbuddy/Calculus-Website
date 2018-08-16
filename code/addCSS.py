import sys
import re



def addStyle(filename):
	f = open(filename, "r")
	lines = f.readlines()
	f.close()

	newFile = []

	count = 0
	count2 = 0

	for line in lines:
		newLine = ""
		if re.match(r"^\s*</head>\s*$", line):
			# print("OLD: " + line)
			# newText = re.sub(r"^\s*</head>\s*$", '\n<!-- Bootstrap core CSS -->\n<link href="../vendor/bootstrap/css/bootstrap.css" rel="stylesheet">\n\n<!-- Custom fonts for this template -->\n<link href="../vendor/font-awesome/css/font-awesome.css" rel="stylesheet" type="text/css">\n<link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>\n<link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>\n\n<!-- Custom styles for this template -->\n<link href="../vendor/bootstrap/css/clean-blog.css" rel="stylesheet">\n<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML">\n</script>\n\n<script src="https://code.jquery.com/jquery-1.10.2.js"></script>\n</head>', line)
			# newText = re.sub(r"^\s*</head>\s*$", r'    <!-- Bootstrap core CSS -->\n<link href="../vendor/bootstrap/css/bootstrap.css" rel="stylesheet">\n\n<!-- Custom fonts for this template -->\n<link href="../vendor/font-awesome/css/font-awesome.css" rel="stylesheet" type="text/css">\n<link href="https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic" rel="stylesheet" type="text/css">\n<link href="https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800" rel="stylesheet" type="text/css">\n\n<!-- Custom styles for this template -->\n<link href="../vendor/bootstrap/css/clean-blog.css" rel="stylesheet">\n<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML">\n</script>\n\n<script src="https://code.jquery.com/jquery-1.10.2.js"></script>', line)
			newText = re.sub(r"^\s*</head>\s*$", r'    <!-- Bootstrap core CSS -->\n<link href="../../../vendor/bootstrap/css/bootstrap.css" rel="stylesheet">\n\n<!-- Custom fonts for this template -->\n<link href="../../../vendor/font-awesome/css/font-awesome.css" rel="stylesheet" type="text/css">\n<link href="https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic" rel="stylesheet" type="text/css">\n<link href="https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800" rel="stylesheet" type="text/css">\n\n<!-- Custom styles for this template -->\n<link href="../../../vendor/bootstrap/css/clean-blog.css" rel="stylesheet">\n<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML">\n</script>\n\n<script src="https://code.jquery.com/jquery-1.10.2.js"></script>', line)
			# print("NEW: " + newText)
			newFile.append(newText)
			print("done")
		else:
			newFile.append(line) 

	f = open(filename[:-12]+"_style.html", "w")
	f.write("".join(newFile))
	f.close()





if __name__ == "__main__":
	addStyle(sys.argv[1])
	print("Done style")
	# addEnd(sys.argv[1][:-5]+"_button.html")
	# print("Done end")