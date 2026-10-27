import sqlite3
from config import DATABASE_PATH, read_statements

create_table, insert_wallets, read_balances, debit, credit = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_table)
cursor.execute(insert_wallets)
connection.commit()


def balances():
    cursor.execute(read_balances)
    return cursor.fetchall()


def transfer(sender, receiver, amount):
    """Move money as ONE transaction: both steps happen, or neither."""
    try:
        cursor.execute(debit, {"sender": sender, "amount": amount})
        if cursor.rowcount == 0:
            raise ValueError(f"sender {sender} not found")
        cursor.execute(credit, {"receiver": receiver, "amount": amount})
        if cursor.rowcount == 0:
            raise ValueError(f"receiver {receiver} not found")
        connection.commit()
        return "COMMITTED"
    except (sqlite3.Error, ValueError) as error:
        connection.rollback()
        return f"ROLLED BACK ({error})"


print("Balances at the start      :", balances())

print("\nTransfer 1: Asha sends 200 to Ravi")
print("Result                     :", transfer("Asha", "Ravi", 200))
print("Balances                   :", balances())

print("\nInside a transaction, before deciding")
cursor.execute(debit, {"sender": "Asha", "amount": 100})
print("After the debit, not saved :", balances())
connection.rollback()
print("After rollback             :", balances())

print("\nTransfer 2: Asha sends 100 to Nobody (the debit works, then the credit fails)")
print("Result                     :", transfer("Asha", "Nobody", 100))
print("Balances (debit undone)    :", balances())

print("\nTransfer 3: Ravi sends 5000 to Asha (more than he has)")
print("Result                     :", transfer("Ravi", "Asha", 5000))
print("Balances                   :", balances())

connection.close()