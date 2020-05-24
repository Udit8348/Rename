# rename three
import glob
import os
import re

targets = []
ending = "*(1)*" # targeted file suffixed (png, mp4)
deploy = True
# Build a Filtered List of Targets
for name in glob.glob(ending):
	if(name.rfind("U") >= 0 and name.rfind(".xmp") < 0):			# change to HDDU
		targets.append(name)
		
print(targets)

# Extract Number to Find the Corresponding XMP file and Rename the Media File
newPrefix = "HDDUDITB - "
src = ["",""]	# media, xmp source
namePart = ["",""] # orginal name with '(1)', shorted name without '(1)' (both without extension)
dst = ["",""]	# media, xmp destination
for file in range(len(targets)):

	src[0] = targets[file]
	start = src[0].rfind('.');
	end = len(src[0]) # note: the selection operation is not inclusive so this does not need to be -1
	type = src[0][start : end]
	namePart[0] = src[0][0:start]
	namePart[1] = src[0][0:start-3] 	# get the file name without the (1)
	
	# use regex to get id number
	num = re.findall(r'\d+', namePart[1])
	
	# build new file names if number is found and skip empty lists
	if(num):
		src[1] = namePart[0] + ".xmp"
		
		dst[0] = newPrefix + num[0] + type
		dst[1] = newPrefix + num[0] + ".xmp"
	else:
		print("no number found...renaming skipped")
	
	# check vals
	if(deploy):
		os.rename(src[0], dst[0]);
		os.rename(src[1], dst[1]);
	else:
		print(" ")
		print("Input Media Name: ", src[0])
		print("Generated XMP Name: ", src[1])
		print("New Media Name: ", dst[0])
		print("New XMP Name: ", dst[1])

