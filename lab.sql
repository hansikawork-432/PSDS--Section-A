
IF OBJECT_ID('Loan', 'U') IS NOT NULL DROP TABLE Loan;
IF OBJECT_ID('Book', 'U') IS NOT NULL DROP TABLE Book;
IF OBJECT_ID('Member', 'U') IS NOT NULL DROP TABLE Member;
IF OBJECT_ID('Author', 'U') IS NOT NULL DROP TABLE Author;

CREATE TABLE Author (
    author_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE Member (
    member_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    join_date DATE NOT NULL
);

CREATE TABLE Book (
    book_id INT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author_id INT,
    published_year INT,
    FOREIGN KEY (author_id) REFERENCES Author(author_id)
);

CREATE TABLE Loan (
    loan_id INT PRIMARY KEY,
    book_id INT,
    member_id INT,
    loan_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

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
