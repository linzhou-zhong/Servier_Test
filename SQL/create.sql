CREATE TABLE IF NOT EXISTS `transactions` (
  `order_id` int(16) NOT NULL,
  `client_id` int(16) NOT NULL,
  `prod_id` int(16) NOT NULL,
  `prod_price` double NOT NULL,
  `prod_qty` int(16) NOT NULL,
  `date` varchar(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS `product_nomEnclature` (
  `product_id` int(16) NOT NULL,
  `product_type` varchar(200) NOT NULL,
  `product_name` varchar(200) NOT NULL,
   PRIMARY KEY (`product_id`)
);

INSERT INTO `transactions` (`order_id`, `client_id`, `prod_id`,`prod_price`,`prod_qty`,`date`) VALUES
  (1234, 999, 490756, 50, 1, '23/03/20'),
  (1234, 999, 389728, 3.56, 4, '01/04/19'),
  (3456, 845, 490756, 23, 2, '19/09/19'),
  (3456, 845, 549380, 56, 10, '01/04/19'),
  (3456, 845, 293718, 56, 23, '12/08/19');

INSERT INTO `product_nomEnclature` (`product_id`, `product_type`, `product_name`) VALUES
  (490756, 'MEUBLE', 'Chaise'),
  (389728, 'DECO', 'Boule de Noel'),
  (549380, 'MEUBLE', 'Canape'),
  (293718, 'DECO', 'Mug');