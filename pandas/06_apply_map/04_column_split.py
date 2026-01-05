import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)

# 주가데이터 로드

df = pd.read_excel('./data/주가데이터.xlsx')

df.info()

# 연, 월, 일 데이터 분리
df['연월일'] = df['연월일'].astype(str)
dates = df['연월일'].str.split('-')

print(dates.head())
                                    
df['연'] = dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)
print(df['연'])
print(df['월'])
print(df['일'])


print('\n ======== expand 옵션 ========\n')

df_expend = df['연월일'].str.split('-', expand=True)
print(df_expend.head(3))


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
print('\n ======== 타임 스탬프 방법 ========\n')

df['연월일'] = pd.to_datetime(df['연월일'])
df.info()
print()

df['연'] = df['연월일'].dt.year
df['월'] = df['연월일'].dt.month
df['일'] = df['연월일'].dt.day
df['요일'] = df['연월일'].dt.day_name(locale="ko_KR")

print(df['연'])
print(df['월'])
print(df['일'])
print(df['요일'])

