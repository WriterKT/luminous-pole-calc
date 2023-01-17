# メインのポールの長さ配列
main_pole = [16,32,47,54.5,67.5,72,90.5]
# 延長ポールの長さ配列
extended_pole = [16,31,46,61.5,89.5]
# 96に近似の組み合わせ
ret = [0,0]
# 最小値
min_num = 0
# 基準値
STANDARD_VALUE = 96

for main_pole_val in main_pole :
    for extended_pole_val in extended_pole :
        # メインと延長の合計
        sum = main_pole_val + extended_pole_val
        # 96以下で96に近いものを選ぶ
        if sum <= STANDARD_VALUE :
            tmp_num = STANDARD_VALUE - sum
            if min_num == 0 :
                 min_num = tmp_num
            if tmp_num <= min_num :
                min_num = tmp_num
                ret[0] = main_pole_val
                ret[1] = extended_pole_val

# 結果
for val in ret :
    print(val)
