try:
    f = open("demo.txt", "r")
    print(f.read())
except Exception as readingError:
    print(readingError)