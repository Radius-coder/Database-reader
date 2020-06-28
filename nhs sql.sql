CREATE TABLE `customer` (
  `CustomerID` int(10) NOT NULL,
  `CustomerFName` varchar(30) NOT NULL,
  `CustomerLName` varchar(30) NOT NULL,
  `CustomerEmail` varchar(50) NOT NULL,
  `CustomerCard` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `customer`
  ADD PRIMARY KEY (`CustomerID`);
