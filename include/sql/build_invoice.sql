CREATE OR REPLACE VIEW silver_detailed_invoice AS (
    SELECT
        invoice_line.invoiceid, 
        track.albumid, 
        invoice.total
    FROM invoice_line
    LEFT JOIN invoice ON invoice_line.invoiceid = invoice.invoiceid
    LEFT JOIN track ON invoice_line.trackid = track.trackid
);
