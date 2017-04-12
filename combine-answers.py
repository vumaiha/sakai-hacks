import glob
import sys
import re

read_files = glob.glob(sys.argv[1])
patternlist=['(<p>)','(</p>)']

with open("result.txt", "wb") as outfile:
	for f in read_files:
		with open(f, "rb") as infile:
			new_result=(infile.read())
			if len(new_result) > 0:
				new_result = re.sub('(&quot;)','"',new_result)
				for r in patternlist:
					new_result = re.sub(r,'',new_result)
				outfile.write(new_result + "\n" +"\n")

	

