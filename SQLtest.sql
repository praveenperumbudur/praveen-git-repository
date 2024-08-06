/*show databases*/
 
/*create database ustglobaldb*/
 
use classicmodels;
/*use cdb;*/
show tables;
desc employees
 
select * from employees

select * from orders
 
select firstName, lastname from employees
 
select concat(firstname, " ", lastname) as "Full Name"from employees
 
select now() datetime
 
select current_date()
 
select current_user()
 
select * from offices
 
select country, city, state,territory from offices order by country 
select country, city, state,territory from offices order by country desc
 
select country, city, state,territory from offices order by country asc , city desc
 
select country, city, state,territory from offices order by country desc , city asc
 
select country, city, state,territory from offices order by state desc
select * from orderdetails limit 10
 
select ordernumber, quantityordered*priceeach "bill_amount" from orderdetails order by bill_amount desc
 
select ordernumber, quantityordered, priceeach
, priceeach * quantityordered "totalprice"
from orderdetails 
order by priceeach * quantityordered desc
limit 10;
 
 
select ordernumber, quantityordered, priceeach
from orderdetails limit 10,10
 
select ordernumber, quantityordered, priceeach
, priceeach * quantityordered "totalprice"
from orderdetails 
order by priceeach * quantityordered desc
limit 1,1
 
select ordernumber, quantityordered, priceeach
from orderdetails limit 10 offset 5

#filtering
select * from orders where status = 'shipped'

select * from orders where status = 'shipped' order by orderdate limit 10

select * from employees where jobTitle = 'VP Marketing'

select distinct jobtitle from employees

select firstname,lastname from employees where jobTitle in ('President','VP Sales', 'VP Marketing')


select firstname,lastname from employees where jobTitle not in ('President','VP Sales', 'Vp Marketing')

select firstname,lastname from employees 
where
jobTitle in ('President','VP Sales', 'Vp Marketing')
OR officecode = 1

select firstname,lastname from employees 
where
jobTitle not in ('President','VP Sales', 'Vp Marketing')
OR officecode = 1

select * from orderdetails where quantityordered > 50

select * from orderdetails where quantityordered < 50 and priceEach >= 75

/* > < = <= >= != */

select  * from offices where addressline2 is null
select  * from offices where addressline2 is not null and state is null


select firstname , lastname, jobtitle,reportsto
from employees
where jobtitle in ('President', 'VP Sales','Sales Rep')
and reportsto is null

select * from products where productName like 'America%'

select * from products where productName like '%bus'

select * from products where productName like '%pickup%'

select firstname, lastname from employees 
where firstname like 'M%N'

select firstname, lastname from employees 
where firstname like 'L%e'

select productName from products where productname like '_____A%'

select firstname, lastname from employees 
where firstname like '__r%'

select firstname, lastname from employees 
where firstname like '__rr%'

select firstname, lastname from employees 
where firstname like '__r_r%'


select firstname, lastname from employees 
where firstname like '%r__d'

select firstname, lastname from employees 
where firstname like '____y'

select firstname, lastname from employees 
where firstname like '%y'

select firstname, lastname from employees 
where firstname not like '____y'
'2003-03-03'

select productname,productcode from products where productcode like '%\_20%';

select * from orders where orderdate >= '2003-01-01'
and orderdate <= '2003-03-03'

select * from orders where orderdate  between '2003-01-01' and '2003-03-03'

select productcode, productname, buyprice
from products
where  
buyprice between 90 and 100

select productcode, productname, buyprice
from products
where  
buyprice not between 90 and 100

select ordernumber,  requireddate,status from orders
where status in ('Shipped','In Process')
and 
requireddate between '2003-01-01' and '2003-03-03'

select count(*) from orders

select count(*) from orders where shippeddate is not null

select count(shippedDate) from orders

select * from orderdetails

select sum(priceeach), max(priceeach),min(priceeach),avg(priceeach),count(priceeach) from orderdetails

select count(distinct shippedDate) from orders

select count(*) ,shippeddate from orders group by shippeddate

select count(*),ordernumber,productcode from orderdetails group by ordernumber,productcode

select * from products

select * from productlines

select ordernumber, sum(priceeach*quantityordered) "total_price" , ordernumber from orderdetails
where quantityordered > 30
group by ordernumber
having total_price > 50000
order by ordernumber desc
limit 1 offset 1

select o.ordernumber, status ,sum(quantityordered*priceEach) as total from
orders o inner join orderdetails od using (ordernumber)
where status = 'IN PROCESS'
group by o.ordernumber
HAVING(TOTAL) > 6000
ORDER BY TOTAL DESC

SELECT CUSTOMERNAME, ORDERNUMBER,ORDERDATE,ORDERLINENUMBER,PRODUCTNAME,QUANTITYORDERED, PRICEEACH
FROM ORDERS INNER JOIN ORDERDETAILS USING(ORDERNUMBER)
INNER JOIN PRODUCTS USING (PRODUCTCODE)
INNER JOIN CUSTOMERS USING (CUSTOMERNUMBER)
ORDER BY ORDERNUMBER

SELECT ORDERNUMBER,PRODUCTNAME,MSRP, PRICEEACH
FROM PRODUCTS P INNER JOIN ORDERDETAILS O
ON P.PRODUCTCODE  = O.PRODUCTCODE
AND P.MSRP > O.PRICEEACH
WHERE P.PRODUCTCODE = 'S10_1678'

SELECT C.CUSTOMERNUMBER,CUSTOMERNAME, ORDERNUMBER,STATUS FROM CUSTOMERS C
LEFT JOIN ORDERS O ON O.CUSTOMERNUMBER = C.CUSTOMERNUMBER
WHERE ORDERNUMBER IS NOT NULL

SELECT C.CUSTOMERNUMBER,CUSTOMERNAME, ORDERNUMBER,STATUS FROM ORDERS O
RIGHT JOIN CUSTOMERS C ON O.CUSTOMERNUMBER = C.CUSTOMERNUMBER
WHERE ORDERNUMBER IS NOT NULL

SELECT LASTNAME,FIRSTNAME, CUSTOMERNAME,CHECKNUMBER,AMOUNT FROM
EMPLOYEES LEFT JOIN CUSTOMERS ON
EMPLOYEENUMBER = SALESREPEMPLOYEENUMBER
LEFT JOIN PAYMENTS ON
PAYMENTS.CUSTOMERNUMBER = CUSTOMERS.CUSTOMERNUMBER
ORDER BY CUSTOMERNAME , CHECKNUMBER

SELECT CONCAT(M.LASTNAME,' ', M.FIRSTNAME) AS MANAGER,
CONCAT(E.LASTNAME,' ',E.FIRSTNAME) AS EMPLOYEE
FROM EMPLOYEES E INNER JOIN EMPLOYEES M ON
M.EMPLOYEENUMBER = E.REPORTSTO
ORDER BY MANAGER





