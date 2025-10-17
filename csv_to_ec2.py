import pandas as pd
from sqlalchemy import create_engine

# CSV 파일 불러오기
df = pd.read_csv("Data/musinsa_pick.csv")

# MySQL 연결 설정
user = 'redash_user'
password = 'tmdrbs6755'
host = '13.209.99.209'
port = 3306
database = 'musinsa_db'

# SQLAlchemy 엔진 생성
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

# 테이블로 적재 (기존 테이블에 추가 삽입)
df.to_sql(name='musinsa_pick', con=engine, if_exists='append', index=False)