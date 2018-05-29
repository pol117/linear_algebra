def f1():
    print(1/0)

def f2():
    try:
        f1()
    except Exception as e:
        e.args += ('more info',)
        raise  # don't raise e !!!

f2()
