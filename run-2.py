import sys

def main():
    if len(sys.argv)<2:
        print("Please pass the dataset name...")
        return
    title = sys.argv[1]
    print(title)

if  __name__ == '__main__':
    main()