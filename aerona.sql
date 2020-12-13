DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Items;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS OrderItems;
DROP TABLE IF EXISTS CompletedPDFs;

CREATE TABLE IF NOT EXISTS `Users` (
  `userID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `firstName`	TEXT NOT NULL,
  `surname`	TEXT NOT NULL,
  `public`  TEXT NOT NULL,
  `username`  TEXT NOT NULL,
  `password`  TEXT,
  `role`  TEXT NOT NULL
);

INSERT INTO 'Users'('firstName','surname', 'public', 'username','role' ) VALUES ('Joe','Bloggs','True', 'Joe01', 'Admin');
INSERT INTO 'Users'('firstName','surname', 'public', 'username','role' ) VALUES ('Tom','Brown','True', 'Tom01', 'Staff');
INSERT INTO 'Users'('firstName','surname', 'public', 'username', 'password', 'role' ) VALUES ('Admin','User','True', 'Admin01', "b'$2b$12$5nU0TVBvc2ZD2mLE6PztrO8vcrKWWkch.VCxZ8drz9TOgZpGThcPG'", 'Admin');
INSERT INTO 'Users'('firstName','surname', 'public', 'username', 'password', 'role' ) VALUES ('Admin','User','True', 'Admin', "b'$2b$12$5nU0TVBvc2ZD2mLE6PztrOcdB.SwZnfS5Ff7PK3rQYK.gjJtu967K'", 'Admin');
INSERT INTO 'Users'('firstName','surname', 'public', 'username', 'password', 'role' ) VALUES ('Staff','User','True', 'Staff', "b'$2b$12$5nU0TVBvc2ZD2mLE6PztrOcdB.SwZnfS5Ff7PK3rQYK.gjJtu967K'", 'Staff');

CREATE TABLE IF NOT EXISTS `Customers` (
  `customerID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `customerName`	TEXT NOT NULL,
  `address`	TEXT NOT NULL,
  `deliveryAddress`  TEXT NOT NULL
);

INSERT INTO 'Customers'('customerName','address', 'deliveryAddress') VALUES ('Delta Med','2nd Floor, Dubai, UAE, 1900','2nd Floor, Dubai, UAE, 1900');
INSERT INTO 'Customers'('customerName','address', 'deliveryAddress') VALUES ('Moscow Pharma','Ulitsa Moskva, Moscow, Russia, 12800','Ulitsa Moskva, Moscow, Russia, 12800');
INSERT INTO 'Customers'('customerName','address', 'deliveryAddress') VALUES ('Abbvie GmBH','Frankfurt Plaza, 1325, Frankfurt, Germany, 8860','Frankfurt Plaza, 1325, Frankfurt, Germany, 8860');
INSERT INTO 'Customers'('customerName','address', 'deliveryAddress') VALUES ('Warsaw Holding co.','12 Warsaw Square, Warsaw, Poland','265 Warsaw Industrial Estate, Warsaw, Poland');
INSERT INTO 'Customers'('customerName','address', 'deliveryAddress') VALUES ('BulgarPharm','1900 Alexander Nevski, Sofia, Bulgaria','1700 Mladost, Sofia, Bulgaria');

CREATE TABLE IF NOT EXISTS `Items` (
  `itemID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `productName`	TEXT NOT NULL,
  `temperature`	TEXT NOT NULL,
  `origin`  TEXT NOT NULL
);

INSERT INTO 'Items'('productName','temperature', 'origin') VALUES ('Carmustine 100mg inj','Cold Chain','UK');
INSERT INTO 'Items'('productName','temperature', 'origin') VALUES ('Melphalan 50mg inj','Ambient','UK');
INSERT INTO 'Items'('productName','temperature', 'origin') VALUES ('Cidofovir 375mg inj','Ambient','UK');
INSERT INTO 'Items'('productName','temperature', 'origin') VALUES ('Labetalol 100mg tablets','Ambient','UK');
INSERT INTO 'Items'('productName','temperature', 'origin') VALUES ('Busulfan 6mg inj','Cold Chain','UK');
INSERT INTO 'Items'('productName','temperature', 'origin') VALUES ('Dapsone 50mg caps','Ambient','UK');
INSERT INTO 'Items'('productName','temperature', 'origin') VALUES ('Meropenem 1g inj','Ambient','UK');
INSERT INTO 'Items'('productName','temperature', 'origin') VALUES ('Keytruda 100mg inj','Cold Chain','DE');
INSERT INTO 'Items'('productName','temperature', 'origin') VALUES ('Prolia 500mg','Cold Chain','China');
INSERT INTO 'Items'('productName','temperature', 'origin') VALUES ('Soliris 100mg','Ambient','Japan');

CREATE TABLE IF NOT EXISTS `Orders` (
  `orderID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `userID`	INTEGER NOT NULL,
  `customerID`	INTEGER NOT NULL,
  `pdfName`	TEXT NOT NULL
);

INSERT INTO 'Orders'('userID', 'customerID', 'pdfName') VALUES (2, 3, "PDF1");
INSERT INTO 'Orders'('userID', 'customerID', 'pdfName') VALUES (2, 4, "PDF2");

CREATE TABLE IF NOT EXISTS `OrderItems` (
  `orderItemsID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `orderID`		INTEGER NOT NULL,
  -- orderID is orderNumber in CompltedPDFs
  `productName`	INTEGER NOT NULL,
  `quantity`	INTEGER NOT NULL,
  `batchNumber`	TEXT NOT NULL,
  `expiryDate`	TEXT NOT NULL,
  `temperature`	TEXT NOT NULL,
  `origin`	TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS `CompletedPDFs` (
  `completedPDFsID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `customerName`	TEXT NOT NULL,
  `orderNumber`	TEXT NOT NULL,
  `consignmentNumber`	TEXT NOT NULL,
  `numOfPallets`	TEXT NOT NULL,
  `totalWeight`	TEXT NOT NULL,
  `contactName`	TEXT NOT NULL,
  `contactNumber`	TEXT NOT NULL
);
