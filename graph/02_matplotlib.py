import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import font_manager, rc

# 한글표기
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 음수표기
plt.rcParams['axes.unicode_minus'] = False

# ===============================================================

df = pd.read_excel('data/시도별_전출입_인구수.xlsx')

df = df.ffill()
print(df)

# 전출지 =  서울, 전입지 = 서울빼고(전국)

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
print("df_seoul: \n", df_seoul)

df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul = df_seoul.rename({'전입지별':'전입지'}, axis=1)
df_seoul = df_seoul.set_index('전입지')

sr_one = df_seoul.loc['경기도']
print(sr_one)

# ===============================================
# plt.plot(sr_one)
# plt.show()

# 기본 그래프
# plt.plot(sr_one.index, sr_one.values, linestyle='dotted')
# plt.title('서울 -> 경기 인구 이동')
# plt.xlabel('기간')
# plt.ylabel('이동 인구수')
# plt.show()

# 기본 그래프2
# plt.figure(figsize=[14, 7])
# plt.plot(sr_one.index, sr_one.values, linestyle='dotted')
# plt.xticks(rotation=90)
# plt.title('서울 -> 경기 인구 이동')
# plt.xlabel('기간')
# plt.ylabel('이동 인구수')
# plt.legend(labels=['서울 -> 경기'])
# plt.show()

# ===============================================
# plt.style.use('dark_background')

# 스타일 / 마커
# plt.figure(figsize=[14, 7])
# plt.plot(sr_one.index, sr_one.values, '-.',
#         marker='*',
#         markerfacecolor='slateblue',
#         markeredgecolor='slateblue',
#         markeredgewidth=2,
#         markersize=10,
#         color='gold',
#         )
# plt.xticks(rotation='vertical', size=10)
# plt.title('서울 -> 경기 인구 이동')
# plt.xlabel('기간', size=20)
# plt.ylabel('이동 인구수', size=20)
# plt.legend(labels=['서울 -> 경기'])
# plt.show()

# bmh ggplot dark_background . . .

# 마커 종류 D d s o p > v < 1 2 3 4 x * + _ .

'''
라인 스타일
dotted ':'
solid '-'
dashed '--'
dashdot '-.'

축약형식 '컬러 라인' 
ex) 
'r--' 빨간 점선
'b-' 빠란 실선 
'''

# ===============================================

plt.figure(figsize=(14, 7))
plt.plot(sr_one.index, sr_one.values, marker='.', markersize=10)
# 한 군데만 컬러 다르게 주기
plt.plot(sr_one.index[5], sr_one.values[5], marker='o', markerfacecolor='red')
plt.xticks(rotation=70, size=10)
plt.title('서울 -> 경기 인구 이동', size=20, pad=20, color='salmon', fontweight='bold')
plt.xlabel('기간', size=20, labelpad=10, color='gold', fontweight='light')
plt.ylabel('이동 인구수', size=20, labelpad=10, color='navy', fontweight='normal')
plt.legend(labels=['서울->경기'], loc='best', fontsize=15) # loc를 ex) upper right, low left 이런식으로 가능 

plt.ylim(50000, 800000)
plt.xlim(-2, 50)

# 주석 표시 (화살표)

# -> / <- / <-> / 

plt.annotate('', 
             xy=(20, 620000), # 화살표 머리
             xytext=(2, 295000), # 화살표 시작
             fontsize=15,
             rotation=32,
             xycoords='data',
             arrowprops=dict(arrowstyle='->', color='skyblue', lw=5),
             )
plt.annotate('인구 이동 증가(1970-1995)', 
             xy=(5, 390000), # 화살표 머리
             fontsize=15,
             rotation=32,
             )

plt.annotate('',
             xy=(45, 430000), # 화살표 머리
             xytext=(30, 580000), # 화살표 시작
             xycoords='data',
             arrowprops=dict(arrowstyle='->', color='pink', lw=5)
             )
plt.annotate('인구 이동 감소(1995-2017)', 
             xy=(32, 480000), # 화살표 머리
             fontsize=15,
             rotation=-18,
             )

plt.show()
