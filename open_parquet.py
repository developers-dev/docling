import pandas as pd

# Parquet 파일 읽기
df = pd.read_parquet('scratch/multimodal_2025-04-22_235533.parquet')

print(df.columns)
print(df['contents_md'])
# 기본 정보 확인
print(df.info())

# 처음 몇 행 보기
print(df.head())

# 특정 열만 보기 (이미지 바이트 데이터 제외)
print(df.drop(columns=['image.bytes']).head())