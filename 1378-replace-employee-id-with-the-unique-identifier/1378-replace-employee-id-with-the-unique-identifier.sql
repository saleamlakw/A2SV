/* Write your T-SQL query statement below */
select EmployeeUNI.unique_id,Employees.name from Employees 
left join EmployeeUNI
on Employees.id=EmployeeUNI.id;