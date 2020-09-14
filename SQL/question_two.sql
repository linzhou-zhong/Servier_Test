SELECT t1.client_id, t1.ventes_meuble, t2.ventes_deco FROM
  (SELECT ts.client_id, sum(ts. prod_qty) AS ventes_meuble
  FROM transactions as ts, product_nomEnclature AS pn
  WHERE ts.prod_id = pn.product_id
  AND pn.product_type = 'MEUBLE'
  AND STR_TO_DATE(ts.date, '%d/%m/%Y') BETWEEN '2019-01-01' AND '2019-12-31'
  GROUP BY ts.client_id) AS t1
  
  inner join
  
  (SELECT ts.client_id, sum(ts. prod_qty) as ventes_deco
  FROM transactions as ts, product_nomEnclature as pn
  WHERE ts.prod_id = pn.product_id
  AND pn.product_type = 'DECO'
  AND STR_TO_DATE(ts.date, '%d/%m/%Y') BETWEEN '2019-01-01' AND '2019-12-31'
  GROUP BY ts.client_id) AS t2
  
  ON t1.client_id = t2.client_id

-- Second Solution
SELECT ts.client_id, 
SUM( CASE WHEN pn.product_type = 'MEUBLE' THEN ts.prod_qty ELSE 0 END) AS ventes_meuble, 
SUM( CASE WHEN pn.product_type = 'DECO' THEN ts.prod_qty ELSE 0 END) AS ventes_deco
  FROM transactions as ts, product_nomEnclature AS pn
  WHERE ts.prod_id = pn.product_id
  AND STR_TO_DATE(ts.date, '%d/%m/%Y') BETWEEN '2019-01-01' AND '2019-12-31'
  GROUP BY ts.client_id