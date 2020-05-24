# newer rename searches by file ending
# https://www.geeksforgeeks.org/how-to-use-glob-function-to-find-files-recursively-in-python/
# https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
import glob
import os
deploy = False
targets = []
suffix = ["*(1).xmp", "*(1).jpg", "*(1).avi", "*(1).mov", "*(1).png"] # targeted file suffixed (png, mp4)

# Build a list of Targets
for ending in range(len(suffix)):
	for name in glob.glob(suffix[ending]):
		targets.append(name)

print(targets)

# Rename the Entire List of Targets
print("Start Rename")
for file in range(len(targets)):
	src = targets[file]
	start = src.rfind('.');
	end = len(src) # note: the selection operation is not inclusive so this does not need to be -1
	type = src[start : end]
	print(type)
	dst = "HDDUditB_" + str(file) + type
	
	if(deploy):
		os.rename(src, dst);
	else:
		print(dst)

print("Renaming Complete")