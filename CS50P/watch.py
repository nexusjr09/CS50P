import re

def main():
    print(parse(input("Enter the html code:")))
def parse(s):
    pattern = r'src="(https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+))"'
    if match:= re.search(pattern,s):
        two = match.group(1)
        return (f"https://youtu.be/{two}")
    else:
        return None


if __name__ == "__main__":
    main()

#https://youtu.be/xvFZjo5PgG0
#https://www.youtube.com/embed/xvFZjo5PgG0
