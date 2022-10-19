
def read_file(path_file: str):
    list_webs = []
    try:
        with open(path_file, 'r') as file:
            content = file.readlines()
            for line in content:
                split_line =  line.strip().split(';')
                list_webs.append((split_line[0], split_line[1]))
    except OSError as ex:
        print(f"File not read: {ex}")
    return list_webs
