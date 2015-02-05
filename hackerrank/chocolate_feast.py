#chocolate feast
#M money, C price of chocolate, W wrappers to get 1 chocolate for free
#2 <= M <= 100,000, 1 <= C <= M, 2 <= W <= M

T = int(raw_input())

for i in range(0,T):
    money,price,number = [int(x) for x in raw_input().split(' ')]
    print (' given {} money, chocolate price {} and if you have {} # of wrappers, you get 1 chocolate for free').format(money, price,number)


#state 0
    wrappers, chocolate = 0, 0

#state 1
    chocolate += money//price

#state 2
    eaten = chocolate #where eaten is a running counter for total chocolate
    wrappers += chocolate
    chocolate = 0 #assume you always eat all the chocolate

    def recurse(number,chocolate,wrappers, eaten):
        print "you ate " + str(eaten) + " chocolates"

        #enough to cash in
        if wrappers >= number:
            chocolate += wrappers//number
            wrappers -= number
            print "you have " + str(wrappers) + " wrappers left"
            eaten += chocolate
            wrappers += chocolate
            chocolate = 0
            print "you ate " + str(eaten) + " chocolates"
            recurse(number,chocolate,wrappers, eaten)
            return chocolate, wrappers, eaten

        #not enough to cash in
        elif wrappers < number:
            print "answer = " + str(eaten)
            return

    C = recurse(number,chocolate,wrappers, eaten)




    #Sample input

    #3
    #10 2 5
    #12 4 4
    #6 2 2

   # Sample Output

   # 6
   # 3
   # 5
