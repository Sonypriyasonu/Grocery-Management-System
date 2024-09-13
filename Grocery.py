'''
Grocery application
Build a console-based application for grocery management system. 
This application should have functionality such as add items, view items, 
update items, delete items.
 
Create the application such a way that it should handle exceptions.
Validate the items that are been added, should not allow any duplicates.
Items quantity can also be updated once the item has been added.'''

global g_items,cart,users
g_items={} #eggs,milk,apple,soap,tooth paste, curd,bread
cart={}
users={"user1":111,"user2":222}


class InvalidInputError(Exception):
    "Raised when quantity is negative"
    pass
class ItemNotFound(Exception):
    "Raised when item not found"
    pass
class ItemExistsError(Exception):
    "Raised when item already exists"
    pass
class IncorectPassword(Exception):
    "Raised when password is wrong"
    pass
class UsernameNotAvailable(Exception):
    pass
class IncorrectPin(Exception):
    pass
def addItems(a):        #Adding items in grocery
    global g_items
    while True:
        name=input("\nEnter the name of item to add or '*' to exit: ").lower()
        
        try:
            if name=='*':
                break
            elif name not in a:                          #items will not added if they are in grocery
                p=float(input("Enter the price of item: "))
                while(1):                                     
                    try:
                        q=int(input("Enter the quantity: "))
                        if q>=0:
                            break
                        elif q<0:
                            raise InvalidInputError              #if quantity is negative then exception will be raised
                    except InvalidInputError:
                        print("Exception occured: Invalid input. \n\nPlease enter positive number")        
                a[name]=[p,q]
                print(f"{name} is successfully added to grocery items")
            else:
                raise ItemExistsError
        except ItemExistsError:
            print(f"Exception raised: {name} already exists in grocery")
    
        
def updateItems():              #updating items
    global g_items
    try:
        a=input("Enter item you want to edit: ")
        
        if a.lower() in g_items:                             # item converted to lower case
            np=float(input("Enter the price of item: "))
            while(1):
                try:
                    nq=int(input("Enter the quantity: "))    #enter quantity will be asked until u enter correct quantity
                    if nq>=0:
                        break
                    elif nq<0:
                        raise InvalidInputError               #if quantity is negative then exception will be raised
                except InvalidInputError:
                    print("\nException occurred: Invalid input. \n\nPlease enter positive number")     
            g_items[a]=[np,nq]
            print(f"{a} updated successfully.")
        else:
            raise ItemNotFound                              #if item not found exception will be raised
    except ItemNotFound:
        print("\nException occurred: Item not found in grocery")
        
def deleteItems():                    #deleting items
    global g_items
    try:
        a=input("Enter item you want to delete: ").lower()       #item converted to lower case
        if a.lower() in g_items:
            g_items.pop(a)                                       #item will be deleted
            print("Item deleted successfully")
        else:
            raise ItemNotFound                                  #if item not found exception will be raised
    except ItemNotFound:
          print("\nException occurred: Item not found in grocery")    
        
def print_table():
    print("{:<15}{:<10}{:<10}".format('Item','Price','Quantity\n---------------------------------' ))
    for key,value in g_items.items():
        print("{:<15}{:<10}{:<10}".format(key,value[0],value[1] ))

def print_cart():
    print("{:<15}{:<10}{:<10}{:<15}".format('Item','Quantity','Price','Total price\n----------------------------------------------' ))
    tc=0
    for key,value in cart.items():
        if key in g_items:
            p=g_items[key][0]
            tp=p*value
            tc+=tp
            print("{:<15}{:<10}{:<10}{:<15}".format(key,value,p,tp))
    print("\nTotal cost of your cart: {} rupees".format(tc))
def grocery():
    global g_items
    while True:
        try:
            print("\n1: View Grocery items and quantity")
            print("2: Add items")
            print("3: update items")
            print("4: Delete items")
            print("Enter any number to Exit\n")
            n=int(input("Enter number: "))
            if n==1:
                print_table()
            elif n==2:
                addItems(g_items) 
            elif n==3:
                updateItems()
            elif n==4:
                deleteItems()               
            else:
                print("Exited")
                break
        except ValueError:
           print("Exception occured: Invalid input. Please enter number") 
           
def addcart():
    global g_items,cart
    print("Items available")
    print_table()
    while True:
        name=input("Enter item you want to add to cart or '*' to exit: ").lower()
        if name=='*':
            break
        else:
            try:
                if name in g_items:
                    while(1):
                        try:
                            q=int(input("Enter Quantity: "))
                            if q>g_items[name][1]:
                                print("Sorry, we don't have enough quantity")
                                break
                            elif q<0:
                                raise InvalidInputError
                            else:
                                if name in cart:
                                    cart[name]+=q
                                else:
                                    cart[name]=q
                                print(f"{q} {name} added to your cart") 
                                g_items[name][1]-=q
                                break                   
                        except InvalidInputError:
                            print("\nException occurred: Invalid input. \n\nPlease enter positive number") 
                else:
                    raise ItemNotFound
            except ItemNotFound:
                print("\nException occurred: Item not found in grocery")
                                    
def updatecart():
    print_cart()
    item=input("\nEnter item you want to update: ").lower()
    while(1):
        try:
            if item in cart:
                q=int(input("Enter new quantity: "))
                if q<0 :
                    raise InvalidInputError
                elif q>g_items[item][1]:
                    print("Sorry, we don't have enough quantity")
                    break
                else:
                    g_items[item][1]+=cart[item]        #adding cart quantity to g_items 
                    cart[item]=q                        #updating quantity with new quantity
                    g_items[item][1]-=q                 #removing new quantity from g_items
                    print("\nQuantity updated successfully")
                    break
            else:
                raise ItemNotFound
        except InvalidInputError:
            print("\nException occurred: Invalid input. \n\nPlease enter positive number")
        except ItemNotFound:   
            print("\nException occurred: Item not found in cart")
                
def deletecart():
    item=input("Enter item you want to delete from cart: ").lower()
    try:
        if item in cart:
            g_items[item][1]+=cart[item]          #adding cart quantity to g_items
            cart.pop(item)
            print("Item deleted successfully")
        else:
            raise ItemNotFound
    except ItemNotFound:
        print("\nException occurred: Item not found in cart")
        
def checkout():
    print_cart()
    cart.clear() 
          
def Customer_cart():
    global g_items
    while True:
        try:
            print("\n1: View cart")
            print("2: Add to cart")
            print("3: update cart")
            print("4: Delete cart")
            print("5: Checkout")
            print("Enter any number to Exit\n")
            n=int(input("Enter number: "))
            if n==1:
                print_cart()
            elif n==2:
                addcart()
            elif n==3:
                updatecart()
            elif n==4:
                deletecart() 
            elif n==5:
                checkout()
                break              
            else:
                print("Exited")
                cart.clear()
                break
        except ValueError:
           print("Exception occured: Invalid input. Please enter number")         

'''def buyG():
    global g_items,cart
    print("Items available")
    print_table()
    c=0
    while True:
        a=input("Enter item you want to buy or 'd' to exit: ").lower()
        if a=='d':
            break
        elif a in g_items:
            k=int(input("Enter Quantity: "))
            if k>g_items[a][1]:
                print("Sorry, we don't have enough quantity")
            else:
                c+=g_items[a][0]*k
                g_items[a][1]-=k
                print(f"{k} {a} added to your cart")
        else:
            print(f"{a}s not available")
            
    print(f"\nTotal cost of your purchase: {c} rupees")'''
            
    
def shop():
    global users
    while True:
        try:
            print("\nMenu")
            print("1.Update Grocery Items(owner)")
            print("2.Buy groceries(customer)")
            print("Enter any number to exit")
            n=int(input("Enter number: "))
            if n==1:
                print("Welcome to Grocery store\n")
                user=input("Enter username here: ").lower()
                count=0
                while True:
                    try:
                        #user=input("Enter username here: ").lower()
                        if user=="sony":
                            p=input("Enter your Password here: ")
                            if p=="shop123":
                                grocery()
                                break
                            else:
                                count+=1
                                raise IncorectPassword
                        else:
                            print("Incorrect Username. Access denied")
                            break
                    except IncorectPassword:
                        if count==3:
                            print("Too many incorrect login attempts. Try later")
                            break
                        else:
                            print("Exception occured: Incorrect password. Please try again")                          
            elif n==2:
                print("\nWelcome to Grocery store\n")
                print("1: New customer" )
                print("2: Customer login")
                n=int(input("Enter number here: "))
                if n==1:
                    try:
                        while(1):
                            try:
                                u=input("Enter username: ").lower()
                                if u not in users:
                                    print("Username created successfully.\n")
                                    n=int(input("Enter your PIN here: \n"))
                                    c=0
                                    while(1):
                                        try:
                                            k=int(input("Enter your PIN again: "))
                                            if n==k:     
                                                users[u]=n
                                                print("Credentials created successfully.\n")
                                                break
                                            else:
                                                c+=1
                                                raise IncorrectPin
                                        except IncorrectPin:
                                            if c==3:
                                                print("\nToo many incorrect PIN attempts. Try later")
                                                break
                                            else:
                                                print("Exception occurred: Invalid PIN")  
                                    break       
                                else:
                                    raise UsernameNotAvailable
                            except UsernameNotAvailable:
                                print("Username not available")
                                
                    except ValueError:
                        print("Exceptin occurred: Invalid input.")
                elif n==2:
                    user=input("Enter username here: ").lower()
                    count=0
                    while True:
                        try:
                            if user in users:
                                p=int(input("Enter your PIN here: "))
                                if users[user]==p:
                                    Customer_cart()
                                    break
                                else:
                                    count+=1
                                    raise IncorectPassword
                            else:
                                print("Incorrect Username. Access denied")
                                break
                        except IncorectPassword:
                            if count==3:
                                print("Too many incorrect login attempts. Try later")
                                break
                            else:
                                print("Exception occurred: Incorrect PIN. Please try again")  
                    print("\nThank you. Please visit again")
            else:
                print("Exited")
                break
        except ValueError:
            print("Exceptin occurred: Invalid input. Please enter number")
shop()
