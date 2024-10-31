-- Секция 2. Практическое задание SQL/PostgreSQL

-- 2.1
SELECT user_id, SUM(reward) AS total_reward_2022
FROM reports
WHERE user_id IN (
    SELECT user_id
    FROM reports
    GROUP BY user_id
    HAVING MIN(created_at) >= '2021-01-01' AND MIN(created_at) < '2022-01-01'
)
AND EXTRACT(YEAR FROM created_at) = 2022
GROUP BY user_id;


-- 2.2
SELECT pos.title AS pos_title, reports.barcode, reports.price
FROM reports
JOIN pos ON reports.pos_id = pos.id
WHERE pos.title IN (
    SELECT title
    FROM pos
    GROUP BY title
    HAVING COUNT(*) > 1
)
ORDER BY pos.title, reports.barcode;
