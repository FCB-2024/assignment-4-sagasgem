import sys

def main():
    if len(sys.argv) != 2:
        print("python antiprime.py <numero>")
        return

    x = int(sys.argv[1])

    def cdiv(n):
        y = 0
        i = 1
        while (i <= n):
            if (n % i == 0):
                y += 1  
            i += 1
        return y

    def is_ap(n):
        actual = cdiv(n)
        i = 1
        while i < n:
            if cdiv(i) >= actual:
                return False  
            i += 1
        return True  

    if is_ap(x):
        print("anti-prime")
    else:
        print("not anti-prime")  
        
if __name__ == "__main__":
    main()
