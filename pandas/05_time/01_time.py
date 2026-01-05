import pandas as pd

# 사계절 데이터를 용이하게 다루기 위한 시간 자료형
# Timestamp(그 시점) 와 Period(기간)

df = pd.read_csv('./data/stock-data.csv')

print(df)
print()
df.info()
print()

# 문자열 데이터 'Data' 컬럼을 Timestamp로 변환
df['new_Date'] = pd.to_datetime(df['Date'])

print(df)
print()
df.info()
print()
print(type(df['new_Date'][0]))


# new_Data 를 인덱스로 설정
df = df.set_index('new_Date')

# Date 컬럼은 드랍
df = df.drop('Date', axis=1)

print(df)
print()

# =========================================================

# DatetimeIndex
# 사계절 데이터의 인덱스로 쓰이기 위해 설계된 자료 구조

print("\n======== pd.DatetimeIndex ========\n")

print(pd.DatetimeIndex(["2022-12-25", "2024/02/09", "1999.5.5"]))
print(type(pd.DatetimeIndex(["2022-12-25", "2024/02/09", "1999.5.5"])))
print(pd.DatetimeIndex(["2022-12-25", "2024/02/09", "1999.5.5"]).dtype)


# Timestamp
#

print("\n======== pd.DatetimeIndex ========\n")

print(pd.Timestamp("04-30-2021")) # 2021-04-30 00:00:00
print(pd.Timestamp("30-05-2021")) # 2021-05-30 00:00:00
print(pd.Timestamp("06-04-2021")) # 2021-06-04 00:00:00
print(type(pd.Timestamp("06-04-2021"))) # Timestamp



print("\n======== pd.to_datetime ========\n")

print(pd.to_datetime("2023년 12월 28일", format="%Y년 %m월 %d일"))
print(pd.to_datetime("12-12 2025 23:59:12", format="%d-%m %Y %H:%M:%S"))                  
print(pd.to_datetime("2023ㅋㅋ 12ㅎㅎ 25??", format="%Yㅋㅋ %mㅎㅎ %d??"))



print("\n======== Timestamp를 Period로 변환 ========\n")

dates = ['2019-01-01', '2020-03-01', '2021-06-01']

ts_dates = pd.to_datetime(dates)
print(ts_dates)
print()

pr_day = ts_dates.to_period(freq='D')
print(pr_day)
print()

pr_month = ts_dates.to_period(freq='M')
print(pr_month)
print()

pr_year = ts_dates.to_period(freq='Y')
print(pr_year)
print()



