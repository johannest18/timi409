#TAka við jákvæðri heiltölu í input, köllum hana n
n = int(input("Enter the length of the sequence: ")) # Do not change this line
# Ef talan er 1 skal prenta út lista bara með töluni 1. Ef talan er 2 skal prenta út lista með 1,2 og ef hún er 3 skal prenta út lista með 1, 2 og 3.

listi = [1,2,3]
if n==1:
    listi = [1]
if n==2:
    listi = [1,2]
#hér eru tölur sem skal bæta við aftast við listann
endatala1=1
endatala2=2
endatala3=3
if n>3:
    for bla in range (n):
        endatala4=endatala1 + endatala2 + endatala3
        endatala1= endatala2
        endatala2 = endatala3
        endatala3 = endatala4
        listi.append(endatala3)
print(listi)
    
        
    

#Gera formúlu sem að finnur allar í runu þar sem að runa byrjar á 1 og tölurnar hækka um summu síðustu þriggja talna í runu í hvert skipti.
#Prenta út n- fyrstu tölurnar í formúlunni