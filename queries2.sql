
-- QUERY 1: Calculates the daily price changes in percentage using LAG()


-- SELECT
--     assets.ticker,
--     assets.asset_name,
--     daily_prices.trade_date,
--     daily_prices.close_price,
--     LAG(daily_prices.close_price) OVER(PARTITION BY daily_prices.asset_id ORDER BY daily_prices.trade_date) as yesterday_closeprice,
--     ((daily_prices.close_price - LAG(daily_prices.close_price) OVER(PARTITION BY daily_prices.asset_id ORDER BY daily_prices.trade_date)) / LAG(daily_prices.close_price) OVER(PARTITION BY daily_prices.asset_id ORDER BY daily_prices.trade_date)) * 100 AS daily_percentage_change

    
-- FROM daily_prices

-- JOIN
--     assets ON daily_prices.asset_id = assets.asset_id;


-- QUERY 2: Calculates the daily price changes in percentage using "WITH" to create Common Table Expressions (CTEs) to simplify the process

-- WITH lag_prices AS (
--     SELECT
--         assets.ticker,
--         assets.asset_name,
--         daily_prices.trade_date,
--         daily_prices.close_price,
--         LAG(close_price) OVER(PARTITION BY assets.asset_id ORDER BY daily_prices.trade_date) AS previous_price
--     FROM daily_prices

--     JOIN assets ON daily_prices.asset_id=assets.asset_id
    

-- SELECT 
--     ticker,
--     asset_name,
--     trade_date,
--     close_price,
--     previous_price,
--     ((close_price - previous_price)/previous_price) * 100 AS daily_percentage_change

-- FROM lag_prices
-- WHERE previous_price IS NOT NULL;


-- QUERY 3: Calculating the 20 day moving average. 
-- Issue: averages out close_price even when 20 previous close price data aren't included.

    
-- SELECT  
--     assets.ticker,
--     assets.asset_name,
--     daily_prices.trade_date,
--     AVG(daily_prices.close_price) OVER(
--         PARTITION BY assets.asset_id 
--         ORDER BY daily_prices.trade_date
--         ROWS BETWEEN 19 PRECEDING AND CURRENT ROW) AS moving_average_20d

-- FROM daily_prices

-- JOIN assets ON assets.asset_id = daily_prices.asset_id; 



 
-- QUERY 4: Calculates 20 day moving average and constraints it only when 20 previous day close_price is available. 

SELECT  
    assets.ticker,
    assets.asset_name,
    daily_prices.trade_date,
    daily_prices.close_price,
    CASE 
        WHEN COUNT(daily_prices.close_price) OVER (
            PARTITION BY assets.asset_id 
            ORDER BY daily_prices.trade_date
            ROWS BETWEEN 19 PRECEDING AND CURRENT ROW
        ) = 20 
        THEN ROUND(
            AVG(daily_prices.close_price) OVER (
                PARTITION BY assets.asset_id 
                ORDER BY daily_prices.trade_date
                ROWS BETWEEN 19 PRECEDING AND CURRENT ROW
            ), 2
        )
        ELSE NULL 
    END AS moving_average_20d
FROM daily_prices
JOIN assets ON assets.asset_id = daily_prices.asset_id;