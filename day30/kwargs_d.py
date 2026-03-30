def values(*args): #()

    print(args)

values("hello",True,1) #multiple number of arguments

def values_2(**kwargs): #{"name":"nandana"}  # takes it as dictionary


    print(kwargs)

values_2(name = "nandana" , course = "DL")      # used to pass multiple number of keyword arguments