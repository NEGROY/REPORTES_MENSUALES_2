CTE
select month(so.orderdate Mes,
C. companyname as Cliente
Sum (unitprice qty) as Total
from Sales Orders as 50
join sales OrderDetails as SOD
on so orderid - sod orderid
join Sales. Customers as C
on SO custid C.custid
where year (so orderdate) 2015
group by MONTH (SO orderdate),
C. companyname
select Cliente, COALESCE ([1],0) AS 'Enero'
COALESCE([2], 0) AS "Febrero
COALESCE([3] 0) AS "Marzo
COALESCE([4], 0) AS 'Abril'
COALESCE ([5] 0) AS "Mayo",
COALESCE([6] 0) AS Junio
COALESCE [7] 0) AS 'Julio'
COALESCE([8] 0) AS 'Agosto
COALESCE ([9] 0) AS 'Septiembre',
COALESCE ([10] 0) AS 'Octubre
COALESCE ([11] 0) AS 'Noviembre,
COALESCE([12], 0) AS 'Diciembre
from Ventas
pivot (sum(total) for Mes in ([1], [2]. [3], [4],[5],[6], [7], [8], [9] [10], [11], [12])) as M


https://www.youtube.com/watch?v=CZ4joIrKQTM


