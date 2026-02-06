import os


files = {}
directory = "../"

def get_file_names(folder, level=1):
    if level == -1:
        return
    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            extension = os.path.splitext(element)[1]
            if extension not in files:
                files[extension] = []
            files[extension].append(element)
        else:
            get_file_names(f, level - 1)

get_file_names(directory, level=2)

with open(os.path.join(directory, "report.txt"), "w") as output_file:
    for ext, file_names in sorted(files.items()):
        output_file.write(f"{ext}\n")
        for f_name in sorted(file_names):
            output_file.write(f"- - - {f_name}\n")