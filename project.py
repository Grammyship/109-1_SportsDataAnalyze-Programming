import matplotlib.pyplot as plt
import numpy as np
hit = []

# team data
braves = []
dodges = []
indians = []

# MLB data
'''
hits = []  #i[4]
homerun = []
RBI = []
score = []  # i[7]
SO = []
AVG = []
OBP = []
SP = []  # i[11]
'''

with open('batting.txt', encoding='utf8') as f:
    for line in f:
        hit.append(line.split())
 
for i in hit:
    if i[1] == "亞特蘭大勇士":
        braves = i
        #print(braves)
    elif i[1] == "洛杉磯道奇":
        dodges = i
        #print(dodges)
    elif i[1] == "克里夫蘭印地安人":
        indians = i
        #print(indian)

count = 0
temp = 0

Braves = [0, 0, 0, 0, 0, 0, 0, 0]
Dodges = [0, 0, 0, 0, 0, 0, 0, 0]
Indians = [0, 0, 0, 0, 0, 0, 0, 0]
np_braves = np.array(Braves)
np_dodges = np.array(Dodges)
np_indians = np.array(Indians)

for i in hit:
    if count != 0:
        temp = 0
        braves_ = 0
        dodges_ = 0
        indians_ = 0
        for j in i:
            if temp >= 4:
                if float(j) >= float(braves[temp]):
                    np_braves[temp-4] += 1
                if float(j) >= float(dodges[temp]):
                    np_dodges[temp-4] += 1
                if float(j) >= float(indians[temp]):
                    np_indians[temp-4] += 1
            temp += 1
    count += 1

# sincd i[8] = 被三振的打擊數, we have to use 30 - i[8] to calulate the real ranking
np_braves[4] = 31 - np_braves[4]
np_dodges[4] = 31 - np_dodges[4]
np_indians[4] = 31 - np_indians[4]
'''
print(np_braves)
print(np_dodges)
print(np_indians)
'''
# ranking
avg_d = 0
avg_b = 0
avg_i = 0

for i in range(0,8):
    avg_d += np_dodges[i]
    avg_b += np_braves[i]
    avg_i += np_indians[i]

# divide 8 to calculate the average ranking
avg_d /= 8
avg_b /= 8
avg_i /= 8

print("================================================")
print("冠軍道奇隊的打擊平均排名為：", round(avg_d,1) )
print("亞特蘭大勇士隊的打擊平均排名為：" , round(avg_b,1) )
print("克里夫蘭印地安人的打擊平均排名為：" , round(avg_i,1) )
print("================================================")

# team data
_braves = []
_dodges = []
_indians = []

pitch = []
with open('pitching.txt', encoding='utf8') as f:
    for line in f:
        pitch.append(line.split())


for i in pitch :
    if i[1] == "克里夫蘭印地安人":
        _indians = i
        #print(braves)
    elif i[1] == "洛杉磯道奇":
        _dodges = i
        #print(dodges)
    elif i[1] == "亞特蘭大勇士":
        _braves = i
        #print(indian)

count = 0
temp = 0


# MLB data
'''
wins = []  #i[3]
save = []  #i[5]
full_pitch = []
shutout = []  # i[7]
scored = []
escort = []
SO = []
ERA = []  # i[11]
'''
_Braves = [0, 0, 0, 0, 0, 0]
_Dodges = [0, 0, 0, 0, 0, 0]
_Indians = [0, 0, 0, 0, 0, 0]
_np_braves = np.array(_Braves)
_np_dodges = np.array(_Dodges)
_np_indians = np.array(_Indians)

for i in pitch:
    if count != 0:
        temp = 0
        braves_ = 0
        dodges_ = 0
        indians_ = 0
        for j in i:
            if temp == 3:
                if float(j) >= float(_braves[temp]):
                    _np_braves[temp-3] += 1
                if float(j) >= float(_dodges[temp]):
                    _np_dodges[temp-3] += 1
                if float(j) >= float(_indians[temp]):
                    _np_indians[temp-3] += 1
            elif temp == 5:
                if float(j) >= float(_braves[temp]):
                    _np_braves[temp-4] += 1
                if float(j) >= float(_dodges[temp]):
                    _np_dodges[temp-4] += 1
                if float(j) >= float(_indians[temp]):
                    _np_indians[temp-4] += 1
            elif temp >= 8:
                if float(j) >= float(_braves[temp]):
                    _np_braves[temp-6] += 1
                if float(j) >= float(_dodges[temp]):
                    _np_dodges[temp-6] += 1
                if float(j) >= float(_indians[temp]):
                    _np_indians[temp-6] += 1
            temp += 1
    count += 1

# sincd i[2] = 自責分, i[3] = 保送數, i[5] = 防禦率, we have to use 30 - i[8] to calulate the real ranking
_np_braves[2] = 31 - _np_braves[2]
_np_dodges[2] = 31 - _np_dodges[2]
_np_indians[2] = 31 - _np_indians[2]
_np_braves[3] = 31 - _np_braves[3]
_np_dodges[3] = 31 - _np_dodges[3]
_np_indians[3] = 31 - _np_indians[3]
_np_braves[5] = 31 - _np_braves[5]
_np_dodges[5] = 31 - _np_dodges[5]
_np_indians[5] = 31 - _np_indians[5]
'''
print(_np_braves)
print(_np_dodges)
print(_np_indians)
'''
# ranking
_avg_b = 0
_avg_d = 0
_avg_i = 0

for i in range(0, 6):
    _avg_d += _np_dodges[i]
    _avg_b += _np_braves[i]
    _avg_i += _np_indians[i]

_avg_b /= 6
_avg_d /= 6
_avg_i /= 6

print(' ')
print("================================================")
print("冠軍道奇隊的投手平均排名為：", round(_avg_d, 1))
print("亞特蘭大勇士隊的投手平均排名為：", round(_avg_b, 1))
print("克里夫蘭印地安人的投手平均排名為：", round(_avg_i, 1))
print("================================================")
print(' ')
print("================================================")
print("冠軍道奇隊的總平均排名為：", round( (avg_d*8 + _avg_d*6)/14 , 1))
print("亞特蘭大勇士隊的總平均排名為：", round((avg_b*8 + _avg_b*6)/14, 1))
print("克里夫蘭印地安人的總平均排名為：", round((avg_i*8 + _avg_i*6)/14, 1))
print("================================================")


brave_win = 0
indian_win = 0
