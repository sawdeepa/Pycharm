
text = "today is a great day"
print(text.upper())
print(text.capitalize())
print(text.title())

print("great" in text)
print(text.startswith("great"))
print(text.endswith("day"))

text2 = "      today is a great day\t"
print("--->{}<---".format(text2))
print("--->{}<---".format(text2.strip()))
print("--->{}<---".format(text2.rstrip()))
print("--->{}<---".format(text2.lstrip()))

text3="ramesh,223,rsannareddy@gmail.com,9885970033"

print(text3.split(','))

name,eid,email,mobile = text3.split(',')


words = ["hello","how","are","you"]

print(".".join(words))
print(",".join(words))
print("\t".join(words))
print("_____".join(words))
