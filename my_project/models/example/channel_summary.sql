-- models/channel_summary.sql

SELECT 
    channel_title,
    COUNT(*) AS message_count,
    AVG(price) AS average_price
FROM 
    {{ ref('preprocessed_data_transformation') }}  -- Reference the preprocessed data model
GROUP BY 
    channel_title
