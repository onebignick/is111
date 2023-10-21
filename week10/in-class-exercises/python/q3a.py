# Nicholas Ong - Q3(a): Phone book

def solve(file_name):
    infile = open(f"../src/{file_name}", "r")
    lines = infile.readlines()
    for line in lines:
        temp = line.strip().split("|")
        if len(temp[-1])==8:
            print(f"{temp[0]}\t{temp[-1]}")
        elif temp[-1][0] == "+":
            ttemp = temp[-1].split()
            if ttemp[0][1:]=="65" and len(ttemp[1])==8: print(f"{temp[0]}\t{temp[-1]}")
        elif temp[-1][0] == "(":
            ttemp = temp[-1].split(")")
            if ttemp[0][2:]=="65" and len(ttemp[1])==8: print(f"{temp[0]}\t{temp[-1]}")
    return

def main():
    test_cases = ["phone_book.txt"]
    for test_case in test_cases:
        solve(test_case)

if __name__ == "__main__":
    main()
