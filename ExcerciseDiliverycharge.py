a=True

while a:

 purchase_cost=float(input("enter the purchase cost:"))

 if purchase_cost>150:

     no_items=int(input("enter the no. of items:"))

     days=int(input("press 1 for same day and 2 for next day:"))

     if no_items<=5:

         if days==1:

            dc=8

            total_cost=purchase_cost+dc

            print("delivery charges:",total_cost)

         elif days==2:

            dc=1.5*no_items

            total_cost=purchase_cost+dc

            print("delivery charges:",total_cost)

     if no_items>5:

         if days==1:

            dc=2.5*no_items

            total_cost=purchase_cost+dc

            print("delivery charges:",total_cost)

         elif days==2:

            dc=1.2*no_items

            total_cost=purchase_cost+dc

            print("delivery charges:",total_cost)

     s=int(input("do you want use again or not press 1y or 2n:"))

     if s==1:

        a=True

     else:

        a=False

