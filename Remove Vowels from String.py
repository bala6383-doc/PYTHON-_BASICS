text = "education"
result = ""
for ch in text:
    if ch not in "aeiou":
        result += ch
        print(result)
