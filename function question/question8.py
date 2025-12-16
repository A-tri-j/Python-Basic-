# general way even number print in a range 

# def even_genarate(limit):
#     for i in range(2,limit+1,2):
#         print(i)


# even_genarate(10)


# use yield method 

def even_genarate(limit):
    for i in range(2,limit+1,2):
        yield i


for num in even_genarate(10):
    print(num)