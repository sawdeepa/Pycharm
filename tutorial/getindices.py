def get_indices(word,char):
    output=[]
    for index, x in enumerate(word):
        if (x == char):
            print(index)
            output.append(index)
    print(output)
    return output
print(get_indices("banana","a") == [1,3,5])

