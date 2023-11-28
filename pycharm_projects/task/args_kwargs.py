my_list = []

for i in range(0, 10):
    my_list.append(i)


def args_play(num, num2, *ar):
    for i in ar:
        if i == num:
            print(ar.index(i), "is the index whose number matches number.")

    print("multiple parameters along with args functionality works: ", num2)


def kwargs_play(num1, num2, **kw):
    for key, value in kw.items():
        print(f"{key} {value} from kwargs")

    print("multiple parameters along with kargs functionality works: ", num1, num2)


args_play(5, 1000, *my_list)
kwargs_play(1, 2, **{"name": "Afzhal", "age": 1000, "state": "Tamil Nadu"})

# without default params, 3 params, mn optional, 1 line code, python thing
# also handle in args and kwargs
# python environment variable

