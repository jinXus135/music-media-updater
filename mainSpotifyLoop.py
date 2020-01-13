
def see_file():
    filetoopen = open('listOfArtists.txt')


    contents = filetoopen.read()
    print(contents)
    print("\n")
    filetoopen.close()

def add_artist():
    NA = input("Artist: ")

    with open('listOfArtists.txt', 'a') as wf:
        wf.write("\n")
        wf.write(NA)
        wf.close()

def delete_artist():
    DA = input("Aritt to delete: ")
    with open('listOfArtists.txt', 'r') as f:
        lines = f.readlines()
    with open('listOfArtists.txt', 'w') as f:
        for line in lines:
            if line.strip("\n") != DA:
                f.write(line)







end = int(input("1. add artist\n2. remove artist\n3. show list of artists\n4. show new songs this week\n0. to escape this loop"))
while end > 0:
    if end == 1:
        add_artist()
        end = int(input(
            "1. add artist\n2. remove artist\n3. show list of artists\n4. show new songs this week\n0. to escape this loop"))
    if end == 2:
        delete_artist()
        end = int(input(
            "1. add artist\n2. remove artist\n3. show list of artists\n4. show new songs this week\n0. to escape this loop"))
    if end == 3:
        see_file()
        end = int(input(
            "1. add artist\n2. remove artist\n3. show list of artists\n4. show new songs this week\n0. to escape this loop"))
    else:
        float(end)
        end = int(input(
            "1. add artist\n2. remove artist\n3. show list of artists\n4. show new songs this week\n0. to escape this loop"))


