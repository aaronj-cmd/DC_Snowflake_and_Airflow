SELECT
    gh.album_name,
    gh.artist_name,
    SUM(di.total) AS total_sales_driven
FROM silver_detailed_invoice AS di
JOIN silver_greatest_hits AS gh ON di.albumid = gh.albumid
WHERE di.albumid IN (
    SELECT albumid FROM silver_greatest_hits WHERE is_greatest_hits
)
GROUP BY gh.album_name, gh.artist_name, gh.is_greatest_hits
ORDER BY total_sales_driven DESC;
