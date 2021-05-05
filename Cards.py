import random as r

class deck():

    rank = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
    suit = ['Spades','Clubs','Hearts','Diamonds']
    deck = []
    
    def shuffle(self):
        
        self.deck.clear()
        
        seen = []
        
        while len(self.deck) != 52:
            
            for i in self.rank:
                for j in self.suit:
                
                    i = r.choice(self.rank)
                    j = r.choice(self.suit)

                    item = str(i)+' of '+str(j)
                    
                    if item not in seen:
                        seen.append(item)
                        self.deck.append(item)
        
    def displayAll(self):

        for i in self.deck:
            print(i)
        return

    def getTopCard(self):
        first = self.deck[0]
        return first

    def getBottomCard(self):
        last = self.deck[-1]
        return last

    def removeTopCard(self):

        t = self.deck[0]
        del self.deck[0]
        return t

    def removeBottomCard(self):

        t = self.deck[-1]
        del self.deck[-1]
        return t

    def getRandomCard(self):

        t = r.choice(self.deck)
        return t

    def removeRandomCard(self):

        t = r.choice(self.deck)
        for i in range(len(self.deck)-1):
            if self.deck[i] == t:
                del self.deck[i]
        return t


# Test cases

deck = deck()
deck.shuffle()
deck.displayAll()
print(' ')
card = deck.getRandomCard()
print(card)


