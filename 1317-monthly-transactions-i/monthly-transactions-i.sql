SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month,  -- Corrected date format
    country,
    COUNT(*) AS trans_count,  -- Count all transactions
    COUNT(CASE WHEN state = 'approved' THEN 1 END) AS approved_count,  -- Count only approved transactions
    SUM(amount) AS trans_total_amount,  -- Sum of all transaction amounts
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount  -- Sum of approved transactions
FROM Transactions
GROUP BY country, month; 