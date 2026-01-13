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

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]

df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul = df_seoul.rename({'전입지별':'전입지'}, axis=1)
df_seoul = df_seoul.set_index('전입지')

sr_one = df_seoul.loc['경기도']

df_4 = df_seoul.loc[['충청남도','경상북도','강원도','전라남도'], '2010':'2017']
df_4 = df_4.T

# ===============================================================

# 스타일 지정
plt.style.use('Solarize_Light2')

# 막대 그래프 그리기
df_4.plot(kind='bar', figsize=(16, 8), width=0.5,
          color=['orange', 'green', 'skyblue', 'deeppink']
          )
plt.title('서울 -> 타도시', pad=10, size=30, color='brown', fontweight='bold')
plt.ylabel('이동 인구수', labelpad=10, size=20)
plt.xlabel('기간', labelpad=10, size=20)

# plt.ylim(5000,30000)
plt.legend(title='전입지', fontsize=15)

plt.xticks(rotation=45)
plt.tick_params(
    axis='both',
    direction='out', # in, out, inout
    length=10,
    width=1,
    labelsize=10
)

plt.show()

'''
plt.xticks()
눈금 위치, 표시될 문자 지정 
ex) 
plt.xticks([0, 1, 2], ['A', 'B', 'C'], 로테이션)

plt.tick_params()
눈금 디자인(길이, 방향, 색, 두께 등)
ex)
plt.tick_params(
    axis='both',
    direction='out',
    length=6,
    width=1,
    labelsize=10
)
'''
# =========================== 가로형 막대그래프 ===========================

df_4 = df_seoul.loc[['충청남도','경상북도','강원도','전라남도'], '2010':'2017']

df_4['합계'] = df_4.sum(axis=1)
print(df_4['합계'])

df_total = df_4[['합계']].sort_values(by='합계', ascending=True)

print(df_total)

df_total.plot(kind='barh', figsize=(10,5))
plt.title('서울 -> 타시도 인구이동')
plt.ylabel('전입지')
plt.xlabel('이동 인구 수')
plt.show()


fig, axes = plt.subplots(1, 2, figsize=(10, 5))
# ax.stackplot(df_4.index, df_4.T, alpha=0.2, labels=df_4.columns)
axes[0].barh(df_total.index, df_total['합계'])
axes[0].set_title('시도별 전입인구')

df_total.plot(kind='bar', ax=axes[1], rot=0)                      
axes[1].set_title('시도별 인구증가')
# 이름만 변경
axes[1].set_xticklabels(['충청', '경상', '강원', '전라'], rotation=45)

plt.tight_layout()
plt.show()
