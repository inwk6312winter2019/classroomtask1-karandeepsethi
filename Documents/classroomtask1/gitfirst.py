import os

def walk(dirname):
	for name is os.listdir(dirname):
		path=os.path.join(dirname,name)

		if os.path.isfile(path):
			pritnt(path)
		else:
			walk(path)

print(os.filename(" "))