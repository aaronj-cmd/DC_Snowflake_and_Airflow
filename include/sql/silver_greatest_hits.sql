CREATE OR REPLACE VIEW silver_greatest_hits AS (
    SELECT
        album.albumid,
        album.title AS album_name,
        artist.name AS artist_name,

        -- Determine if an album is a "Greatest Hits" album
        CASE
            WHEN album_name ILIKE '%greatest%' THEN TRUE
            ELSE FALSE
        END AS is_greatest_hits

    FROM album
    JOIN artist ON album.artistid = artist.artistid
);
