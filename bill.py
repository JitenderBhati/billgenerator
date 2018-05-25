class product:
    
    def addProduct(productId, productName, quantity, price):
        dicti={};
        dicti['price'] = price;
        dicti['stock'] = quantity;
        dicti['name'] = productName;
        items[productId].update[dicti];
    items = {123: {'price': 4.3, 'stock':8, 'name': 'Apple'},
             132: {'price': 5.5, 'stock':7, 'name': 'Banana'},
             321: {'price': 3, 'stock':6, 'name': 'Grapes'}};
    
class checkoutregister:
    def checkouts(self, totalRecieved, totalPrice, totalPrices, bags):
        objProduct = product();
        print();
        print();
        print("-- Final Reciept -- ".center(80));
        
        for i in bags:
           print(objProduct.items[i]['name'] +", " + str(objProduct.items[i]['stock']) + "        " + " $" + str(objProduct.items[i]['price']));
        print();
        print("Total amount due: $" + str(totalPrices));
        print("Amount recieved: $" + str(totalRecieved));
        print("Change Given: $" + str(abs(totalPrice)));
        print("Thank you for shopping");
        print();
        print("Visit Again");
        
    
flag = True;

print("---- Welcome to FedUni -----".center(80));
print();
print("Press Any Option down below");
print("1) Add Product");
print("2) Bill Generator")
print("3) Exit");
option = int(input("Choose Any Option(1-3): "));

if(option is 1):
        product = product();
        productId = int(input("Enter the product Id: "));
        productName = input("Enter the product name: ");
        price = int(input("Enter the Price of Product"));
        quantity = int(input("Enter the total quantity: "));
        product.addProduct(productId, productName, quantity, price);
        print("Product Added Successfully");
        
if(option is 2):
        bag = [];
        cost = [];
        totalRecieved = 0;
        dummy = False;
        while(flag or dummy):
            productId = int(input("Please enter the barcode of your item: "));
            objProduct = product();     
            for key in objProduct.items:        
                if (key == productId):            
                    bag.append(key);
                    cost.append(int(objProduct.items[key]['price']));
                    print(objProduct.items[key]['name'] + ", " + str(objProduct.items[key]['stock']) + " - $" + str(objProduct.items[key]['price']));
                    print();
                    option = input("Would you like to scan another product? (Y/N) ");   
                    if(option is 'y'):
                        flag = True;
                    elif(option is 'n'):
                        amount = [];
                        flag = False;
                        totalPrice = 0;
                        totalPrices = 0;
                        for i in cost:
                            totalPrice+=i;
                            totalPrices+=i;
                        while(totalPrice > 0):
                            print("Payment due: $" + str(totalPrice) + ". " , end=" ");
                            money = int(input("Please enter an amount to pay: $"));
                            if money >= 0:
                                amount.append(money);
                                totalPrice = totalPrice - money;
                            else:
                                print("We don`t accept negative money!");        
                        for i in amount:
                            totalRecieved = totalRecieved + i;
                        objCheckout = checkoutregister();
                        bags = tuple(bag);
                        objCheckout.checkouts(totalRecieved, totalPrice, totalPrices, bag);
                        print();
                        options1 = input("Want to Generate Another Bill");
                        if(options1 is 'y'):
                            dummy = True;
                        else:
                            dummy = False;
                    else:
                        print("Invalid!");
if(option is 3):
         System.Exit();



