-- models/preprocessed_data_transformation.sql

SELECT 
    channel_title,
    channel_username,
    id,
    message,
    date::TIMESTAMP WITH TIME ZONE AS date,
    media_path,
    NULLIF(REGEXP_REPLACE(price, '[^0-9]', '', 'g'), '')::NUMERIC AS price,
    phone_number,
    telegram_address,
    location
FROM 
    public."MyTgData"
