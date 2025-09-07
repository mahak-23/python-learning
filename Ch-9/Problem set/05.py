# 5. Repeat program 4 for a list of such words to be censored.
words = ["donkey", "bustle", "rascal"]

with open("../files/05_PS.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("../files/05_PS.txt", "w") as f:
    f.write(content)