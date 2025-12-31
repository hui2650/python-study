import pandas as pd

df = pd.read_csv('./data/stock-data.csv')

# Data 컬럼을 변환하여 새로운 데이트타임 컬럼 new_Date 을 만들기
# 헤드, 인포 출력

df['new_Date'] = pd.to_datetime(df['Date'])
print(df.head())
print()
df.info()

df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
df['Quarter'] = df['new_Date'].dt.quarter
df['DayName'] = df['new_Date'].dt.day_name(locale='ja_JP')
# 'ja_JP', 'fr_FR', 'es_ES
df['M_days'] = df['new_Date'].dt.days_in_month


print(df.head())


# Timestamp를 Period로 변환하여 년원일 표기 변경하기
df['Date_yr'] = df['new_Date'].dt.to_period(freq='Y')
df['Date_m'] = df['new_Date'].dt.to_period(freq='M')
print(df.head())

# 2018년 6월 데이터만 추출 (문자열 속성 활용)
df_june = df[df['Date_m'].astype(str).str.fullmatch('2018-06')] 
print(df_june.head())
print()


df_june = df[df['Date_m'] ==  '2018-06'] 
print(df_june.head())
print()

df_june2 = df[df['Date_m'] == pd.Period('2018-06')]
print(df_june2.head())

# df_june2 에서 Data_m 을 인덱스로 지정

