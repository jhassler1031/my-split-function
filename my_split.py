
def my_split(sentence):
    word_list = [""]
    index = 0

    for letter in sentence:
        if letter == " ":
            index += 1
            word_list.append("")
        else:
            word_list[index] = word_list[index] + letter
    return word_list


my_sentence = "This is a test."


print(my_split(my_sentence))
print(my_sentence.split())
