WITH cte AS (
    -- Find policyholders whose tiv_2015 appears more than once
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) >= 2
),

cte2 AS (
    -- Find policyholders who meet both conditions:
    -- 1. Their tiv_2015 appears in the above CTE
    -- 2. Their (lat, lon) is unique
    SELECT i.pid, i.tiv_2016
    FROM Insurance i
    WHERE i.tiv_2015 IN (SELECT tiv_2015 FROM cte)
    AND (lat, lon) IN (
        SELECT lat, lon
        FROM Insurance
        GROUP BY lat, lon
        HAVING COUNT(*) = 1
    )
)

-- Sum tiv_2016 for the filtered policyholders
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM cte2;
