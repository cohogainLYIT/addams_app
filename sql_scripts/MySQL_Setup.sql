create schema addams;

CREATE TABLE addams.`bookingsv2` (
  `reservation_name` varchar(50) DEFAULT NULL,
  `reservation_date` date DEFAULT NULL,
  `guests` int DEFAULT NULL
);