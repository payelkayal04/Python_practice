ItemsInCart = 0
#2 items will be added into the cart

if ItemsInCart != 2:
    #raise Exception("not matching")
    pass
assert(ItemsInCart == 0)

try:
    with open('filelog.txt', 'r') as file:
        file.read()
except:
    print("failures in try block")

try:
    with open('text.txt','r') as file:
        file.read()
except Exception as e:
    print(e)

finally:
    print("Cleaning up resources")