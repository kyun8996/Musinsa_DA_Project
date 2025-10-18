import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# ✅ .env 파일 로드
load_dotenv()

# ✅ 환경 변수에서 MySQL 연결정보 불러오기
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
port = os.getenv("MYSQL_PORT", "3306")  # 기본값 3306
database = os.getenv("MYSQL_DATABASE")

# ✅ CSV 파일 불러오기
df = pd.read_csv("Data/musinsa_pick.csv")

# ✅ SQLAlchemy 엔진 생성
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

# ✅ 테이블로 적재 (기존 테이블에 추가 삽입)
df.to_sql(name='musinsa_pick', con=engine, if_exists='append', index=False)

print("✅ Data successfully inserted into musinsa_pick table.")
