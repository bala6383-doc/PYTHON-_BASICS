text = "I love python"
words = text.split()
rev = ""
for word in words:
    rev = word[::-1] + " " + rev
    print(rev)
