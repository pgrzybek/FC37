nums =[23,56,90,0,100,12]
result=[num**2 for num in nums ]
#result=[]

# for i  in range(len(nums)):
#     #result.append(nums[i]**2)
#     result.append(pow(nums[i],2))
#print(result)

MONTHS = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}
result.clear()
monthNames= list(MONTHS.values())
for month in monthNames:
   #lower= str.lower(month)
   lower=month.lower()
   montlen=len(month)

   result.append((month,lower,montlen))
#print(result)
listmonths=list(MONTHS.items())
print(listmonths)
number10= listmonths[-3][0]
april=listmonths[4][1]
print(number10)
print(april)