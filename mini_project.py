# #PROJECT 01-(Number Analyzer)

n=int(input('enter a number'))
count=0
if n>0:
    print(n,'is postive')
    if n%2==0:
        print(n,'postive number is also even')
    else:
        print(n,'postive number and also odd')
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print('prime')
    else:
        print('non prime')
elif n==0:
    print(n,'is zero')
else:
    print(n,'is negaative')


#PROJECT 02-(MULTIPLICATION TABLE GENERATOR)
 
p=int(input('enter number'))
choice=input('enter whether u want table from (1 to 10) or (10 to 1)')
if choice=='1 to 10':
    for i in range(1,11):
        print(f'{p}X{i}={p*i}')
elif choice=='10 to 1':
    for i in range(10,0,-1):
        print(f'{p}X{i}={p*i}')
else:
    print('pls put only valid note')


# PROJECT 03-(NUMBER GUESSING GAME)
import random
a=random.randint(1,100)
o=True
while o==True:
    num=int(input('enter the number'))
    if a==num:
        print('Correct')
        o=False
    elif a<num:
        print('Too high')
    else:
        print('Too low')


# PROJECT 04-(STUDENT MARKS ANALYZER)
l=[]
sub1=int(input('enter the number1'))
l.append(sub1)
sub2=int(input('enter the number2'))
l.append(sub2)
sub3=int(input('enter the number3'))
l.append(sub3)
sub4=int(input('enter the number4'))
l.append(sub4)
sub5=int(input('enter the number5'))
l.append(sub5)
total_marks=sum(l)
print('THE TOTAL MARKS',total_marks)
maximum_marks=max(l)
print('MAXIMUM MARK IS',maximum_marks)
minimum_marks=min(l)
print('MINIMUM MARK IS',minimum_marks)
percentage=((sum(l))/500)*100
print(percentage)
if percentage>=33:
    print('Pass')

    if percentage>=90 and percentage<=100:
        print('Ex')
    elif percentage<90 and percentage>=80:
        print('A')
    elif percentage<80 and percentage>=70:
        print('B')
    elif percentage<70 and percentage>=60:
        print('C')
    elif percentage<60 and percentage>=50:
        print("D")
    else:
        print("F")
else:
    print('fail')


# PROJECT 05-(SHOPPING CART)

print('''chosse 1 if you want to add item in cart
chosse 2 if you want to view cart
chosse 3 if you want to remove item from cart
chosse 4 if  you want to know the total price of products in the cart
chosse 5 if your shopping is finish ''')
cart={}
choice=int(input('enter number in between :'))
while choice!=5:
    if choice==1:
        item=input('enter item name')
        item_price=int(input('enter item price name:'))
        cart[item]=item_price
    elif choice==2:
        if len(cart)==0:
            print('your cart is empty')
        else:
            for i in cart:
                print(i,':',cart[i])
    elif choice==3:
        list_of_items=cart.keys()
        item=input('enter the item u want to remove from the cart')
        if item in list_of_items:
            cart.pop(item)
        else:
            print('This item is not in cart')
    elif choice==4:
        price_list=cart.values()
        print('the total amount of the cart items:',sum(price_list))
    else:
        print('Invalid choice')
    choice=int(input('enter 5 if shopping is finsh'))
print('Thankyou for shopping')


#PROJECT 06-(HINDI-ENGLISH DICTIONARY)
hindi_vocabulary = {
    "जिज्ञासा (Jigyasa)": "Curiosity or a strong desire to know or learn something",
    "आकांक्षा (Aakanksha)": "An ambition, desire, or aspiration",
    "प्रतिबिंब (Pratibimb)": "A reflection or image cast back",
    "सहानुभूति (Sahanubhuti)": "Empathy or compassionate understanding",
    "परिश्रम (Parishram)": "Hard work, diligence, or industrious effort",
    "वात्सल्य (Vatsalya)": "Unconditional parental or tender affection",
    "अनुभूति (Anubhuti)": "Deep perception, realization, or intuitive feeling",
    "गंतव्य (Gantavya)": "Destination or targeted goal",
    "आत्मीयता (Aatmiyata)": "Warm intimacy, soulfulness, or close affinity",
    "दृढ़ता (Dridhta)": "Perseverance, determination, or resilience",
    "संवेदना (Samvedna)": "Sensitivity, compassion, or emotional sensation",
    "संतोष (Santosh)": "Contentment, satisfaction, or peace of mind",
    "सुवासित (Suvasit)": "Fragrant, aromatic, or sweetly scented",
    "विश्राम (Vishram)": "Rest, tranquility, or relaxation",
    "कृतज्ञता (Kritagyata)": "Gratitude or heartfelt thankfulness",
    "नवोन्मेष (Navonmesh)": "Innovation, fresh brilliance, or new initiative",
    "अद्वितीय (Advitiya)": "Unique, peerless, or unmatched",
    "उल्लास (Ullas)": "Exuberant joy, delight, or festivity",
    "सामंजस्य (Samanjasya)": "Harmony, balance, or perfect accord",
    "विहंगम (Vihangam)": "Panoramic, majestic, or a bird's-eye view"
}
print('''
chosse 1 if you want to insert a word and its meaning in the dictionary
chosse 2 if you wnat to search for a word 
chosse 3 if u want to dispaly all the  words 
chosse 4 if u want to exit from this dictionary
''')
choice=int(input('enter the number as per the function you want to execute'))
while choice!=4:
    if choice==1:
        word=input('enter word u want to enter')
        meaning=input('enter the meaning of word you wat to enter in the vocabulary dictionary')
        hindi_vocabulary[word]=meaning
        print('word added successfully')
    if choice==2:
        word=input('enter the word which meaning u want to know')
        list_of_words=hindi_vocabulary.keys()
        if word in list_of_words:
            print(word,'meaning is',hindi_vocabulary[word])
        else:
            print('this word is not in hindi_vocabulary')
    if choice==3:
        list_of_words=hindi_vocabulary.keys()
        print(list_of_words)
    choice=int(input('enter 4 if you want to exit'))
print('Dictionary closed.')
    

#PROJECT 07-MINI ATM
print('=====ATM=====')
balance=10000
print('''chosse \'A\' to Check Balance
chosse \'B\' to Deposit Money
chosse \'C\' to Withdraw Money 
chosse \'D\' to Exist
''')
choice=input('enter the digit as per function you want to execute')
while choice!='D':
    
    if choice=='A':
        print('The current account balance',balance)
    elif choice=='B':
        deposit_amount=int(input('enter the amount you want to deposit'))
        if deposit_amount>0:
            balance+=deposit_amount
            print('The updated balance',balance)
        else:
            print('don\'t put non zero and negative amount')
    elif choice=='C':
        withdraw_money=int(input('enter the amount you want to withdraw'))
        if withdraw_money>0:
            if withdraw_money<=balance:
                balance-=withdraw_money
                print('The updated balance',balance)
        else:
            print('Insufficent balance')
    else:
        print('Amount must  be greater than 0')
    choice=input('enter the alphabet as per function you want to execute')
print('Thank you for usinng the ATM')


#PROJECT 08-(MINI QUIZ)
print(''' EVERY CORRECT ANSWER GET YOU 5 NUMBER
QUESTION 01 what is the sum of two smallest prime numbers ?
(A)5          (B)2
(C)10         (D)4
QUESTION 02 what  is keyword?
(A)keywords are the reserved words in python which have specific feeling.
(B)keywors define the data type of any element.
(C)keyword are the symbols by which any operation got operated.
(D)keyword are prime numbers.
QUESTION 03  which one is operator in the following?
(A)int             (B)'+='
(C)input           (D)print
QUESTION 04  what is decorator?
(A)//divison         (B)abstractionmethod
(C)#hastag          (D)()puntuators
QUESTION 05 how many variables are in python?
(A)3                (B)4
(C)6                (D)2''')
solution1=input('enter the solution') 
solution2=input('enter the solution')
solution3=input('enter the solution')
solution4=input('enter the solution')
solution5=input('enter the solution')
total_question=5
correct=0
incorrect=0
score=0
if solution1=='A':
    print('correct')
    correct+=1
    score+=5
else:
    print('incorrect')
    incorrect+=1
if solution2=='A':
    print('correct')
    correct+=1
    score+=5
else:
    print('incorrect')
    incorrect+=1
if solution3=='B':
    print('correct')
    correct+=1
    score+=5
else:
    print('incorrect')
    incorrect+=1
if solution4=='B':
    print('correct')
    correct+=1
    score+=5
else:
    print('incorrect')
    incorrect+=1
if solution5=='D':
    print('correct')
    correct+=1
    score+=5
else:
    print('incorrect')
    incorrect+=1
print("CORRECT ANSWER",correct)
print("WRONG ANSWER",incorrect)
print("FINIAL SCORE",score)


# PROJECT 09-(SNAKE,WATER,GUN GAME)

import random
print('GUN,SNAKE,WATER')
choices=['GUN','SNAKE','WATER']
computer=random.choice(choices)
print(computer)
user=input('enter the option')
if user not in choices:
    print('invalid input')
elif (user=='GUN' and computer=='SNAKE') or (user=='WATER' and computer=='GUN') or (user=='SNAKE'and computer=='WATER'):
    print('u win')
elif(user==computer):
    print('tie!')
else:
    print('better luck next time')