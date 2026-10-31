-- Query 1: Joining assets and daily price table

-- SELECT 
--     assets.ticker,
--     assets.asset_name,
--     daily_prices.trade_date,
--     daily_prices.close_price
-- FROM daily_prices
-- JOIN assets ON daily_prices.asset_id = assets.asset_id; 
-- -- the order at which the columns are called after the SELECT is the order at which the column are ordered. ex. 1st column is ticker and last is close price


-- Query 2: After joining assets and daily_price table, calculate the avg,count,max, min close_prices.

-- SELECT 
--     assets.ticker,
--     assets.asset_name,
--     COUNT(daily_prices.trade_date) AS number_of_days,
--     MIN(daily_prices.close_price)  AS min_close_price,
--     MAX(daily_prices.close_price)  AS max_close_price,
--     ROUND(AVG(daily_prices.close_price), 2) AS avg_close_price
-- FROM daily_prices
-- JOIN assets ON daily_prices.asset_id = assets.asset_id
-- GROUP BY 
--     assets.ticker, 
--     assets.asset_name;

    -- all columns called on the select are included in the table made from JOIN


-- Query 3: Creates a joined table that shows the average volume per month ordered by the ticker and the month

SELECT
    assets.ticker,
    assets.asset_name,
    STRFTIME('%Y-%m', daily_prices.trade_date) AS year_month,
    ROUND(AVG(daily_prices.volume),0) AS average_volume

FROM daily_prices
JOIN assets ON daily_prices.asset_id = assets.asset_id
GROUP BY
     assets.ticker,
     year_month
ORDER BY 
    assets.ticker ASC,
    year_month ASC;    

-- In SQL, aggregate functions (AVG, SUM, COUNT, MIN, MAX) never decide the timeframe or scope.

-- SELECT decides what math to do; GROUP BY decides the boundaries of the data it does math on.