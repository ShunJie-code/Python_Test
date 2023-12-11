height, weight = eval(input("\
请输入身高(m)和体重(kg), 用逗号隔开： "))
bmi = weight / pow(height, 2)
print("BMI 数值为：{:.2f}".format(bmi))
# 国际标准
if bmi < 18.5:
    who = "偏瘦"
elif bmi < 25:
    who = "正常"
elif bmi < 30:
    who = "偏胖"
else:
    who = "肥胖"
# 国内标准
if bmi < 18.5:
    dom = "偏瘦"
elif bmi < 24:
    dom = "正常"
elif bmi < 28:
    dom = "偏胖"
else:
    dom = "肥胖"
print("BMI指标为：国际 :{0}, 国内 :{1}".
      format(who, dom))
