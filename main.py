desired_index = int(input("which n'th prime number would u like ? \n"))
prime_list = [2]
init=3
while len(prime_list)<desired_index:
    for i in prime_list:
        if init % i == 0:
            break
    else: prime_list.append(init)
    init+=2

print(prime_list[-1])