def is_prime(num):
    prime=True
    for i in range(2,num//2+1):
        if num%i==0:
            prime=False
            break
        else:
            prime=True
            continue
    return prime

def are_relatively_prime(num1, num2):
    are_relative=True
    if num1>num2:
        for i in range(2,num1//2+1):
            if num1%i==0:
                if num2%i==0:
                    are_relative=False
                else:
                    continue
            else:
                continue
    else:
        for i in range(2,num2//2+1):
            if num1%i==0:
                if num2%i==0:
                    are_relative=False
                else:
                    continue
            else:
                continue
    return are_relative

def primes(num):
    list_prime=[]
    for i in range(2,num+1):
        if is_prime(i)==True:
            list_prime.append(i)
        else:
            continue
    return list_prime

def prime_decomposition(num):
    list_decomposition=[]
    list_prime=primes(num)
    for i in list_prime:
        while num%i==0:
            num=num/i
            list_decomposition.append(i)
    return list_decomposition
