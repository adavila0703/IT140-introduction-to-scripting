replacement_words = 'automobile car   manufacturer maker   children kids'.split()
replacement_dict = {}

for index in range(0, len(replacement_words), 2):
    replacement_dict[replacement_words[index]] = replacement_words[index + 1]

sentence = "The automobile manufacturer recommends car seats for children if the automobile doesn't already have one."

for word in replacement_dict:
    sentence = sentence.replace(word, replacement_dict[word])

print(sentence)
