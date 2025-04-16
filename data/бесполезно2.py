import sqlite3

# Названия файлов
input_filename = "npv_type.txt"
db_filename = "operations.db"

# Создание и подключение к SQLite
conn = sqlite3.connect(db_filename)
cur = conn.cursor()

# Создание таблиц
cur.execute('''
CREATE TABLE IF NOT EXISTS types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS operations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_id INTEGER,
    operation TEXT NOT NULL,
    FOREIGN KEY (type_id) REFERENCES types (id)
)
''')

conn.commit()

# Чтение и обработка файла
with open(input_filename, 'r', encoding='utf-8') as file:
    block = []
    for line in file:
        line = line.strip()
        if line == "":
            if block:
                # Первая строка блока — это тип, остальные — операции
                type_name = block[0]
                operations = block[1:]

                cur.execute('INSERT INTO types (type) VALUES (?)', (type_name,))
                type_id = cur.lastrowid

                for op in operations:
                    cur.execute('INSERT INTO operations (type_id, operation) VALUES (?, ?)', (type_id, op))
                block = []
        else:
            block.append(line)

    # Обработка последнего блока, если файл не заканчивается пустой строкой
    if block:
        type_name = block[0]
        operations = block[1:]

        cur.execute('INSERT INTO types (type) VALUES (?)', (type_name,))
        type_id = cur.lastrowid

        for op in operations:
            cur.execute('INSERT INTO operations (type_id, operation) VALUES (?, ?)', (type_id, op))

conn.commit()
conn.close()

print("База данных успешно создана!")
