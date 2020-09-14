SELECT date_format(str_to_date(date, '%d/%m/%Y'), '%d/%m/%Y') AS Date, SUM(prod_qty) AS Ventes
FROM transactions
WHERE STR_TO_DATE(date, '%d/%m/%Y') BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY date