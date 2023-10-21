# Nicholas Ong - Q1(b): Numbers in Files

def solve(output_file_name, n):
    outfile = open(output_file_name, "w")
    outfile.writelines([str(i)+'\n' for i in range(0, n, 2)])
    outfile.close()

def main():
    test_cases = [["q1-output.txt", 10]]
    for filename, n in test_cases:
        solve(filename, n)

if __name__ == "__main__":
    main()
