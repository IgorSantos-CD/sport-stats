from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.config import settings

# Monta a URL de forma segura
if settings.database_url:
    DATABASE_URL = settings.database_url
else:
    if not all([settings.db_user, settings.db_pass, settings.db_host, settings.db_port, settings.db_name]):
        raise ValueError("Banco de dados não configurado corretamente nas variáveis de ambiente")
    
    DATABASE_URL = (
        f"postgresql://{settings.db_user}:{settings.db_pass}"
        f"@{settings.db_host}:{settings.db_port}/{settings.db_name}"
    )

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)