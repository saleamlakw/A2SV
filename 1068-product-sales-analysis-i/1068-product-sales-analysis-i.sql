/* Write your T-SQL query statement below */
select Product.product_name,Sales.year,Sales.price from Sales
join Product
on Product.product_id = Sales.product_id;