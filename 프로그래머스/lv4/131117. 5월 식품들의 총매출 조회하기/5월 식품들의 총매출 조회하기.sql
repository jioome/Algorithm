-- 코드를 입력하세요
SELECT fp.product_id, fp.product_name, (fp.price)*sum(fo.amount) as total_sales


from food_product as fp
join food_order as fo
on fp.product_id = fo.product_id
where year(fo.PRODUCE_DATE )= 2022 and month(fo.PRODUCE_DATE)=5
group by fp.product_id 
order by total_sales desc, fp.product_id asc;