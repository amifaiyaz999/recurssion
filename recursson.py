n = int(input("Enter n (try 3 or 5):"))
guess = input("how much times does countdown call itself for n = "+str(n)+"?")
input("recussion _ watch each call press enter to run")
def countdown(num):
    print("call --n =*, num")
    if num > 0 :
        countdown(num-1)
countdown(n)
print("call=",n+1,"your guess:",guess,"->0(n)")

input('watch calls grow with n press enter')
for size in[5,10,100]:
    print("n=",size,"calls =",size+1,"=> 0(n)")