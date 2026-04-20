"""
Qayta ishlanishi mumkin bo'lgan va kam yog'li mahsulotlar
Jadval: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id — bu jadvaldagi har bir mahsulot uchun yagona va takrorlanmas raqam (asosiy kalit). low_fats — mahsulotning yog' miqdorini bildiruvchi ustun bo‘lib, unda quyidagi qiymatlar bo‘ladi:

'Y' — mahsulot kam yog'li,
N' — mahsulot kam yog'li emas.
recyclable — mahsulotning qayta ishlanish imkoniyatini bildiruvchi ustun bo‘lib, unda quyidagi qiymatlar bo‘ladi:

'Y' — mahsulot qayta ishlanishi mumkin,
'N' — mahsulot qayta ishlanishi mumkin emas.
Vazifa: Kam yog'li va qayta ishlanishi mumkin bo‘lgan mahsulotlarning id raqamlarini topuvchi so'rov yozing.

💡 Natijada qaytadigan jadval istalgan tartibda bo‘lishi mumkin.

Natijaning ko‘rinishi quyidagi misolda keltirilgan:

Misol 1:

Misol uchun kiritilgan ma'lumot:
Products jadvali:

+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Kutilgan natija:
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
Tushuntirish:
Faqatgina 1 va 3-raqamli mahsulotlar ham kam yog'li, ham qayta ishlanishi mumkin.
"""


class SQL:

    def sql(self):
        query = """
        SELECT product_id 
        FROM Products
        WHERE low_fats = 'Y'
        AND recyclable = 'Y'
        """
        return query
