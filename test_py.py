import pytest
#PYTEST, pandas, numpy, matplotlib
#array=(0,1,2,3,4,5,6,7,8,9)

def not_a_prime(num):
    # define a flag variable
    flag = False
    # num = int(input("Please input a positive integer:\n"))
    # num = int(num)
    # prime numbers are greater than 1
    if num <=1:
        flag = True
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break
    # if flag == False:
    #     print("This is a prime!!!")
    # else:
    #     print("Not a prime!!!")
    return str(flag).lower()

@pytest.mark.parametrize("num,is_not_prime", [(0,'true'),(1,'true'),(2,'false'),(3,'false')
                                              ,(4,'true'),(5,'false'),(6,'true'),(7,'false')
                                              ,(8,'true'),(9,'true')])
def test_fnc(num,is_not_prime):
    assert is_not_prime == not_a_prime(num)

# not_a_prime(8)
# if __name__ == "__main__":
#     test_fnc(4)