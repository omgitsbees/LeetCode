WITH SalesWithSeason AS (
    -- Step 1: Assign Season to Sales
    SELECT
        product_id,
        quantity,
        price,
        CASE
            WHEN MONTH(sale_date) IN (12, 1, 2) THEN 'Winter'
            WHEN MONTH(sale_date) IN (3, 4, 5) THEN 'Spring'
            WHEN MONTH(sale_date) IN (6, 7, 8) THEN 'Summer'
            WHEN MONTH(sale_date) IN (9, 10, 11) THEN 'Fall'
        END AS season
    FROM
        sales
),
SeasonalCategoryStats AS (
    -- Step 2: Calculate Seasonal Category Metrics
    SELECT
        sws.season,
        p.category,
        SUM(sws.quantity) AS total_quantity,
        SUM(sws.quantity * sws.price) AS total_revenue
    FROM
        SalesWithSeason sws
    JOIN
        products p ON sws.product_id = p.product_id
    GROUP BY
        sws.season,
        p.category
),
RankedSeasonalCategory AS (
    -- Step 3: Rank Categories within Each Season
    SELECT
        season,
        category,
        total_quantity,
        total_revenue,
        ROW_NUMBER() OVER (PARTITION BY season ORDER BY total_quantity DESC, total_revenue DESC) as rn
    FROM
        SeasonalCategoryStats
)
-- Step 4 & 5: Select Top Category per Season and Order Results
SELECT
    season,
    category,
    total_quantity,
    CAST(total_revenue AS DECIMAL(10, 2)) AS total_revenue -- Ensure revenue format matches example
FROM
    RankedSeasonalCategory
WHERE
    rn = 1
ORDER BY
    season ASC;
