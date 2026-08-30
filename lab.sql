import sqlite3
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.executescript('''
DROP TABLE IF EXISTS Loan;
DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Author;
''')

cursor.executescript('''
CREATE TABLE Author (
    author_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE Member (
    member_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    join_date TEXT NOT NULL
);

CREATE TABLE Book (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author_id INTEGER,
    published_year INTEGER,
    FOREIGN KEY (author_id) REFERENCES Author(author_id)
);

CREATE TABLE Loan (
    loan_id INTEGER PRIMARY KEY,
    book_id INTEGER,
    member_id INTEGER,
    loan_date TEXT NOT NULL,
    return_date TEXT,
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (member_id) REFERENCES Member(member_id)
);
''')

cursor.executescript('''
INSERT INTO Author (author_id, name) VALUES 
(1, 'J.K. Rowling'),
(2, 'George Orwell');

INSERT INTO Member (member_id, name, join_date) VALUES 
(101, 'HANSIKA', '2024-01-15'),
(102, 'AKANSHA', '2024-02-01');

INSERT INTO Book (book_id, title, author_id, published_year) VALUES 
(201, '1984', 2, 1949),
(202, 'Harry Potter', 1, 1997);

INSERT INTO Loan (loan_id, book_id, member_id, loan_date, return_date) VALUES 
(301, 201, 101, '2024-03-01', NULL),
(302, 202, 102, '2024-03-05', '2024-03-12');
''')
conn.commit()

def run_query(title, query):
    print(f"=== {title} ===")
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print()

run_query("Query 1: SELECT * FROM Author", "SELECT * FROM Author;")

run_query("Query 2: SELECT * FROM Member", "SELECT * FROM Member;")

run_query(
    "Query 3: Books with Authors",
    """
    SELECT b.book_id, b.title, a.name AS author_name, b.published_year 
    FROM Book b
    JOIN Author a ON b.author_id = a.author_id;
    """
)

run_query(
    "Query 4: Active Loans (Not Returned)",
    """
    SELECT 
        l.loan_id,
        m.name AS member_name,
        b.title AS book_title,
        l.loan_date
    FROM Loan l
    JOIN Book b ON l.book_id = b.book_id
    JOIN Member m ON l.member_id = m.member_id
    WHERE l.return_date IS NULL;
    """
)

run_query(
    "Query 5: Complete Loan Details",
    """
    SELECT 
        l.loan_id,
        m.name AS member_name,
        b.title AS book_title,
        a.name AS author_name,
        l.loan_date,
        l.return_date
    FROM Loan l
    JOIN Book b ON l.book_id = b.book_id
    JOIN Author a ON b.author_id = a.author_id
    JOIN Member m ON l.member_id = m.member_id;
    """
)

conn.close()
