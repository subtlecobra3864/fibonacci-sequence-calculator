#Calculate fibonacci sequence to 100th term.






def CalculateFibonacci():

    count = 0
    prevNum = 1
    curNum = 1
    sequence = []
    
    print("Calculating Fibonacci sequence to the 100th number")
    for count in range(0, 99):#The calculation.
        count += 1
        nextNum = prevNum + curNum
        print(sequence)
        sequence.append(nextNum)
        curNum = nextNum
        nextNum = 0
        prevNum = curNum - prevNum



    #User Linear Search to find nth term in the sequence(e.g nth term being 42).
    search(sequence)

def search(sequence):

    n = int(input("what is the number you want to find in the sequence?"))

    for i in range(len(sequence)):

        if sequence[i] == n:
            return i
        else:
            print("num not found")

    return -1




        
        
CalculateFibonacci()
