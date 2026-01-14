import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 폰트보다 스타일을 먼저
plt.style.use('grayscale')

from matplotlib import font_manager, rc

# 한글표기
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 음수표기
plt.rcParams['axes.unicode_minus'] = False


# ==============================================

df = pd.read_excel('./data/남북한발전전력량.xlsx')

south = df.iloc[1:5, 2:]
south.index = ['수력', '화력', '원자력', '신재생']
south_T = south.T
print(south_T)

plt.figure(figsize=(12, 6))
sns.lineplot(data=south_T, marker='o', palette='pastel')

plt.title('남한 발전원별 전력 생산량 추이')
plt.xlabel('연도')
plt.ylabel('전력량 (억 kWh)')
plt.xticks(rotation=45)
plt.show()

