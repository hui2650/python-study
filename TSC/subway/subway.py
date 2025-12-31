import pandas as pd
import os as os
import numpy as np

df = pd.read_csv('./data/seoul_subway_data.csv', encoding="cp949")

# 목적 : 각 지하철 역 별 일일 총 승하차승객 분석을 목표
# 그리고 데이터 분석을 바탕으로 일일 총 승하차승객이 많은 이유를 추론하기 위함

# 1단계 : 1~9호선만을 기준

# 2단계 : 컬럼을 1시간 단위가 아닌 3시간 단위로 줄이기

# 3단계 : 총승하차승객 컬럼 추가 -> 사용월 / 호선 / 지하철역 /  총승하차승객수 -> 추론 : 가장 많은 인구가 몰리는 지역 확인 ex) 서울

# 4단계 : 각 역마다 가장 유동인구가 많은 시간대 컬럼 -> 사용월 / 호선 / 지하철역 / 시간대 / 유동인구 -> 추론 : 왜 이 시간대에 이 역은 유동인구가 많은가

# 5단계 : 각 호선별 가장 유동인구가 많은 역들을 데이터프레임 객체로 생성

# 6단계 : 출근, 퇴근 시간대 승하차 비율 컬럼 추가 -> 사용월 / 호선 / 지하철역 / 출근 승차인원 / 출근 하차인원 / 퇴근  승차인원 / 퇴근 하차인원 / 출근 승하차비율 / 퇴근 승하차 비율
#  -> 추론 : 각 역의 성격을 파악 가능 ex) 베드 타운 / 상업 도시/ 유흥가

# 7단계 : 6단계 컬럼에서 시간대를 인덱스로 변경 -> 총승하차승객수 -> 추론 : 피크 타임이 언제냐

# 8단계 : 3개의 컬럼을 bin값에 넣고 객체를 생성해서 출력하자! 

# bin에 들어갈 3개의 값 : 승차 > 하차 = 베드타운
#                        하차 > 승차 = 업무지
#                       (|승차 - 하차| <= 전체 승하차 비율 10~ 15%) & (|승차 + 하차| >= 중앙값)

# ================================
# = 1 ~ 9호선만을 기준으로
# ================================


# 1 ~ 9호선만 명시적으로 허용
valid_lines = [f"{i}호선" for i in range(1, 10)]

df = df[df['호선명'].isin(valid_lines)].copy()


print("\n1~9호선만 명시적으로 허용: \n", df)
print()

# ================================
# = 2단계 컬럼을 1시간 단위에서 3시간 단위로 나누기
# ================================
time_groups = {
    '04-07': ['04시-05시', '05시-06시', '06시-07시'],
    '07-10': ['07시-08시', '08시-09시', '09시-10시'],
    '10-13': ['10시-11시', '11시-12시', '12시-13시'],
    '13-16': ['13시-14시', '14시-15시', '15시-16시'],
    '16-19': ['16시-17시', '17시-18시', '18시-19시'],
    '19-22': ['19시-20시', '20시-21시', '21시-22시'],
    '22-01': ['22시-23시', '23시-24시', '00시-01시'],
    '01-04': ['01시-02시', '02시-03시', '03시-04시'],
}

# 원본보호를 위해 df 카피
df_3hours = df.copy()

# 3시간 단위 컬럼 생성
for period, hours in time_groups.items():
    ride_cols = [f'{h} 승차인원' for h in hours]
    alight_cols = [f'{h} 하차인원' for h in hours]

    df_3hours[f'{period}_승차'] = df_3hours[ride_cols].sum(axis=1)
    df_3hours[f'{period}_하차'] = df_3hours[alight_cols].sum(axis=1)

# 원본 1시간 컬럼들 삭제
hourly_cols = [
    col for col in df_3hours.columns
    if '시-' in col and ('승차인원' in col or '하차인원' in col)
]

df_3hours.drop(columns=hourly_cols, inplace=True)


print("\n3시간 단위 컬럼 생성: \n", df_3hours.head(10))
print("\n3시간 단위 컬럼들:  \n", df_3hours.columns)
print()

# ================================
# = 3단계 총승하차승객 컬럼 추가
# ================================


# 정규식으로 1시간 승차/하차 컬럼만 정확히 포함
import re

pattern = re.compile(r'^\d{2}시-\d{2}시 (승차인원|하차인원)$')

traffic_cols = [
    col for col in df.columns
    if ('승차인원' in col) or ('하차인원' in col)
]

df['총승하차승객'] = df[traffic_cols].sum(axis=1)

print(df[['사용월', '호선명', '지하철역', '총승하차승객']].head(10))


# ================================
# = 4단계 각 역마다 가장 유동인구가 많은 시간대 컬럼
# ================================

# time_groups에 정의된 모든 시간대에 대해 해당 시간대의 승차 + 하차 유동인구 컬럼 생성
for slot in time_groups.keys():
    df_3hours[f'{slot}_유동'] = (
        df_3hours[f'{slot}_승차'] + df_3hours[f'{slot}_하차']
    )

# 최대 유동 시간대 계산도 동일하게 적용
flow_cols = [f'{slot}_유동' for slot in time_groups.keys()]

df_3hours['최대유동값'] = df_3hours[flow_cols].max(axis=1)
df_3hours['최대유동시간대'] = (
    df_3hours[flow_cols]
    .idxmax(axis=1)
    .str.replace('_유동', '')
)

print("\n3시간 기준 최대유동값과 시간대 \n", df_3hours[['사용월', '호선명', '지하철역', '최대유동값', '최대유동시간대']].head(10))

# ================================
# = 5단계 각 호선별 가장 유동인구가 많은 역들을 데이터프레임 객체로 생성
# ================================

# 호선명'을 기준으로 데이터를 "호선별 그룹"으로 나눔
# '최대유동값'이 "가장 큰 값"을 가진 행의 인덱스(index)를 반환
idx = df_3hours.groupby('호선명')['최대유동값'].idxmax() 

# 보기 좋게 필요한 컬럼만 남기기
top_station_by_line = df_3hours.loc[idx].reset_index(drop=True)

print("\n각 호선별 가장 유동인구가 많은 역들 \n", top_station_by_line[['호선명', '지하철역', '최대유동시간대', '최대유동값']])

# ================================
#= 6단계 출근, 퇴근 시간대 승하차 비율 컬럼 추가
# ================================

#출근승차비율 
# = 출근_승차 / (출근_승차 + 출근_하차)
# 1에 가까울수록 → 사람들이 집에서 나감 → 주거지(베드타운)
# 0에 가까울수록 → 사람들이 유입됨 → 업무지 / 상업지

# 퇴근하차비율 
# = 퇴근_하차 / (퇴근_승차 + 퇴근_하차)
# 1에 가까울수록 → 사람들이 집으로 돌아옴 → 주거지
# 0에 가까울수록 → 사람들이 나감 → 상업·유흥 중심지

df_3hours['출근_총유동'] = df_3hours['07-10_승차'] + df_3hours['07-10_하차']
df_3hours['퇴근_총유동'] = df_3hours['16-19_승차'] + df_3hours['16-19_하차']

df_3hours['출근승차비율'] = (
    df_3hours['07-10_승차'] / df_3hours['출근_총유동']
)

df_3hours['퇴근하차비율'] = (
    df_3hours['16-19_하차'] / df_3hours['퇴근_총유동']
)

# 혹시 0으로 나누는 행이 있으면
df_3hours[['출근승차비율','퇴근하차비율']] = (
    df_3hours[['출근승차비율','퇴근하차비율']].fillna(0) 
)

print("\n출근, 퇴근 시간대 승하차 비율 컬럼 추가: \n", df_3hours[['사용월', '호선명', '지하철역', '출근승차비율', '퇴근하차비율']].head(10))

#기준값

# 0.6 이상 → 뚜렷한 성향
# 0.4 ~ 0.6 → 혼합 / 완충지대

# 베드타운
# 출근승차비율 ≥ 0.6  AND  퇴근하차비율 ≥ 0.6

# 업무, 상업지
# 출근승차비율 ≤ 0.4  AND  퇴근하차비율 ≤ 0.4

# 유흥, 상업 혼합지 
# 출근승차비율 ≤ 0.4  AND  퇴근하차비율 ≥ 0.6

# 복합지역
# 그 외 전부 

def classify_area(row):
    if row['출근승차비율'] >= 0.6 and row['퇴근하차비율'] >= 0.6:
        return '베드타운'
    elif row['출근승차비율'] <= 0.4 and row['퇴근하차비율'] <= 0.4:
        return '업무/상업지'
    elif row['출근승차비율'] <= 0.4 and row['퇴근하차비율'] >= 0.6:
        return '유흥/상업지'
    else:
        return '복합지역'

# 성격 분류 컬럼 생성
df_3hours['지역성격'] = df_3hours.apply(classify_area, axis=1)

print("\n각 자역의 성격을 파악: \n", df_3hours[['사용월', '호선명', '지하철역', '지역성격',]].head(10))


# ================================
#= 7단계  6단계 컬럼에서 시간대를 인덱스로 변경 -> 추론 : 피크 타임이 언제?
# ================================

# 유동 컬럼들 준비
# flow_cols = [f'{slot}_유동' for slot in time_groups.keys()]

# 역(행)마다 피크 시간대 & 피크 유동값 구하기
df_3hours['피크시간대'] = (
    df_3hours[flow_cols]
    .idxmax(axis=1)                 # 가장 큰 값을 가진 "컬럼명" 반환
    .str.replace('_유동', '')        # 보기 좋게 정리
)

df_3hours['피크유동값'] = df_3hours[flow_cols].max(axis=1)

peak_station = (
     df_3hours
    .sort_values('피크유동값', ascending=False)   # 피크유동값 큰 게 위로
    .drop_duplicates(subset=['호선명', '지하철역'], keep='first')  # 역별로 1개만
    .reset_index(drop=True)
)

print("\n 6단계 컬럼에서 시간대를 인덱스로 변경 -> 역마다 피크 타임이 언제? \n",  peak_station[['사용월', '호선명', '지하철역', '피크시간대', '피크유동값']].head(10))

# ================================
#= 8단계 3개의 컬럼을 bin값에 넣고 객체를 생성해서 출력 ('복합지역', '베드타운', '업무지')
# ================================

import numpy as np

ride_cols = [c for c in df_3hours.columns if c.endswith('_승차')]
alight_cols = [c for c in df_3hours.columns if c.endswith('_하차')]

df_3hours['총승차'] = df_3hours[ride_cols].sum(axis=1)
df_3hours['총하차'] = df_3hours[alight_cols].sum(axis=1)

# 숫자 보정(문자/콤마 대비)
for c in ['총승차', '총하차']:
    df_3hours[c] = pd.to_numeric(df_3hours[c].astype(str).str.replace(',', ''), errors='coerce')

df_3hours['총유동'] = df_3hours['총승차'] + df_3hours['총하차']

ratio = 0.12
median_flow = df_3hours['총유동'].median()
diff = (df_3hours['총승차'] - df_3hours['총하차']).abs()

is_complex = ((diff <= df_3hours['총유동'] * ratio) & (df_3hours['총유동'] >= median_flow)).fillna(False)

df_3hours['지역유형'] = np.select(
    [is_complex,
     df_3hours['총승차'] > df_3hours['총하차'],
     df_3hours['총하차'] > df_3hours['총승차']],
    ['복합지역', '베드타운', '업무지'],
    default='기타'
)

print("\n 3개의 컬럼을 bin값에 넣고 객체를 생성해서 출력 ('복합지역', '베드타운', '업무지') \n",  df_3hours[['사용월', '호선명', '지하철역', '지역유형']].head(10))