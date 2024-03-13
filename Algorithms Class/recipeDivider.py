
#original recipe
originalSugar = 2.5
originalButter = 1.5
originalFlour = 3
originalBatchsize = 24

print("How many cookies would you like to make?")
numOfCookies = float(input())

newBatchCookieSugar = (originalSugar / originalBatchsize) * numOfCookies
newBatchCookieButter = (originalButter / originalBatchsize) * numOfCookies
newBatchCookieFlour = (originalFlour / originalBatchsize) * numOfCookies

print("You wanted to make ", numOfCookies, " cookies")
print("You will need:")
print(newBatchCookieSugar, " cups of sugar")
print(newBatchCookieButter, " cups of butter")
print(newBatchCookieFlour, " cups of flour")
