### LECTURE 2 CODE NOTES ###

n = 100
%cpaste
for x in range(100000000):
    print(n)
    if n % 2 == 0:
        #n is even
        n = n / 2.0
    elif n % 2 == 1:
        n = n * 3 + 1

    if n == 1:
        break;
--

4 2 1




