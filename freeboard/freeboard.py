import matplotlib.pyplot as plt
import numpy as np
from hidrostatik import TPC,DW,CB
import requests
from bs4 import BeautifulSoup
import pandas as pd
"""
url = 'https://www.imorules.com/GUID-0393B3AF-4E8E-4A7F-B821-C94A99AC29F4.html'
response = requests.get(url)
cont = response.content
soup = BeautifulSoup(cont, 'html.parser')
table = soup.find('table', {"class": "tableborder"})
rows = table.find_all('tr', class_='row')

###    Freeboard Table for Type 'A' Ships   ###
length_of_ship_list = []
freeboard_list = []
for row in rows:
    columns = row.find_all('td')
    if 'Freeboard(milli-metres)' not in columns[0].text.strip() and 'Length' not in columns[0].text.strip():
        length_of_ship = columns[0].text.strip()
        freeboard = columns[1].text.strip()
        length_of_ship_list.append(length_of_ship)
        freeboard_list.append(freeboard)
    if 'Freeboard(milli-metres)' not in columns[3].text.strip() and 'Length' not in columns[3].text.strip():
        length_of_ship = columns[3].text.strip()
        freeboard = columns[4].text.strip()
        length_of_ship_list.append(length_of_ship)
        freeboard_list.append(freeboard)
    if 'Freeboard(milli-metres)' not in columns[6].text.strip() and 'Length' not in columns[6].text.strip():
        length_of_ship = columns[6].text.strip()
        freeboard = columns[7].text.strip()
        length_of_ship_list.append(length_of_ship)
        freeboard_list.append(freeboard)

length_of_ship_listA=[]
freeboard_listA=[]
for i in length_of_ship_list:
    newi=int(i)
    length_of_ship_listA.append(newi)
    length_of_ship_listA.sort()
for i in freeboard_list:
    newi=int(i)
    freeboard_listA.append(newi)
    freeboard_listA.sort()

###    Freeboard Table for Type 'B' Ships   ###

table_id=soup.find("table",{"id":"LL_1966_REG28_TABB__LL_1966_REG28_TABB_METRIC"})

rows1 = table_id.find_all('tr', class_='row')
###    Freeboard Table for Type 'A' Ships   ###
freeboard_list1 = []
for row in rows1:
    columns = row.find_all('td')
    if 'Freeboard(milli-metres)' not in columns[0].text.strip():
        freeboard = columns[1].text.strip()
        freeboard_list1.append(freeboard)
    if 'Freeboard(milli-metres)' not in columns[3].text.strip():
        freeboard = columns[4].text.strip()
        freeboard_list1.append(freeboard)
    if 'Freeboard(milli-metres)' not in columns[6].text.strip():
        freeboard = columns[7].text.strip()
        freeboard_list1.append(freeboard)

freeboard_listB=[]
for i in freeboard_list1:
    try:
        newi=int(i)
        if newi == 7385: # TABLODA HATALI İKİ DEĞER VARDI
            newi = 4385
        elif newi == 7397:
            newi = 4397
        freeboard_listB.append(newi)
        freeboard_listB.sort()
    except:
        pass"""

"""       ############################################ MANUEL EKLE YA DA EKLEME HOCAYA DANIŞ     ##############################################
Length_of_Ship= [24, 49, 76, 103, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365]
FreeboardA= [432, 786, 1181, 200, 208, 217, 225, 233, 242, 250, 258, 267, 275, 283, 292, 300, 308, 316, 325, 334, 344, 354, 364, 374, 385, 396, 408, 420, 443, 455, 467, 478, 490, 503, 516, 530, 544, 559, 573, 587, 600, 613, 626, 639, 653, 666, 680, 693, 706, 720, 733, 746, 760, 773, 800, 814, 828, 841, 855, 869, 883, 897, 911, 926, 940, 955, 969, 984, 999, 1014, 1029, 1044, 1059, 1074, 1089, 1105, 1120, 1135, 1151, 1166, 1196, 1212, 1228, 1244, 1260, 1276, 1293, 1309, 1326, 1342, 1359, 1376, 1392, 1409, 1426, 1442, 1459, 1476, 1494, 1511, 1528, 1546, 1563, 1580, 1598, 1615, 1632, 1650, 1667, 1684, 1702, 1719, 1736, 1753, 1770, 1787, 1803, 1820, 1837, 1853, 1870, 1886, 1903, 1919, 1935, 1952, 1968, 1984, 2000, 2016, 2032, 2048, 2064, 2080, 2096, 2111, 2126, 2141, 2155, 2169, 2184, 2198, 2212, 2226, 2240, 2254, 2268, 2281, 2294, 2307, 2320, 2332, 2345, 2357, 2369, 2381, 2393, 2405, 2416, 2428, 2440, 2451, 2463, 2474, 2486, 2497, 2508, 2519, 2530, 2541, 2552, 2562, 2572, 2582, 2592, 2602, 2612, 2622, 2632, 2641, 2650, 2659, 2669, 2678, 2687, 2696, 2705, 2714, 2723, 2732, 2741, 2749, 2758, 2767, 2775, 2784, 2792, 2801, 2809, 2817, 2825, 2833, 2841, 2849, 2857, 2865, 2872, 2880, 2888, 2895, 2903, 2910, 2918, 2925, 2932, 2939, 2946, 2953, 2959, 2966, 2973, 2979, 2986, 2993, 3000, 3006, 3012, 3018, 3024, 3030, 3036, 3042, 3048, 3054, 3060, 3066, 3072, 3078, 3084, 3089, 3095, 3101, 3106, 3112, 3117, 3123, 3128, 3133, 3138, 3143, 3148, 3153, 3158, 3163, 3167, 3172, 3176, 3181, 3185, 3189, 3194, 3198, 3202, 3207, 3211, 3215, 3220, 3224, 3228, 3233, 3237, 3241, 3246, 3250, 3254, 3258, 3262, 3266, 3270, 3274, 3278, 3281, 3285, 3288, 3292, 3295, 3298, 3302, 3305, 3308, 3312, 3315, 3318, 3322, 3325, 3328, 3331, 3334, 3337, 3339, 3342, 3345, 3347, 3350, 3353, 3355, 3358, 3361, 3363, 3366, 3368, 3371, 3373, 3375, 3378, 3380, 3382, 3385, 3387, 3389, 3392, 3394, 3396, 3399, 3401, 3403, 3406, 3408, 3410, 3412, 3414, 3416, 3418, 3420, 3422, 3423, 3425, 3427, 3428, 3430, 3432, 3433]
FreeboardB= [200, 208, 217, 225, 233, 242, 250, 258, 267, 275, 283, 292, 300, 308, 316, 325, 334, 344, 354, 364, 374, 385, 396, 408, 420, 432, 443, 455, 467, 478, 490, 503, 516, 530, 544, 559, 573, 587, 601, 615, 629, 644, 659, 674, 689, 705, 721, 738, 754, 769, 784, 800, 816, 833, 850, 868, 887, 905, 923, 942, 960, 978, 996, 1015, 1034, 1054, 1075, 1096, 1116, 1135, 1154, 1172, 1190, 1209, 1229, 1250, 1271, 1293, 1315, 1337, 1359, 1380, 1401, 1421, 1440, 1459, 1479, 1500, 1521, 1543, 1565, 1587, 1609, 1630, 1651, 1671, 1690, 1709, 1729, 1750, 1771, 1793, 1815, 1837, 1859, 1880, 1901, 1921, 1940, 1959, 1979, 2000, 2021, 2043, 2065, 2087, 2109, 2130, 2151, 2171, 2190, 2209, 2229, 2250, 2271, 2293, 2315, 2334, 2354, 2375, 2396, 2418, 2440, 2460, 2480, 2500, 2520, 2540, 2560, 2580, 2600, 2620, 2640, 2660, 2680, 2698, 2716, 2735, 2754, 2774, 2795, 2815, 2835, 2855, 2875, 2895, 2915, 2933, 2952, 2970, 2988, 3007, 3025, 3044, 3062, 3080, 3098, 3116, 3134, 3151, 3167, 3185, 3202, 3219, 3235, 3249, 3264, 3280, 3296, 3313, 3330, 3347, 3363, 3380, 3397, 3413, 3430, 3445, 3460, 3475, 3490, 3505, 3520, 3537, 3554, 3570, 3586, 3601, 3615, 3630, 3645, 3660, 3675, 3690, 3705, 3720, 3735, 3750, 3765, 3780, 3795, 3808, 3821, 3835, 3849, 3864, 3880, 3893, 3906, 3920, 3934, 3949, 3965, 3978, 3992, 4005, 4018, 4032, 4045, 4058, 4072, 4085, 4098, 4112, 4125, 4139, 4152, 4165, 4177, 4189, 4201, 4214, 4227, 4240, 4252, 4264, 4276, 4289, 4302, 4315, 4327, 4339, 4350, 4362, 4373, 4385, 4397, 4408, 4420, 4432, 4443, 4455, 4467, 4478, 4490, 4502, 4513, 4525, 4537, 4548, 4560, 4572, 4583, 4595, 4607, 4618, 4630, 4642, 4654, 4665, 4676, 4686, 4695, 4704, 4714, 4725, 4736, 4748, 4757, 4768, 4779, 4790, 4801, 4812, 4823, 4834, 4844, 4855, 4866, 4878, 4890, 4899, 4909, 4920, 4931, 4943, 4955, 4965, 4975, 4985, 4995, 5005, 5015, 5025, 5035, 5045, 5055, 5065, 5075, 5086, 5097, 5108, 5119, 5130, 5140, 5150, 5160, 5170, 5180, 5190, 5200, 5210, 5220, 5230, 5240, 5250, 5260, 5268, 5276, 5285, 5294, 5303]

"""

###################################################################################################
url = 'https://www.imorules.com/GUID-8758D434-AA3E-4C76-A0FB-28EB991FF0FE.html'
response = requests.get(url)
cont = response.content
soup = BeautifulSoup(cont, 'html.parser')

tableA = soup.find("table", {"id": "LL_REG28-_1__LL_TAB28.1"})
tableB= soup.find("table", {"id": "LL_REG28-_2__LL_TAB28.2"})

rowsA = tableA.find_all('tr', class_='row')
rowsB=tableB.find_all("tr",{"class":"row"})
length_of_the_ship = []
freeboardlistA = []
freeboardlistB=[]

for row in rowsA:
    cells = row.find_all('td')

    if len(cells) >= 1 and "nocellnorowborder" in cells[0]["class"]:
        length=(cells[0].get_text(strip=True))
        length_of_the_ship.append(int(length))

        if 49 not in length_of_the_ship:
            length_of_the_ship.append(49)
            freeboardlistA.append(432)
        if 76 not in length_of_the_ship:
            length_of_the_ship.append(76)
            freeboardlistA.append(786)
        if 103 not in length_of_the_ship:
            length_of_the_ship.append(103)
            freeboardlistA.append(1181)

    if len(cells) >= 2 and "cell-norowborder" in cells[1]["class"]:
        FA=(cells[1].get_text(strip=True))
        freeboardlistA.append(int(FA))

length_of_the_shipB=[]
for row in rowsB:
    cells = row.find_all('td')
    if len(cells) >= 2 and "cell-norowborder" in cells[1]["class"]:
        FA = (cells[1].get_text(strip=True))
        freeboardlistB.append(int(FA))
freeboardlistB.append(5303) # bunu tablodan eklemedi


#TABLODAKİ SAYILARIN KONTROLÜ EKSİK VAR MI DİYE
for k in range(24,366):
    if k not in length_of_the_ship:
        print("Eksik olan sayılar:", k)
    else:
        pass


df_length = pd.DataFrame({'LENGTH': length_of_the_ship})
df_FA = pd.DataFrame({'FA': freeboardlistA})
df_FB = pd.DataFrame({'FB': freeboardlistB})
FAB_TABLE_df = pd.concat([df_length, df_FA, df_FB], axis=1)


L=int(input("freeboard boyunu gir: "))
vessel_type=int(input("tab 1 or 2 for choosing the vessel type: 1)cargo 2)tanker "))
TE=int(input("üst yapıların toplam boyu: "))


def calculate_F():
    F = FAB_TABLE_df[FAB_TABLE_df['LENGTH'] == L]
    if not F.empty:
        if vessel_type==2:
            FA_value = F['FA'].values[0]
            F=FA_value

        elif vessel_type==1:
            FB_value=F["FB"].values[0]
            F=FB_value
        return F
    else:
        return ("the length shouldnt be larger than 350 m ")


D=7.1
T=4.71
F_S=calculate_F()
print("F_S COR ",F_S)

#### CORRECTİONS #######
# LENGTH CORRECTİON
if vessel_type==1 and TE/L<=0.35 and 24<=L<=100:
    l_cor=7.5*(100-L)*(0.35-TE/L)
    print("l correction",l_cor)
    F_S=F_S+l_cor
print("F_S L COR ",F_S)

# BLOCK COEFFİCİENT CORRECTİON
CB=CB()
if CB>=0.68:
    CB_cor=(CB+0.68)/1.36
    print("CB COR",CB_cor)
    F_S=F_S*CB_cor
print("F_S  CB COR ",F_S)
print("CB ",CB)

# DEPTH  CORRECTİON
if D>=L/15:
    if 24<=L<=120:
        R=L/0.48
    else:
        R=250
    D_cor=(D-L/15)*R
    F_S=F_S+D_cor
    print("D_COR",D_cor)
print("FS WİTH D_COR",F_S)

F_T=F_S-T*1000/48
F_W=F_S+T*1000/48
F_WNA=F_W+50
F_F=F_S-DW(T)/(40*TPC(T))
F_TF=F_F-T/48

print(F_S)
print(F_T)
print(F_TF)
print(F_W)
print(F_WNA)
print(F_F)

# Freeboard mark
center = (0, F_S)
circle1_radius = 150
circle2_radius = 125

theta = np.linspace(0, 2*np.pi, 100)
circle1_x = center[0] + circle1_radius * np.cos(theta)
circle1_y = center[1] + circle1_radius * np.sin(theta)
circle2_x = center[0] + circle2_radius * np.cos(theta)
circle2_y = center[1] + circle2_radius * np.sin(theta)




plt.plot(circle1_x, circle1_y, color='black')
plt.plot(circle2_x, circle2_y, color='black')
plt.fill(np.append(circle1_x, circle2_x[::-1]),
         np.append(circle1_y, circle2_y[::-1]), color='black')

plt.grid(True,linestyle='--', alpha=0.5)



rw = 450
rh = 25
rectangle_x = np.array([-rw/2, rw/2, rw/2, -rw/2, -rw/2])
rectangle_y = np.array([F_S - rh/2, F_S - rh/2, F_S + rh/2, F_S + rh/2, F_S - rh/2])
rectangle = plt.Rectangle((- rw/2, F_S - rh/2), rw, rh, color='black')
plt.gca().add_patch(rectangle)

############## FREEBOARD DECK ##################
rw = 300
rh = 25
rectangle = plt.Rectangle((- rw/2, 2*F_S - rh/2), rw, rh, color='black')
plt.gca().add_patch(rectangle)



############### SUMMER FREEBOARD ###############
rw_S = 230
rh_S= 25
rectangle = plt.Rectangle((540, F_S - rh_S/2), rw_S, rh_S, color='black')
plt.gca().add_patch(rectangle)
plt.text(540+230+5, F_S , 'S', ha='left', va='center', color='black', fontsize=8, fontweight='bold')
############### WINTER FREEBOARD ############### #
rectangle = plt.Rectangle((540, (F_S - rh_S/2)-110), rw_S, rh_S, color='black')
plt.gca().add_patch(rectangle)
plt.text(540+232, F_S-110, 'W', ha='left', va='center', color='black', fontsize=8, fontweight='bold')

############### NORTH ATLANTIC WINTER FREEBOARD ###############
rectangle = plt.Rectangle((540, (F_S - rh_S/2)-3/2*110), rw_S, rh_S, color='black')
plt.gca().add_patch(rectangle)
plt.text(540+232, (F_S)-3/2*110, 'WNA', ha='left', va='center', color='black', fontsize=8, fontweight='bold')

############### TROPICAL SALT WATER FREEBOARD ###############
rectangle = plt.Rectangle((540, (F_S - rh_S/2)+110), rw_S, rh_S, color='black')
plt.gca().add_patch(rectangle)
plt.text(540+232, (F_S +110), 'T', ha='left', va='center', color='black', fontsize=8, fontweight='bold')


############### FRESH WATER FREEBOARD ###############
rectangle = plt.Rectangle(((540-230), (F_S - rh_S/2)+4/3*110), rw_S, rh_S, color='black')
plt.gca().add_patch(rectangle)
plt.text(540-230,(F_S+rh_S/2)+4/3*110, 'F', ha='left', va='bottom', color='black', fontsize=8, fontweight='bold')

############### TROPICAL FRESH WATER FREEBOARD ###############
rectangle = plt.Rectangle(((540-230), (F_S - rh_S/2)+(1+4/3)*110), rw_S, rh_S, color='black')
plt.gca().add_patch(rectangle)
plt.text(540-230,(F_S+rh_S/2+(1+4/3)*110), 'TF', ha='left', va='bottom', color='black', fontsize=8, fontweight='bold')


############ VERTİCAL LINE ################

rectangle = plt.Rectangle((540, (F_S - rh_S/2)-3/2*110), 25,(25+(1+4/3)*110+3/2*110), color='black')
plt.gca().add_patch(rectangle)


plt.gca().set_aspect('equal', adjustable='box')
plt.show()
