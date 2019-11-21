import sys

def main():
    # print command line arguments
    filename = sys.argv[1]
    for arg in sys.argv[1:]:
        print (arg)
    print("filename = ",filename)

if __name__ == "__main__":
    main()