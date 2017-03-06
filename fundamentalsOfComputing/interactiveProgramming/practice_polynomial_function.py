def poly_eval(x):
    y = -5*x**5 + 69*x**2 - 47
    return y 

val_1 = poly_eval(0)
val_2 = poly_eval(1)
val_3 = poly_eval(2)
val_4 =poly_eval(3)
print (max(val_1,val_2,val_3,val_4)) #returns maximum of the list