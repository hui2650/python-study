import pandas as pd
# df = 파일로드
df = pd.read_csv('./data/train.csv')

# 전체출력
print(df)

# 인포 출력
df.info()

# "Survived", "Pclass", "Sex", "Age", "Fare", "Embarked" 만 남기기
new_df = df[["Survived", "Pclass", "Sex", "Age", "Fare", "Embarked"]]

# 결측치확인
print('=' * 100)
print("결축치 확인")
print('=' * 100)
print(new_df.isnull().sum())

# Age 결측치 평균으로 채우기
new_df['Age'] = new_df['Age'].fillna(round(new_df['Age'].mean()))

print('=' * 100)
print("Age 결측치 평균으로 채우기")
print('=' * 100)
print(new_df['Age'].head(20))

# Embarked 결측치 최빈값으로 채우기
new_df['Embarked'] = new_df['Embarked'].fillna(new_df['Embarked'].mode()[0])

print('=' * 100)
print("Embarked 결측치 최빈값으로 채우기")
print('=' * 100)
print(new_df['Embarked'].head(20))

# 성별을 숫자로 변환 (map 사용) {"male": 0, "female": 1}
changeAgeNum = {"male": 0, "female": 1}
new_df['Sex'] = new_df['Sex'].map(changeAgeNum)

print(new_df.head(10))

print('=' * 100)
print("전처리 후")
print('=' * 100)
print(new_df.describe)
print()
new_df.info()

print('=' * 100)
print("함수로 구현")
print('=' * 100)

# 컬럼 선별 함수
def select_columns(df):
    return df[["Survived", "Pclass", "Sex", "Age", "Fare", "Embarked"]]

# age 채우기 함수
def fill_age_mean(df):
    df = df.copy()
    age_mean = df['Age'].mean()
    df['Age'] = df['Age'].fillna(age_mean)
    return df

#embark 채우기 함수
def fill_embarked_mode(df):
    df = df.copy()
    embarked_mode = df['Embarked'].mode()[0]
    df['Embarked'] = df['Embarked'].fillna(embarked_mode)
    return df

# 성별 맵핑 함수 
def encode_sex(df):
    df = df.copy()
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    return df

df_clean1 = encode_sex(fill_embarked_mode(fill_age_mean(select_columns(df))))
print(df_clean1)

print('=' * 100)
print("pipe() 함수 사용")
print('=' * 100)

df_clean2 = (
    df
    .pipe(select_columns)
    .pipe(fill_age_mean)
    .pipe(fill_embarked_mode)
    .pipe(encode_sex)
)

print(df_clean2)


print('=' * 100)
print("pipe() 함수 추가작업")
print('=' * 100)

def null_check(df, msg):
    print(f"\n ======== [{msg}] ========\n")
    print(df.head(3))
    print("\n결축치 갯수\n")
    print(df.isnull().sum())
    return df

df_clean3 = (
        df
.pipe(select_columns)
.pipe(null_check, "컬럼 선택 후")
.pipe(fill_age_mean)
.pipe(null_check, "Age 결측 처리 후 후")
.pipe(fill_embarked_mode)
.pipe(null_check,"Embarked 결측 처리 후")
.pipe(encode_sex)
.pipe(null_check,"성별 맵핑 후")
)

print(df_clean3)