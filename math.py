import math
B="IF(A>702;182,316*(if ( 2>3;5; 10) - 0,108*(A-702)/14)*(A-702)^1,5;0)"

#input function, value a. return value b
def fun_math(str_function, a):
    str_function = str_function.lower().replace(",", ".").replace("^", "**").replace("sqrt", "math.sqrt")
    str_function_new = ""
    for idx in str_function:
        if idx != " ":
            str_function_new +=idx
#Excute math
    return eval(fun_get_value_if(str_function_new, a))
#case all condition IF.
#input function, value a.
#output value condition IF eg: IF(true, gt1, gt2) ==> gt2
def fun_get_value_if(str_function, a):
    print("Input:")
    print(str_function)
    indexIf = 0
# if mark function contain IF action substring return char ()
    if "if(" in str_function:
        index = str_function.index("if")+ 2
        for x in str_function[str_function.index("if")+ 2: len(str_function)]:
            index +=1
            if x == "(":
                indexIf +=1
            elif x == ")":
                indexIf -=1
            if indexIf == 0:
                str_replate = str_function[str_function.index("if("):index]
                new_str = str_function[(str_function.index("if(")+ 3):(index-1)]
#IF mark function contain if. recursive fun_get_value_if
                if "if(" in new_str:
#replate all mark IF ==> value clause true 
                    new_str = str_function.replace(str_replate, fun_get_value_if(new_str, a))
                str_arr = new_str.split(";")
                if len(str_arr) == 3:
#excute clause if.
                    if eval(str_arr[0]):
                        str_function = str_function.replace(str_replate, str_arr[1])
                    else:
                        str_function = str_function.replace(str_replate, str_arr[2])
                else:
                    print("sai cu phap")
                    print(new_str)
                return str_function
    else:
        return str_function

fun_math(B, 704)