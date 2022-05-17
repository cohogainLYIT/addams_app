-- CREATE DATABASE addams;
use addams;
SET autocommit = 1;

CREATE TABLE IF NOT EXISTS bookings (
  booking_id int not NULL AUTO_INCREMENT,
  reservation_name varchar(50) DEFAULT NULL,
  reservation_date date DEFAULT NULL,
  guests int DEFAULT NULL,
  accomodation varchar(50) DEFAULT NULL,
  nice_to_have varchar(255) DEFAULT NULL,
  PRIMARY KEY (booking_id)
);

CREATE TABLE IF NOT EXISTS accomodations (
  accomodation_name varchar(50) DEFAULT NULL,
  max_guests int DEFAULT NULL,
  booked bool DEFAULT FALSE
);

INSERT INTO accomodations
  (accomodation_name, max_guests, booked)
VALUES
  ('Shadowy Shack',4,FALSE),
  ('Creepy Caravan',2,FALSE),
  ('Haunted House',6,FALSE),
  ('Demonic Domicile',6,FALSE),
  ('Condemned Condominium',8,FALSE),
  ('Macabre Mansion',10,FALSE),
  ('Poltergeist Palace',20,FALSE),
  ('Campsite Cemetery',250,FALSE);

CREATE TABLE IF NOT EXISTS accounts (
	id int(11) NOT NULL AUTO_INCREMENT,
  	username varchar(50) NOT NULL,
  	password varchar(255) NOT NULL,
  	email varchar(100) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO accounts (id, username, password, email) VALUES (1, 'Gomez', 'Fester', 'GomezAddams@addamsfamily.com');

DELIMITER //
CREATE PROCEDURE CreateBooking(
	IN req_name varchar(50),
  IN req_date date,
  IN req_guests int,
  IN nicetohave varchar(255)
)
BEGIN
  SET @availableaccomo = (
  SELECT accomodation_name FROM accomodations
	WHERE max_guests >= req_guests and booked <> TRUE
  ORDER BY max_guests
  LIMIT 1);

  INSERT INTO bookings
    (reservation_name, reservation_date, guests, accomodation, nice_to_have)
  VALUES
    (req_name, req_date, req_guests, @availableaccomo, nicetohave);

  UPDATE accomodations SET booked = TRUE
  WHERE accomodation_name=@availableaccomo;

  SELECT accomodation, reservation_date, booking_id from bookings
  WHERE accomodation = @availableaccomo and reservation_name = req_name and reservation_date = req_date;
  
  COMMIT;
END  //

DELIMITER ;
