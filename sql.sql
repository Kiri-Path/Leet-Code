###  RIDE HAILING

SELECT cities.name, SUM(rides.fare) AS earnings
FROM cities
JOIN drivers ON cities.id = drivers.city_id
JOIN rides ON drivers.id = rides.driver_id
GROUP BY cities.name
ORDER BY earnings ASC, cities.name ASC;



select c.name, sum(r.fare)
from cities c
join users u 
on u.city_id  = c.id
join rides r 
on r.user_id = u.id
group by c.name
order by 2,1


select u.name, sum(r.distance)
from users u
join rides r 
on u.id = r.user_id
group by u.id, u.name
order by 2 desc 1 asc
limit 100






### FAMILIES COUNTRY
  

select count(name)
from countries
where min_size <= (select max(family_size) from families)



#### CAMPAIGNS SUCCESS FAILURE

  

WITH SuccessCounts AS (
  SELECT
    c.id AS customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer,
    COUNT(e.status) AS total
  FROM
    Customers c
    JOIN Campaigns ca ON c.id = ca.customer_id
    JOIN Events e ON ca.id = e.campaign_id
  WHERE
    e.status = 'success'
  GROUP BY
    c.id,
    c.first_name,
    c.last_name
  ORDER BY
    total DESC
  LIMIT 1
),
FailureCounts AS (
  SELECT
    c.id AS customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer,
    COUNT(e.status) AS total
  FROM
    Customers c
    JOIN Campaigns ca ON c.id = ca.customer_id
    JOIN Events e ON ca.id = e.campaign_id
  WHERE
    e.status = 'failure'
  GROUP BY
    c.id,
    c.first_name,
    c.last_name
  ORDER BY
    total DESC
  LIMIT 1
),
CustomerCampaigns AS (
  SELECT
    c.id AS customer_id,
    GROUP_CONCAT(ca.name ORDER BY ca.name ASC) AS campaigns
  FROM
    Customers c
    JOIN Campaigns ca ON c.id = ca.customer_id
  GROUP BY
    c.id
),
FinalResult AS (
  SELECT
    'success' AS event_type,
    s.customer,
    cc.campaigns,
    s.total
  FROM
    SuccessCounts s
    JOIN CustomerCampaigns cc ON s.customer_id = cc.customer_id
  UNION ALL
  SELECT
    'failure' AS event_type,
    f.customer,
    cc.campaigns,
    f.total
  FROM
    FailureCounts f
    JOIN CustomerCampaigns cc ON f.customer_id = cc.customer_id
)
SELECT
  event_type,
  customer,
  campaigns,
  total
FROM
  FinalResult;





#### ORDER QUERY


WITH EarliestOrder AS (
  SELECT MIN(ORDER_DATE) AS earliest_order_date
  FROM `your_dataset.Orders`
),
ValidOrders AS (
  SELECT *
  FROM `your_dataset.Orders`
  WHERE ORDER_DATE <= DATE_ADD((SELECT earliest_order_date FROM EarliestOrder), INTERVAL 10 YEAR)
),
MaxPrice AS (
  SELECT MAX(PRICE) AS max_price
  FROM ValidOrders
)
SELECT c.NAME, o.PRICE
FROM `your_dataset.Customers` c
JOIN `your_dataset.Orders` o ON c.ORDER_ID = o.ID
JOIN MaxPrice mp ON o.PRICE = mp.max_price
WHERE o.ORDER_DATE <= DATE_ADD((SELECT earliest_order_date FROM EarliestOrder), INTERVAL 10 YEAR);




### goals scored


SELECT 
  c.ID AS country_id,
  c.NAME AS country_name,
  SUM(g.goals) AS goals_scored
FROM 
  Goals g
JOIN 
  Players p ON g.player_id = p.ID
JOIN 
  Countries c ON g.country_id = c.ID
GROUP BY 
  c.ID, c.NAME
ORDER BY 
  goals_scored DESC,
  c.ID ASC;
