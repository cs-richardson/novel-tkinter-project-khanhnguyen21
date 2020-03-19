CREATE TABLE "Author" (
	"AuthorID"	INTEGER NOT NULL,
	"AuthorName"	VARCHAR(50) NOT NULL,
	"DOB"	DATE,
	PRIMARY KEY("AuthorID")
);

CREATE TABLE "Book" (
	"ISBN"	INTEGER NOT NULL,
	"Title"	VARCHAR(50) NOT NULL,
	"Price"	INTEGER NOT NULL,
	"Genre"	VARCHAR(50) NOT NULL,
	PRIMARY KEY("ISBN")
);

CREATE TABLE "Customer" (
	"CustomerID"	INTEGER NOT NULL,
	"CustomerName"	VARCHAR(50) NOT NULL,
	"DOB"	DATE,
	PRIMARY KEY("CustomerID")
);

CREATE TABLE "Wrote" (
	"AuthorID"	INTEGER NOT NULL,
	"ISBN"	INTEGER NOT NULL,
	FOREIGN KEY("ISBN") REFERENCES "Book"("ISBN"),
	PRIMARY KEY("AuthorID","ISBN"),
	FOREIGN KEY("AuthorID") REFERENCES "Author"("AuthorID")
);

CREATE TABLE "Bought" (
	"CustomerID"	INTEGER NOT NULL,
	"ISBN"	INTEGER NOT NULL,
	FOREIGN KEY("ISBN") REFERENCES "Book"("ISBN"),
	FOREIGN KEY("CustomerID") REFERENCES "Customer"("CustomerID"),
	PRIMARY KEY("CustomerID","ISBN")
);

INSERT INTO "Author" ("AuthorID","AuthorName","DOB") VALUES (1,'Karl Popper','7/28/1902'),
 (2,'Haruki Murakami','1/12/1949');
 
INSERT INTO "Book" ("ISBN","Title","Price","Genre") VALUES (9781400079278,'Kafka on the Shore',10,'Fiction'),
 (9783161484100,'The Logic of Scientific Discovery',10,'Philosophy');
 
INSERT INTO "Customer" ("CustomerID","CustomerName","DOB") VALUES (1,'John Doe','1/1/2000'),
 (2,'Jane Doe','1/1/2000');
 
INSERT INTO "Wrote" ("AuthorID","ISBN") VALUES (1,9783161484100),
 (2,9781400079278);
 
INSERT INTO "Bought" ("CustomerID","ISBN") VALUES (1,9783161484100),
 (2,9781400079278),
 (2,9783161484100);