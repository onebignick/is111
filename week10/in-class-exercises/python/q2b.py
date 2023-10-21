# Nicholas Ong - Q2(b): Books
def check_same_author(file_name):
    infile = open(f"../src/{file_name}", "r")
    lines = [i.split('\t') for i in infile.readlines()]
    if not lines: return False
    if len(lines) == 1: return True
    
    left, right = 0, 1
    while right < len(lines):
        if lines[left][1] != lines[right][1]: return False
        left, right = right, right+1
    return True

def main():
    test_cases = ["books-1.txt", "books-2.txt", "books-3.txt"]
    for test_case in test_cases:
        print(check_same_author(test_case))
    return 0

if __name__ == "__main__":
    main()
