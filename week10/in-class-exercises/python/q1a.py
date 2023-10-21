# Nicholas Ong - Q1(a) Numbers in Files
def sum_up(input_file_name):
    infile = open(f"../src/{input_file_name}", "r")
    result = sum([float(i.strip()) for i in infile.readlines()])
    print(result)
    infile.close()

def main():
    test_cases = ["q1-1.txt", "q1-2.txt"]
    for test in test_cases:
        sum_up(test)

if __name__ == "__main__":
    main()
