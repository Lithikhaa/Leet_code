
WITH helper AS
(
    SELECT 
        E.name Employee, 
        E.salary Salary,
        D.name Department,
         DENSE_RANK() OVER (PARTITION BY E.departmentId ORDER BY E.salary DESC) AS srank
      
    FROM Employee E JOIN Department D
    ON D.id = E.departmentId
)
SELECT 
    Employee, 
    Salary,
    Department
FROM helper
WHERE srank < 4;