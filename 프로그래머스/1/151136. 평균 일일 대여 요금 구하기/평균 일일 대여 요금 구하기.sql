-- 코드를 입력하세요
SELECT round(sum(DAILY_FEE)/count(*), 0) as AVERAGE_FEE from CAR_RENTAL_COMPANY_CAR where CAR_TYPE = 'SUV'