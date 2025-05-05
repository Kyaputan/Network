import psycopg2

DB_HOST="localhost"
DB_USER="root"
DB_PASSWORD="310146"
DB_NAME="root"

try:
    conn = psycopg2.connect(database=DB_NAME,
                            host=DB_HOST,
                            user=DB_USER,
                            password=DB_PASSWORD)
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"✅ Connected to PostgreSQL! Version: {db_version[0]}")
    cursor.close()
    conn.close()
except psycopg2.Error as err:
    print(f"❌ Connection failed: {err}")