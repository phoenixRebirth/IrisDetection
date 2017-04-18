
class test():
    def __init__(self, *args, **kwargs):
        for elt in args:
            print(elt)
        # print(args)
        # print(*args)


if __name__ == '__main__' :
    a = [7, 9, 11]
    b = {'a':2 ,'b':3 ,'c':4}
    #test(*a)
    test(b)
    # test(*[7, 9, 11])
