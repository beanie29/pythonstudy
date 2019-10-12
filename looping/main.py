
filenames = [
    './drinks.txt',
    './food.txt'
]

#data = []
output_filename = './pantry.txt'

input_files = [open(filename) for filename in filenames]
output = open(output_filename, 'w')

for input_file in input_files:
    for line in input_file:
        output.write(line)
    input_file.close()
output.close()

# with open(output_filename, 'w') as writer:
#     for filename in filenames:
#         with open(filename) as reader:
#             for line in reader:
#                 writer.write(line)


# with open(output_filename, 'w') as f:
#     f.writelines(data)