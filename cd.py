import sys

seperator = "/"

def cd(path, to_path):
    if is_absolute_path(to_path):
        path = normalize_path(to_path)
        return path
    path = normalize_path(path + seperator + to_path)
    return path
    
def is_absolute_path(path):
    return path.startswith('/')
    
def normalize_path(path):
    is_absolute = is_absolute_path(path)
    parts = []
    for p in path.split(seperator):
        if not p or p == ".":
            continue
        elif p == "..":
            if len(parts) == 0:
                if is_absolute:
                    continue
            else:
                if parts[len(parts)-1] != "..":
                    del parts[len(parts)-1]
                    continue
        elif p.startswith(".."):
            return p + ": No such file or directory"
        parts.append(p)
    prefix = ""
    if is_absolute:
        prefix = seperator
    return prefix + seperator.join(parts)

if __name__ == "__main__":
    
    n = len(sys.argv)
    if n == 3:
        path = sys.argv[1]
        newpath = sys.argv[2]
        print(cd(path, newpath))
        
    elif n == 2 and sys.argv[1] == "test":
        tests = [
            ("/", "abc"),
            ("/abc/def", "ghi"),
            ("/abc/def", ".."),
            ("/abc/def", "/abc"),
            ("/abc/def", "/abc/klm"),
            ("/abc/def", "../.."),
            ("/abc/def", "../../.."),
            ("/abc/def", "."),
            ("/abc/def", "..klm"),
            ("/abc/def", "//////"),
            ("/abc/def", "......"),
            ("/abc/def", "../gh///../klm/.")
        ]
        for t in tests:
            path, newpath = t
            print("Testcase: cd {0} {1} \t--> {2}".format(path, newpath, cd(path, newpath)))