use classicmodels;

SELECT CUSTOMERNUMBER, CHECKNUMBER, AMOUNT FROM PAYMENTS
WHERE AMOUNT = (SELECT MAX(AMOUNT) FROM PAYMENTS);

SELECT CUSTOMERNUMBER, CHECKNUMBER, AMOUNT FROM PAYMENTS
WHERE AMOUNT > (SELECT max(amount) from payments);

SELECT CUSTOMERNAME FROM CUSTOMERS WHERE CUSTOMERNUMBER NOT IN (SELECT DISTINCT CUSTOMERNUMBER FROM ORDERS);

SELECT MAX(ITEMS),MIN(ITEMS),FLOOR(AVG(ITEMS)) FROM (SELECT ORDERNUMBER,COUNT(ORDERNUMBER) AS ITEMS
FROM ORDERDETAILS GROUP BY ORDERNUMBER) AS LINEITEMS;

SELECT PRODUCTNAME,BUYPRICE,PRODUCTLINE FROM PRODUCTS P WHERE BUYPRICE > (
SELECT AVG(BUYPRICE) FROM PRODUCTS P1 WHERE P.PRODUCTLINE = P1.PRODUCTLINE
);

SELECT lastName, firstName
FROM Employees
WHERE  EXISTS (SELECT officeCode
        FROM offices
        WHERE Country = 'USA');
        
SELECT
    productLine,
    YEAR(orderDate) orderYear,
    SUM(quantityOrdered * priceEach) orderValue
FROM
    orderDetails
        INNER JOIN
    orders USING (orderNumber)
        INNER JOIN
    products USING (productCode)
GROUP BY
    productLine ,
    YEAR(orderDate);
SELECT 
 productline, 
    SUM(orderValue) totalOrderValue
FROM
    sales
GROUP BY 
    productline
union all
SELECT 
null,
    SUM(orderValue) totalOrderValue
FROM
    sales;
    
    
SELECT  productLine,   orderyear, SUM(orderValue) totalOrderValue
FROM sales
GROUP BY productline,orderyear with rollup;

select * from products

select lower(productname), upper(productname)
,length(productname)
from products;

select productname, left(productname,5) ,right(productname,10) from products

select reverse(status), status from orders

select productname, locate(productname,"1969") position from products

select locate('harley','1969 harley davidson ultimate chopper') from products

select repeat('*', 50)

select substring(productname, 5) from products

select substring(productname, -10) from products

select substring(productname, 5,10) from products

select substring(productname, -10) ,substring(productname, -10,5) from products

select format(12500.2015,2), format(12500.2015,0);

select creditlimit, format(creditlimit,0, 'de_DE') from customers

productname,
    CONCAT('$',
            FORMAT(quantityInStock * buyPrice, 2)) stock_value