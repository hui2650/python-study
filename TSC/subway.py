from pathlib import Path
import pandas as pd

# =========================
# 0) 출력 옵션 (터미널 가독성)
# =========================
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 150)
pd.set_option('display.max_colwidth', 30)

def banner(title, width=90):
    print("\n" + "█" * width)
    print(f"  {title}")
    print("█" * width)

def show(df, cols=None, n=10, sort=None, asc=False):
    out = df.copy()
    if sort:
        out = out.sort_values(sort, ascending=asc)
    if cols:
        out = out[cols]
    print(out.head(n).to_string(index=False))

# =========================
# 1) 데이터 로드 & 1~9호선 필터링
# =========================
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "subway-data.csv"

df = pd.read_csv(DATA_PATH, encoding="cp949").drop_duplicates()

valid_lines = [f"{i}호선" for i in range(1, 10)]
df_1to9 = df[df["호선명"].isin(valid_lines)].copy()

banner("1단계: 1~9호선 데이터 필터링 (호선별 샘플)")
show(df_1to9.groupby("호선명").head(1), ["호선명", "지하철역"], n=20, sort="호선명")

# =========================
# 2) 시간 컬럼 1시간 → 3시간 단위 압축
# =========================
time_cols = [c for c in df_1to9.columns if "시-" in c]

def make_3h_label(col: str) -> str:
    hour = int(col[:2])
    start = (hour // 3) * 3
    end = start + 3
    return f"{start:02d}~{end:02d} {'승차' if '승차' in col else '하차'}"

df_3h = df_1to9.copy()
group_map = {}
for col in time_cols:
    new_col = make_3h_label(col)
    group_map.setdefault(new_col, []).append(col)

for new_col, cols in group_map.items():
    df_3h[new_col] = df_3h[cols].sum(axis=1)

df_3h.drop(columns=time_cols, inplace=True)

banner("2단계: 3시간 단위 변환 (출근/퇴근 시간대 가시성)")
view_cols = ["호선명", "지하철역", "06~09 승차", "06~09 하차", "18~21 승차", "18~21 하차"]
show(df_3h.groupby("호선명").head(1).sort_values("호선명"), view_cols, n=20)

# =========================
# 공통 준비: 유동인구(승+하) 컬럼 생성
# =========================
time_slots = ["00~03", "03~06", "06~09", "09~12", "12~15", "15~18", "18~21", "21~24"]
for slot in time_slots:
    df_3h[f"{slot} 유동인구"] = df_3h[f"{slot} 승차"] + df_3h[f"{slot} 하차"]

floating_cols = [f"{slot} 유동인구" for slot in time_slots]

# =========================
# 3) 역별 하루 총 승하차 -> "어디에 사람이 몰리는가"
# =========================
usage_cols = [c for c in df_3h.columns if ("~" in c and ("승차" in c or "하차" in c))]
df_3h["하루 총 승하차"] = df_3h[usage_cols].sum(axis=1)

station_total = (
    df_3h.groupby(["호선명", "지하철역"], as_index=False)["하루 총 승하차"]
         .sum()
         .sort_values("하루 총 승하차", ascending=False)
)

banner("3단계: 하루 기준 승하차 TOP 10 (역별)")
show(station_total, ["호선명", "지하철역", "하루 총 승하차"], n=10)

# =========================
# 4) 시간대별 유동인구 TOP 역 -> "왜 이 시간대에 이 역이 붐비나"
# =========================
banner("4단계: 시간대별 유동인구 TOP 역 (하루 기준)")

for slot in time_slots:
    col = f"{slot} 유동인구"
    top = (
        df_3h.groupby(["호선명", "지하철역"], as_index=False)[col]
              .sum()
              .sort_values(col, ascending=False)
              .head(5)
    )
    print(f"\n▶ {slot} TOP 5")
    print(top[["호선명", "지하철역", col]].to_string(index=False))

# =========================
# 5) 각 호선별 대표 역(사례) -> "설명용 샘플"
# =========================
top_by_line = (
    station_total.loc[station_total.groupby("호선명")["하루 총 승하차"].idxmax()]
    .sort_values("호선명")
)

banner("5단계: 각 호선별 가장 많이 몰린 역 (하루 기준)")
show(top_by_line, ["호선명", "지하철역", "하루 총 승하차"], n=20)


# =========================
# 6) 시간대가 기준:
#    "피크 시간대가 00~03인 역만", "피크가 06~09인 역만" … 이런 식으로 필터링
# =========================
station_peak = (
    df_3h.groupby(["호선명", "지하철역"], as_index=False)[floating_cols]
         .sum()
)

station_peak["피크 시간대"] = station_peak[floating_cols].idxmax(axis=1).str.replace(" 유동인구", "")
station_peak["피크 유동인구"] = station_peak[floating_cols].max(axis=1)

banner("6단계: 시간대별 '피크가 해당 시간대인 역' 필터링 (TOP 10씩)")
for slot in time_slots:
    pick = (
        station_peak[station_peak["피크 시간대"] == slot]
        .sort_values("피크 유동인구", ascending=False)
    )
    print(f"\n▶ 피크 시간대 = {slot} 인 역 TOP 10")
    if len(pick) == 0:
        print("(해당 없음)")
    else:
        print(pick[["호선명","지하철역","피크 유동인구"]].head(10).to_string(index=False))


# =========================
# 7) 출근/퇴근 승·하차 비율 테이블
#    - 저표본 컷은 내부 적용, 출력은 전체 비율 중심
# =========================

station_commute = (
    df_3h.groupby(["호선명", "지하철역"], as_index=False)
         .agg(
            출근_승차=("06~09 승차", "sum"),
            출근_하차=("06~09 하차", "sum"),
            퇴근_승차=("18~21 승차", "sum"),
            퇴근_하차=("18~21 하차", "sum"),
         )
)

# 내부 신뢰도 컷 (출력 컬럼에는 노출 안 함)
station_commute["출근_합"] = station_commute["출근_승차"] + station_commute["출근_하차"]
cutoff = station_commute["출근_합"].quantile(0.20)
station_commute = station_commute[station_commute["출근_합"] >= cutoff].copy()

# 비율 계산
eps = 1e-9

station_commute["출근 승차비율"] = (
    station_commute["출근_승차"] / (station_commute["출근_합"] + eps)
).round(2)

station_commute["출근 하차비율"] = (
    station_commute["출근_하차"] / (station_commute["출근_합"] + eps)
).round(2)

station_commute["퇴근_합"] = station_commute["퇴근_승차"] + station_commute["퇴근_하차"]

station_commute["퇴근 승차비율"] = (
    station_commute["퇴근_승차"] / (station_commute["퇴근_합"] + eps)
).round(2)

station_commute["퇴근 하차비율"] = (
    station_commute["퇴근_하차"] / (station_commute["퇴근_합"] + eps)
).round(2)

banner("7단계: 출근·퇴근 승·하차 비율 테이블")
show(
    station_commute,
    cols=[
        "호선명", "지하철역",
        "출근 승차비율", "출근 하차비율",
        "퇴근 승차비율", "퇴근 하차비율",
    ],
    n=20,          
    sort=None    
)
# =========================
# 8) 최종 요약:
#    6단계 표(비율 중심) + 역 성격 컬럼만 추가 (컬럼 최소화)
# =========================
# 1.5배 기준을 '비율'로 변환하면 대략 0.6(=1.5/2.5) 임계값
HI = 0.60   # 우세 판단 기준(비율)
BAL = 0.10  # 균형 판단 기준(0.5±0.10)

def classify_zone_ratio(row):
    am_on  = row["출근 승차비율"]
    am_off = row["출근 하차비율"]
    pm_on  = row["퇴근 승차비율"]
    pm_off = row["퇴근 하차비율"]

    # 베드타운: 아침 승차 우세 + 저녁 하차 우세(귀가)
    if (am_on >= HI) and (pm_off >= HI):
        return "베드타운 성향"

    # 업무지구: 아침 하차 우세(유입) + 저녁 승차 우세(이탈)
    if (am_off >= HI) and (pm_on >= HI):
        return "업무지구 성향"

    # 복합: 출근/퇴근 둘 다 0.5 근처면 균형
    if (abs(am_on - 0.5) <= BAL) and (abs(pm_on - 0.5) <= BAL):
        return "복합지역 성향"

    return "일반지역 성향"

final_ratio = station_commute[[
    "호선명","지하철역",
    "출근 승차비율","출근 하차비율",
    "퇴근 승차비율","퇴근 하차비율"
]].copy()

final_ratio["역 성격(요약)"] = final_ratio.apply(classify_zone_ratio, axis=1)

banner("8단계: 출근·퇴근 승하차 비율 기반 역 성격 요약 (하루 기준)")

# ✅ 전체 분포 확인
print(final_ratio["역 성격(요약)"].value_counts())

# ✅ 성격별 예시 출력
print(final_ratio.groupby("역 성격(요약)").head(10).to_string(index=False))



