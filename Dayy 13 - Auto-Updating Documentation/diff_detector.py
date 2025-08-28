import difflib

def load_file(path):
    with open(path, 'r') as f:
        return f.readlines()

def get_diff(old_path, new_path):
    old = load_file(old_path)
    new = load_file(new_path)
    diff = difflib.unified_diff(old, new, fromfile='old', tofile='new', lineterm='')
    return '\n'.join(diff)