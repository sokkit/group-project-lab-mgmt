DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Items;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS OrderItems;

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
  `customerID`	INTEGER NOT NULL
);

INSERT INTO 'Orders'('userID', 'customerID') VALUES (2, 3);
INSERT INTO 'Orders'('userID', 'customerID') VALUES (2, 4);

CREATE TABLE IF NOT EXISTS `OrderItems` (
  `orderItemsID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `itemID`	INTEGER NOT NULL,
  `orderID`	INTEGER NOT NULL
);

INSERT INTO 'OrderItems'('itemID', 'orderID') VALUES (2, 1);
INSERT INTO 'OrderItems'('itemID', 'orderID') VALUES (4, 1);
INSERT INTO 'OrderItems'('itemID', 'orderID') VALUES (6, 1);
INSERT INTO 'OrderItems'('itemID', 'orderID') VALUES (2, 2);
INSERT INTO 'OrderItems'('itemID', 'orderID') VALUES (8, 2);