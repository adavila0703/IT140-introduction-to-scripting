"""
7.8 LAB: Word frequencies (lists)

"""

# import csv


# with open('test.csv') as file:
#     lines = csv.reader(file, delimiter=',')

#     container = {}

#     for line in lines:
#         for word in line:
#             if container.get(word) == None:
#                 container[word] = 1
#             else:
#                 container[word] += 1

#     for word in container:
#         print(word, container[word])


"""
7.9 LAB: Sorting TV Shows (dictionaries and lists)


input
20
Gunsmoke
30
The Simpsons
10
Will & Grace
14
Dallas
20
Law & Order
12
Murder, She Wrote

"""


file_name = input()
file = open(file_name)
lines = file.readlines()
show_data = {}
titles = []

for index in range(0, len(lines) - 1, 2):
    seasons = int(lines[index].strip())
    title = lines[index + 1].strip()
    print(title)
    titles.append(title)

    if show_data.get(seasons) == None:
        show_data[seasons] = [title]
    else:
        show_data[seasons].append(title)

sorted_dict = {}

for key in sorted(show_data.keys()):
    sorted_dict[key] = show_data[key]

new_file = open('output_keys.txt', 'w+')

for key in sorted_dict:
    name = sorted_dict[key]

    if len(name) > 1:
        value = '; '.join(name)

        new_file.writelines(f"{key}: {value}\n")
        continue

    value = str(name).replace(
        '[', '').replace(']', '').replace("'", "")
    new_file.writelines(f"{key}: {value}\n")

titles.sort()

new_file = open('output_titles.txt', 'w+')

for title in titles:
    new_file.writelines(f"{title}\n")
