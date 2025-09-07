# 6. Write a program to mine a log file and find out whether it contains 'python'.

with open("../files/06_PS.txt", "r") as f:
    content = f.read()
    isTrue="python" in content
    print(f"Log contains 'python' word: {isTrue}")
