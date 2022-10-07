create table ticket 
(
	pnr int,
    Train_no int,
    travel_date date,
    departure datetime,
    arrival datetime,
    departure_time time,
    arrival_time time,
    user_id int,
    train_type varchar(50),
    compartment_type varchar(50),
    compartment_no int,
    primary key (pnr),
    foreign key(user_id) references user(user_id)
);

create table payment_info
(
	transaction_id int,
    bank varchar(40),
    card_number int,
    price int ,
    pnr int,
    foreign key (pnr) references ticket(pnr),
    primary key (transaction_id)
);


create table ticket_passenger
(
	seat_no int,
    name varchar(50),
    age int,
    pnr int,
    primary key(seat_no),
    foreign key (pnr) references ticket(pnr)
);

create table fare_table
(
	Train_type varchar(50),
    compartment_type varchar(50),
    fare_per_km int,
    primary key (train_type,compartment_type)
);

alter table train modify name varchar(50) not null, modify train_type varchar(50) not null, modify availability varchar(3);
set sql_safe_updates=1;
update compartment set Availability =  "yes";

alter table train add unique(train_no);
alter table user add check (age>5);
alter table ticket_passenger rename passenger_ticket;


