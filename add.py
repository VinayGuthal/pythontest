class wrong(Exception): pass


def add(num1,num2):
    num3=0;
    if((num1%1) == 0)and((num2%1) == 0):
        pass
    else:
        raise wrong,"number wrong";
        return num3;
    if(num1 > 0)and(num2 > 0):
        num3=num1+num2;
    else:
        raise wrong,"number wrong";
    return num3;

