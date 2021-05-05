
class readingLevel:
    
    passage = '''



              '''  
    sentences = []
    sentenceCount = 0

    words = []
    wordCount = 0

    syllables = 0
    gradeLevel = 0
    readingLevel = 0
    
    def toSentences(self):
        self.sentences = self.passage.split('. ')

        for i in self.sentences:
            self.sentenceCount += 1
        

    def toWords(self):
        self.words = self.passage.split()
        self.words = [x for x in self.words if not any(x1.isdigit() for x1 in x)]

        for i in self.words:
            self.wordCount += 1
        

    def toSyllable(self, theWord):
        vowels = 'aeiouy'
        theWord = theWord.lower()

        if theWord[0] in vowels:
            self.syllables += 1
            
        for i in range(1, len(theWord)):
            if theWord[i] in vowels and (theWord[i-1] not in vowels):
                self.syllables += 1        

        if theWord.endswith('e'):
            self.syllables -= 1
        if self.syllables == 0:
            self.syllables += 1

    def totalSyllables(self):

        for i in self.words:
            self.toSyllable(i)
        

    def fleschKincaid(self):

        self.toSentences()
        self.toWords()
        self.totalSyllables()
        
        self.readingLevel = ((206.835) - (1.015 * (self.wordCount / self.sentenceCount)) - (84.6 * (self.syllables / self.wordCount)))
        self.gradeLevel = ((.39*(self.wordCount / self.sentenceCount)) + (11.8*(self.syllables / self.wordCount)) - (15.59))

        print(self.passage)
        
        print("\n[90-100] Very Easy")
        print("[80-89] Easy")
        print("[70-79] Fairly Easy")
        print("[60-69] Standard")
        print("[50-59] Fairly Difficult")
        print("[30-49] Difficult")
        print("[0-29] Very Confusing")

        print("\nFlesch-Kincaid Readability Ease Value: ",self.readingLevel)
        if self.gradeLevel > 12:
            print("Flesch-Kincaid Readability Grade Level: ",self.gradeLevel," --> "+str((int(round(self.gradeLevel)))-(12))+" years into university")
        else:
            print("Flesch-Kincaid Readability Grade Level: ",self.gradeLevel," --> "+str(int(round(self.gradeLevel)))+"th grade")

        ##input("Press ENTER to quit")
        

rL = readingLevel()
rL.fleschKincaid()

