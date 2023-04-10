import sys

# Get the number of elements in the array
if __name__ == '__main__':
    n= int(input("Please Enter how many elements:"))

    # Get the elements of the array as input and store them in a list
    arr=list(map(int , input("please separate by space, like - 5 10 30 20:  ").split()))

    # Sort the array in ascending order
    arr.sort()

    # Make a copy of the array
    brr=arr

    # Find the maximum element and remove it from the array
    a=max(brr)
    brr.pop()

    # Find the second largest element
    b=max(brr)

    # If the maximum and second maximum elements are the same, continue to find the third, fourth, fifth, and sixth largest elements
    if (a==b):
        c=max(brr)
        brr.pop()
        d=max(brr)
        if(c==d):
            e=max(brr)
            brr.pop()
            f=max(brr)
            if (e==f):
                g=max(brr)
                brr.pop()
                h=max(brr)
                if(g==h):
                    i=max(brr)
                    brr.pop()
                    j=max(brr)
                else:
                    # Exit if there is no second largest element
                    print(h)
                    sys.exit()
            else:
                print(f)
                sys.exit()
        else:
            print(d)
            sys.exit()
    else:
        print(b)
