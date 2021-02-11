n = int(input())
cards = []
miss = []

for i in range(1, n+1):
    cards.append(i)   
    
for i in range(0, n-1):
    num = int(input())
    miss.append(num)  

for card in miss:
    cards.remove(card) 
    
print(cards[0])

