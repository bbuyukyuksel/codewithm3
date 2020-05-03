def is_prime(num):
    if num in [2,3]:
        return True
    for i in range(2,(num//2)+1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    index = 0
    current_num = 2
    target_index = 10001
    while True:
        if is_prime(current_num):
            index += 1
            print("{:<6}. prime num '{:<6}' is detected!".format(index, current_num), end='\r')
            if target_index == index:
                break
        current_num+=1
