def countWordsFromFile():
    filename = input('Enter the file name:')

    numberOfWords = 0
    
    file = open(filename,'r')
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords+ len(words)
    print('number Of Words:')
    print(numberOfWords)

countWordsFromFile()    
    