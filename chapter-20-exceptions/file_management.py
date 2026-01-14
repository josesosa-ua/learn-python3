def get_file(name):
    try:
        return open(name)
    except FileNotFoundError as fe:
        print(fe.args)
        return None