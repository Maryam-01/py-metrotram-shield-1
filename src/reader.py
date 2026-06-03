def read_log(filepath):
    with open(filepath) as log_file:
        contents = log_file.readlines()
    return contents

file = "./data/sample.log"

logs = read_log(file)
print(logs[0].strip())