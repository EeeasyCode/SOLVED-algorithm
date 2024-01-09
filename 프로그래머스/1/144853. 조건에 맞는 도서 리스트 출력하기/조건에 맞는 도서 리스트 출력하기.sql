-- 코드를 입력하세요
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') from BOOK where PUBLISHED_DATE like '2021%' and CATEGORY = '인문' order by BOOK_ID ASC;