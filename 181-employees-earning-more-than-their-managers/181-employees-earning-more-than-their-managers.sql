/* Write your T-SQL query statement below */
select a.name as Employee
from Employee as a, Employee as b
where a.ManagerId = b.id and a.salary > b.salary