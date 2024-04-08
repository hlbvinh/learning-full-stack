##varible
##Day 2: 30 Days of python programming
first_name = "Huynh"
last_name = "Vinh"
full_name = "Huynh Le Bao Vinh"
country = "Viet Nam"
city = "HCM"
age = "26"
year = "2024"
is_married = True
is_true = False
is_light_on = False
var1 = 0 ; var2 = 1 ; var3 = 3

print(type(is_light_on))
print(len(first_name))
print(len(first_name)==len(last_name))

num_one = 5
num_two = 4
tong = num_one + num_two
hieu = num_one - num_two
tich = num_one * num_two
thuong = num_one / num_two


print(divmod(num_one, num_two))
exp = pow(num_one, num_two)  # pow là hàm lũy thừa 
print(exp)

floor_div = num_one // num_two ## phep chia lay phàn nguyen
print(floor_div)

#hinh tron


radian = float(input("nhap  gia tri ban kinh cua hinh tron: "))

chuvi = 2*radian*3.14    # circumference = chu vi
print(chuvi) 
dientich = 3.14 * pow(radian, 2)
print(dientich)

## using built_in to get infor

firstname = str(input("hay nhap ten cua ban: "))
help('keywords')
