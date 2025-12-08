import re

def main():
    data = input("Enter the html code: ")
    print(parse(data))

def parse(s):
    pattern = r'src="(https?://(?:www\.)?youtube\.com/embed/[a-zA-Z0-9_-]+)"'
    if match:= re.search(pattern,s):
        return(match.group(1))
    else:
        return None
    

if __name__ == "__main__":
    main()