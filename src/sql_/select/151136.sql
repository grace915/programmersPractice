SELECT round(avg(daily_fee)) as AVERAGE_FEE
from car_rental_company_car
group by car_type
having car_type = 'SUV'