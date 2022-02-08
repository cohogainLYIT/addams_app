-- CREATE DATABASE addams;
use addams;

CREATE TABLE bookings (
  booking_id int not NULL AUTO_INCREMENT,
  reservation_name varchar(50) DEFAULT NULL,
  reservation_date date DEFAULT NULL,
  guests int DEFAULT NULL,
  accomodation varchar(50) DEFAULT NULL,
  PRIMARY KEY (booking_id)
);


CREATE TABLE accomodations (
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

DELIMITER //
CREATE PROCEDURE CreateBooking(
	IN req_name varchar(50),
  IN req_date date,
  IN req_guests int
)
BEGIN
  SET @availableaccomo = (
  SELECT accomodation_name FROM accomodations
	WHERE max_guests >= req_guests and booked <> TRUE
  ORDER BY max_guests
  LIMIT 1);

  INSERT INTO bookings
    (reservation_name, reservation_date, guests, accomodation)
  VALUES
    (req_name, req_date, req_guests, @availableaccomo);
  
  UPDATE accomodations SET booked = TRUE 
  WHERE accomodation_name=@availableaccomo;
  
  SELECT accomodation, reservation_date, booking_id from bookings
  WHERE accomodation = @availableaccomo and reservation_name = req_name and reservation_date = req_date
  ;

END  //

DELIMITER ;
