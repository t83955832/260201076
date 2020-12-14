def binary_to_dec(b):
    d = 0
    b_rev = str(b)[::-1] # reverse
    for i in range(len(b_rev)):
        d += (2**i)*int(b_rev[i])
    return(d)



def dec_to_binary(d):
    b = ""
    while d > 0:
        b += str(d%2)
        d //= 2
    return(b[::-1])

def main():
    b = "10010"
    print(binary_to_dec(b))
    d = 18
    print(dec_to_binary(d))
main()


