"""
Application utils methods
"""

def read_file(path_file: str):
    """
    Read text file and store in list (urls and content requirement)
    Args:
        :param  document: document payload
    Returns:
        response: list web pages with their content requirement
    """
    list_webs = []
    try:
        with open(path_file, 'r', encoding='UTF-8') as file:
            content = file.readlines()
            for line in content:
                split_line =  line.strip().split(';')
                list_webs.append((split_line[0], split_line[1]))
    except OSError as ex:
        print(f"File not read: {ex}")
    return list_webs
