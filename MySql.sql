CREATE TABLE investor (
        id INT AUTO_INCREMENT, 
        name  VARCHAR(255) NOT NULL, 
        address VARCHAR (255),
        status VARCHAR(10) NOT NULL,
        PRIMARY KEY(id)
);

CREATE TABLE account (
        id INT AUTO_INCREMENT, 
        investor_id  INT NOT NULL, 
        balance DECIMAL (10,2) NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY (investor_id) REFERENCES investor(id)
);

CREATE TABLE portfolio (
        id INT AUTO_INCREMENT, 
        account_id  INT NOT NULL, 
        ticker VARCHAR(10) NOT NULL,
        quantity INT NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY (account_id) REFERENCES account(id)
);

-- Investor Data
INSERT INTO investor (name, address, status) VALUES ('Jhon Doe' , '111 Main St' , 'ACTIVE');
INSERT INTO investor (name, address, status) VALUES ('James Doe' , '222 Main St' , 'ACTIVE'); 
INSERT INTO investor (name, address, status) VALUES ('Jane Doe' , '333 Main St' , 'INACTIVE');
INSERT INTO investor (name, address, status) VALUES ('Jack Doe' , '444 Main St' , 'ACTIVE'); 
insert into investor (name, address, status) values ('Jeff Doe','888 Main St',"INACTIVE");
insert into investor (name, address, status) values ('Jenny Doe','999 Main St',"INACTIVE");
insert into investor (name, address, status) values ('Jimmy Doe','1010 Main St',"INACTIVE");
insert into investor (name, address, status) values ('Jim Doe','1111 Main St',"INACTIVE");
insert into investor (name, address, status) values ('Jerry Doe','1212 Main St',"INACTIVE");

-- Account Data 
INSERT INTO account (investor_id, balance) VALUES (1 , 1000.00);
INSERT INTO account (investor_id, balance) VALUES (2 , 500.00);
INSERT INTO account (investor_id, balance) VALUES (3 , 2000.00);
INSERT INTO account (investor_id, balance) VALUES (4 , 700.00);
INSERT INTO account (investor_id, balance) VALUES (6 , 1100.00);
INSERT INTO account (investor_id, balance) VALUES (7 , 2200.00);
INSERT INTO account (investor_id, balance) VALUES (8 , 400.00);


INSERT INTO portfolio (account_id, ticker, quantity) VALUES (1 , 'MSFT', 10);
INSERT INTO portfolio (account_id, ticker, quantity) VALUES (2 , 'FB', 12);
INSERT INTO portfolio (account_id, ticker, quantity) VALUES (3 , 'amz', 8);
INSERT INTO portfolio (account_id, ticker, quantity) VALUES (4 , 'FB', 4);
INSERT INTO portfolio (account_id, ticker, quantity) VALUES (6 , 'FB', 12);
INSERT INTO portfolio (account_id, ticker, quantity) VALUES (7 , 'amz', 8);
INSERT INTO portfolio (account_id, ticker, quantity) VALUES (8 , 'FB', 4);


SELECT * FROM investor;
SELECT * FROM  account;
Select*from portfolio;

select name, address, status, id from investor where id = 1;
select name, address, status, id from investor where name = 'Jane Doe';
select* from investor;


alter table account modify balance integer;
update investor set address='101010 Coit Sr' where address = '111 Main St' and name= 'Jhon Doe';
update investor set name = 'Jackie Doe' where id = 2;
update portfolio set quantity =221 where ticker = 'FB' and id =8;
select portfolio.account_id from((account inner join investor on account.investor_id = investor.id) inner join portfolio on account.id = portfolio.account_id) where investor.status = "ACTIVE";

delete from portfolio where id = 1;
delete from account where id = 1;
delete from investor where id = 1;
delete from account where investor_id = 1; 
delete from investor where id = 1 ;
alter table account modify balance integer;

select balance from account where id=2