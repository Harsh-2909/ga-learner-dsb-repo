# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census = np.concatenate((data, new_record))
# print(census)


# --------------
#Code starts here
age = census[:,0]
max_age = age.max()
min_age = age.min()

age_mean = np.mean(age)
age_std = np.std(age)


# --------------
#Code starts here
race = census[:, 2]
c_0, c_1, c_2, c_3, c_4 = race==0, race==1, race==2, race==3, race==4
race_0, race_1, race_2, race_3, race_4 = census[c_0], census[c_1], census[c_2], census[c_3], census[c_4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minimum = min((len_0, len_1, len_2, len_3, len_4))
if minimum == len_0:
    minority_race = 0
elif minimum == len_1:
    minority_race = 1
elif minimum == len_2:
    minority_race = 2
elif minimum == len_3:
    minority_race = 3
elif minimum == len_4:
    minority_race = 4



# --------------
#Code starts here
senior_citizens = census[census[:,0]>60]
working_hours_sum = senior_citizens[:,6].sum()
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]

avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])




