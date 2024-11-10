from sqlalchemy import create_engine

# Configurações do banco de dados
db_user = "user"
db_password = "user_password"
db_host = "localhost"  # ou o nome do contêiner se estiver usando Docker
db_port = "3306"
db_name = "meu_banco"

# URL de conexão
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Testando a conexão
try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("Conexão bem-sucedida!")
    connection.close()
except Exception as e:
    print(f"Erro ao conectar: {e}")