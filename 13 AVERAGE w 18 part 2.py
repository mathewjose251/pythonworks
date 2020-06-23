def average(num):
        sum_num = 0
        for t in num:
                sum_num = sum_num + t
        avg = sum_num / len(num)
        return avg
       
print("The average is", average([10,20,90,200]))
