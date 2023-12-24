#  輸入顧客購買金額，若金額在
# 100000元打8折.
# 50000打85折.
# 30000打9折.
# 10000打95折.
# 

import pyinputplus as pyip

Price = pyip.inputInt('輸入顧客購買金額',min=0)
Rate = 1
if Price >=100000:
    Rate = 0.8 
elif Price >= 50000:
    Rate = 0.85
elif Price>= 30000:
    Rate = 0.9
elif Price>= 10000:
    Rate = 0.95
Discount = Price * Rate   
    
print(f'打折後應付金額{Discount:.1f}')