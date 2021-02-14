import config
import csv
import psycopg2
import psycopg2.extras

connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)

cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute("""
    CREATE TABLE mention (
        stock_id INTEGER,
        dt TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        message TEXT NOT NULL,
        source TEXT NOT NULL,
        url TEXT NOT NULL,
        PRIMARY KEY (stock_id, dt),
        CONSTRAINT fk_mention_stock FOREIGN KEY (stock_id) REFERENCES stock (id)
    );
""")

cursor.execute("""
    CREATE INDEX ON mention (stock_id, dt DESC);
""")

cursor.execute("""
    SELECT create_hypertable('mention', 'dt');
""")

connection.commit()