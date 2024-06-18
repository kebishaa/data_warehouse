
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='view') }}

WITH fast_vehicles AS (
    SELECT *,
           AVG(SPEED) OVER (PARTITION BY VEHICLE_ID) AS avg_speed
    FROM trajectories
)

SELECT *
FROM fast_vehicles
ORDER BY avg_speed DESC
LIMIT 100;
