import psycopg

def get_connection():
    connection = psycopg.connect(
        host = "localhost",
        dbname = "invoice_management",
        user = "postgres",
        password = "CG-vak123",
        port = 5432
    )

    return connection
