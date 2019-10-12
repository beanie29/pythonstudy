names = [
	"Peter\n",
	"Julia\n",
	"Aubri\n",
	"David\n"
]

filename = "./test.txt"
f = open(filename, 'r+')
f.seek(-3,2)
f.write('something')
# for name in names:
# 	f.write(name + '\n')
f.writelines(names)

next_line = f.readline()
print(next_line)
f.close()