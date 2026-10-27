-- Lesson 10 of 20 | Transactions
-- A transaction groups several changes into one unit: either all of them are saved, or none of them.
-- COMMIT saves the changes. ROLLBACK throws them away.
-- Classic example: moving money. The debit and the credit must both happen, or neither.
-- :sender, :receiver and :amount are named parameters that Python fills in.

CREATE TABLE wallets (
    wallet_id INTEGER PRIMARY KEY,
    owner     TEXT NOT NULL,
    balance   REAL NOT NULL CHECK (balance >= 0)
);

INSERT INTO wallets (owner, balance)
VALUES ('Asha', 1000), ('Ravi', 500);

SELECT owner, balance
FROM wallets
ORDER BY wallet_id;

UPDATE wallets
SET balance = balance - :amount
WHERE owner = :sender;

UPDATE wallets
SET balance = balance + :amount
WHERE owner = :receiver;