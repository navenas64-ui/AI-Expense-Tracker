import sqlite3

conn = sqlite3.connect("expense.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    category TEXT,
    amount REAL,
    date TEXT,
    note TEXT
)
""")

conn.commit()
conn.close()

print("Expense Database Created Successfully!")


def add_expense(expense_type, category, amount, date, note):
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses(type, category, amount, date, note)
        VALUES (?, ?, ?, ?, ?)
    """, (expense_type, category, amount, str(date), note))

    conn.commit()
    conn.close()

def view_expenses():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()

    conn.close()
    return data

def total_expense():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses WHERE type='Expense'")
    expense = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(amount) FROM expenses WHERE type='Income'")
    income = cursor.fetchone()[0]

    conn.close()

    if expense is None:
        expense = 0

    if income is None:
        income = 0

    return income, expense

def Dashboard():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses WHERE type='Income'")
    income = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(amount) FROM expenses WHERE type='Expense'")
    expense = cursor.fetchone()[0]

    conn.close()

    if income is None:
        income = 0
    if expense is None:
        expense = 0

    return income, expense
