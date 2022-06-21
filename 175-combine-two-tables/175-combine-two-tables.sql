/* Write your T-SQL query statement below */
SELECT per.firstName, per.lastName, addr.city, addr.state
FROM Person per
left join Address addr on addr.personId = per.personId