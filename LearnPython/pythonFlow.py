# coding=utf-8
# python 中的if elif else

score=-1
if score<=100:
    if score>=0:
        if score==100:
            print ("满分")
        elif score >= 90:
            print ("很优秀")
        elif score >= 80:
            print ("优秀")
        elif  score>=70:
            print ("良好")
        elif score>=60:
            print ("及格")
        elif score<60:
            print ("不及格")
    else:
        print ("分数有问题")
else:
    print ("分数有问题")