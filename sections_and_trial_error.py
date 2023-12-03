import pandas as pd
from scipy.interpolate import interp1d
def section_selection(W):
    data = [
        [1, 0, 0, 0, 0],
        [2, 0, 0, 0, 0],
        [3, 0, 0, 0, 0],
        [4, 0, 0, 0, 0],
        [5, 0, 0, 0, '50x5'],
        [6, 0, 0, 0, '50x6'],
        [7, 0, 0, 0, '50x7'],
        [8, 0, 0, 0, 0],
        [9, 0, 0, 0, '65x6'],
        [10, 0, 0, 0, '60x8'],
        [11, '45x45x5', 0, '60x4', '65x7'],
        [12, 0, 0, '60x5', '75x6'],
        [13, 0, 0, 0, '65x8'],
        [14, 0, 0, '60x6', '75x7'],
        [15, 0, 0, 0, '80x7'],
        [16, '45x45x7', '60x40x5', 0, '75x8'],
        [17, '50x50x6', 0, 0, 0],
        [18, 0, 0, 0, 0],
        [19, 0, '60x40x6', 0, '75x9'],
        [20, '50x50x7', 0, '80x5', 0],
        [21, '55x55x6', '65x50x5', 0, '75x10'],
        [22, 0, '60x40x7', 0, 0],
        [23, 0, 0, '80x6', '90x8'],
        [24, 0, 0, 0, 0],
        [25, '60x60x6 or 50x50x9', '75x50x5', '80x7', 0],
        [26, 0, 0, 0, '90x9'],
        [27, 0, '75x55x5', 0, '100x8'],
        [28, '55x55x8', 0, 0, 0],
        [29, 0, '80x40x6 or 65x50x7', 0, '90x10'],
        [30, 0, 0, 0, 0],
        [31, 0, 0, 0, '100 x 9'],
        [32, 0, 0, 0, '110 x 8'],
        [33, '60 x 60 x 8', 0, 0, '90 x 11'],
        [34, '55 x 55 x 10 or 65 x 65 x 7', 0, '100 x 6', 0],
        [35, 0, '75 x 50 x 7', 0, '100x10'],
        [36, 0, '65x50x9', 0, '90x12'],
        [37, 0, '75x55x7 or 80x40x8', 0, '110x9'],
        [38, 0, 0, '100x7', '120x8'],
        [39, 0, '80x65x6', 0, '100x11'],
        [40, '70x70x7', 0, 0, 0],
        [41, '60x60x10', 0, 0, 0],
        [42, 0, 0, '100x8', '110x10'],
        [43, 0, '90x60x6', 0, 0],
        [44, '65x65x9', '75x50x9', 0, '120x9'],
        [45, 0, '100x50x6', 0, 0],
        [46, '75x75x7', 0, 0, 0],
        [47, 0, '75x55x9', 0, '110x11'],
        [48, 0, 0, 0, 0],
        [49, 0, 0, '120x6', '120x10'],
        [50, 0, 0, 0, 0],
        [51, '70x70x9', 0, 0, 0],
        [52, 0, '80x65x8', 0, '110x12'],
        [53, '75x75x8 or 65x65x11', 0, 0, 0],
        [54, 0, 0, '120x7', 0],
        [55, 0, 0, 0, '120x11'],
        [56, 0, 0, 0, 0],
        [57, 0, '90x60x8', 0, '130x10'],
        [58, 0, 0, 0, '150x8'],
        [59, 0, '90x75x7 or 100x50x8', 0, 0],
        [60, '80x80x8', 0, '120x8', 0],
        [61, '70x70x11', '100x65x7', 0, '120x12'],
        [62, 0, 0, 0, 0],
        [63, 0, 0, 0, 0],
        [64, 0, '80x65x10', 0, '140x10'],
        [65, '75x75x10', 0, 0, 0],
        [66, 0, '100x75x7', '140x6', 0],
        [68, 0, 0, 0, '120x13'],
        [70, 0, 0, 0, 0],
        [72, 0, 0, 0, '140x11'],
        [74, '80x80x10', '100x50x10', '140x7', '150x10'],
        [76, '75x75x12', 0, 0, '120x14'],
        [78, 0, '100x65x9', 0, 0],
        [80, 0, 0, 0, '140x12'],
        [82, 0, 0, '140x8', 0],
        [84, '90x90x9', 0, 0, '160x10'],
        [86, 0, 0, 0, 0],
        [88, '80x80x12', '100x75x9', 0, '140x13'],
        [90, 0, 0, 0, 0],
        [92, 0, 0, '140x9', '150x12'],
        [94, 0, 0, 0, 0],
        [96, 0, '100x65x11', 0, '140x14'],
        [98, 0, 0, 0, 0],
        [100, '80 x 80 x 14x or 90 x 90 x 11', '130 x 65 x 8', 0, 0],
        [105, 0, '100x75x11 or 120x80x8', '160x7', '160x12 or 180x10'],
        [110, 0, '135x75x8', '160x8', 0],
        [115, '100 x 100 x 10', 0, 0, '160x13'],
        [120, '90 x 90 x 13', 0, '160x9', '140x16'],
        [125, 0, '130x65x10', 0, '160x14'],
        [130, 0, '120x80x10', 0, '180x12'],
        [135, '100 x 100 x 12', '130x75x10', 0, '160x15'],
        [140, '110 x 110 x 10', 0, 0, '180x13'],
        [145, '90 x 90 x 16', 0, '180x8', '160x16'],
        [150, 0, '130x65x12 or 150x75x9', 0, 0],
        [155, 0, '120x80x12 or 130x90x10', 0, '180x14'],
        [160, '100 x 100 x 14', 0, '180x9', '160x17'],
        [165, '110 x 110 x 12', '130x75x12', 0, '180x15'],
        [170, 0, 0, 0, '160x18'],
        [175, 0, '120x80x14', '180x10', 0],
        [180, 0, '130x90x12 or 150x75x11', 0, '180x16'],
        [185, '120 x 120 x 11', 0, 0, '200x14'],
        [190, 0, '160x80x10 or 150x90x10', '180x11', '180x17'],
        [195, '110 x 110 x 14', 0, 0, 0],
        [200, 0, '150x100x10', 0, '200x15'],
        [210, '120 x 120 x 13', 0, '200x9', '180x18'],
        [220, '100 x 100 x 20', 0, '200x10', '200x16 or 220x14'],
        [230, '130 x 130 x 12', '150 x 90 x 12  or 160 x 80 x 12', 0, '200x17'],
        [240, 0, '150 x 100 x 12', 0, '220x15'],
        [250, '120 x 120 x 15', '180 x90 x 10', '200x11,5', '200x18'],
        [260, 0, '160 x80 x 14', 0, '220 x 16 or 240 x 14'],
        [270, '130 x 130 x 14', 0, 0, '200 x 19'],
        [280, 0, '150 x100 x 14', '220 x10', '220 x 17 or 240 x 15 or 200 x 20'],
        [290, 0, '180 x90 x 12', 0, 0],
        [300, '140 x 140 x 13', '200 x100 x 10', 0, '220 x 18'],
        [310, '130 x 130 x 16', 0, '220 x11,5', '240 x 16 or 260 x 14'],
        [320, '120 x 120 x 20', 0, 0, '220 x 19'],
        [330, 0, '180 x90 x 14', 0, '240 x 17 or 260 x 15 or 220 x 20'],
        [340, '140 x 140 x 15', 0, '240 x10', 0],
        [350, 0, 0, 0, '240 x 18 or 260 x 16'],
        [360, 0, '200 x100 x 12', 0, 0],
        [370, '150 x 150 x 14', 0, '240 x11', '240 x 19'],
        [380, '140 x 140 x 17', '250 x90 x 10', 0, '260 x 17'],
        [390, 0, 0, '240 x12', '240 x 20'],
        [400, 0, 0, 0, '260 x 18'],
        [410, '150 x 150 x 16', '200 x100 x 14', 0, '280 x 16'],
        [420, 0, 0, '260 x10', 0],
        [430, 0, 0, 0, '280 x 17 or 260 x 19'],
        [440, 0, 0, 0, 0],
        [450, '160 x 160 x 15', 0, '260 x11', 0],
        [460, 0, '250 x90 x 12', 0, '280 x 18 or 260 x 20'],
        [470, '150 x 150 x 18', '200 x100 x 16', '260 x12', 0],
        [480, 0, 0, 0, 0],
        [490, 0, 0, 0, '300 x 17 or 280 x 19'],
        [500, '160 x 160 x 17', 0, '260 x13', 0],
        [510, 0, 0, 0, 0],
        [520, 0, 0, 0, '280 x 20 or 300 x 18'],
        [530, 0, '250 x 90 x 14', '280 x11', 0],
        [540, 0, 0, 0, 0],
        [550, '160 x 160 x 19', 0, 0, '280 x21'],
        [560, 0, 0, 0, '300 x 19'],
        [570, 0, 0, '280 x12', 0],
        [580, 0, 0, 0, '280 x22'],
        [590, 0, 0, 0, '300 x20 or  320 x18'],
        [600, '180 x 180 x 16', '250 x 90 x 16', '280 x13', 0],
        [620, 0, 0, 0, 0],
        [640, 0, 0, '280x14 or  300x11', '300 x21 or  320 x19'],
        [660, '180 x 180 x 18', 0, 0, '300 x22'],
        [680, '200 x 200 x 18', 0, '300x12', '320 x20'],
        [700, 0, 0, '300x13', '300 x23'],
        [720, 0, 0, 0, '320 x21 or  340 x19'],
        [740, '180 x 180 x 20', 0, '300x14', '320 x22 or  300 x24'],
        [760, '200 x 200 x 16', 0, 0, '340 x20'],
        [780, 0, 0, '300x15 or  320x12', '320 x23'],
        [800, 0, 0, 0, '340 x21'],
        [820, 0, 0, '320x13', '320 x24'],
        [840, 0, 0, 0, '340 x22 or  360 x20'],
        [860, 0, 0, '320x14', 0],
        [880, 0, 0, 0, '320 x25 or  340 x23'],
        [900, 0, 0, '320x15 or  340x12', 0],
        [920, '200 x 200 x 20', 0, '340 x24 or  320 x26', 0],
        [940, 0, 0, '320 x 16', '360 x 22'],
        [960, 0, 0, '340 x 13', '340 x 25'],
        [980, 0, 0, 0, 0],
        [1000, 0, 0, '340 x 14', 0],
        [1020, 0, 0, 0, '340 x 26 or  360 x 24'],
        [1040, 0, 0, '340 x 15', '380 x 22'],
        [1060, 0, 0, 0, '340 x 27'],
        [1080, 0, 0, '340 x 16', 0],
        [1100, 0, 0, 0, '340 x 28'],
        [1120, 0, 0, 0, '360 x 26'],
        [1140, 0, 0, 0, '380 x 24'],
        [1160, 0, 0, 0, 0],
        [1180, 0, 0, '370 x 13', 0],
        [1200, 0, 0, 0, 0],
        [1220, 0, 0, '370 x 14', '360 x 28'],
        [1240, 0, 0, 0, '380 x 26'],
        [1260, 0, 0, 0, '400 x 24'],
        [1280, 0, 0, '370 x 15', 0],
        [1300, 0, 0, 0, 0],
        [1320, 0, 0, '370 x 16', '360 x 30'],
        [1340, 0, 0, 0, 0],
        [1360, 0, 0, 0, '380 x 28 or 400x26'],
        [1380, 0, 0, '370 x 17', '420x28'],
        [1400, 0, 0, 0, 0],
        [1450, 0, 0, '370 x 18', 0],
        [1500, 0, 0, '400x14', '380 x 30 or 400x28'],
        [1550, 0, 0, '400x15', '420 x26'],
        [1600, 0, 0, '400x16', '400 x 30'],
        [1650, 0, 0, '400x17', '420 x 28 or  440 x 26\n 440 x 26'],
        [1700, 0, 0, 0, 0],
        [1750, 0, 0, '400x18', '420 x 30'],
        [1800, 0, 0, '400x19', '440 x 28'],
        [1850, 0, 0, '430x15', 0],
        [1900, 0, 0, 0, '420 x 32'],
        [1950, 0, 0, '430x16', '440 x 30 or  440 x 30'],
        [2000, 0, 0, '430 x 17', 0],
        [2050, 0, 0, 0, 0],
        [2100, 0, 0, '430 x 18', '440 x 32 or  460 x 30'],
        [2150, 0, 0, '430 x 19', 0],
        [2200, 0, 0, 0, 0],
        [2250, 0, 0, '430 x 20', 0],
        [2300, 0, 0, 0, '460 x 32'],
        [2350, 0, 0, '430 x 21', 0],
        [2400, 0, 0, 0, 0],
        [2450, 0, 0, 0, 0]
    ]

    columns = ['Section Modulus', 'Angle Section with equal legs', 'Angle Section with not equal legs ', 'Bulb Flat Section',
               'Flat Bar Section']

    WR_Selection = pd.DataFrame(data, columns=columns)
    selected_row = None
    for index, row in WR_Selection.iterrows():
        if W <= row['Section Modulus']:
            selected_row = row
            break

    if selected_row is not None:
        for col, value in selected_row.items():
            if value!=0:
                print(f"{col}: {value}")
    else:
        print("Section not found for the given W value. you need to use trial error method for a suitable section")


W_value = 122
section_selection(W_value)

from scipy.interpolate import interp1d

from scipy.interpolate import interp1d


def Trial_Error(W, t):
    F = 40 * t * t
    fs_coefficient = 30 # as a first approximation

    while True:
        fs = fs_coefficient * t * t
        fs_F = fs / F

        wlist = [0.98, 1, 1.04, 1.08, 1.1, 1.13, 1.18, 1.2, 1.24, 1.27, 1.3, 1.35, 1.39, 1.42, 1.47, 1.5]
        fs_F_list = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3]

        calculate_w = interp1d(fs_F_list, wlist)
        w = calculate_w(fs_F)
        Wn = w * F * fs / t

        if Wn < W:
            fs_coefficient += 1
        else:
            fs_coefficient -= 1

        if Wn > W and Wn - W <= 50:
            print(f"Section modulus by trial error: {round(Wn)} and you need a section with at least {fs_coefficient} mm height" )
            break


W_value=963
t_value = 1.1
Trial_Error(W_value, t_value)
