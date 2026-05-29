import os
from utils.file_utils import load_colleagues
from utils.openspace import OpenSpace

def main () -> None:
    
    filepath = "new_colleagues.txt"

    colleagues = load_colleagues(filepath)
    print (colleagues)

    open_space = OpenSpace()

    open_space.organize(colleagues)

    open_space.display()

    open_space.store("output")

if __name__ == "__main__":
    main()