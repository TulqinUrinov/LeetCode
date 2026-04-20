"""
Maqolalar ko'rilishi
Jadval: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
Ushbu jadval uchun asosiy kalit (ya'ni, yagona qiymatlarga ega ustun) mavjud emas, jadvalda takroriy qatorlar bo‘lishi mumkin. Jadvalning har bir qatori shuni bildiradiki, kimdir biror maqolani (muallif tomonidan yozilgan) ma'lum bir sanada ko‘rgan. Shuni ham unutmangki, author_id va viewer_id bir xil bo‘lsa, bu bir inson ekanligini anglatadi.

Vazifa: Hech bo‘lmaganda o‘z maqolalaridan birini ko‘rgan barcha mualliflarni topuvchi so‘rov yozing.

💡 Natijada qaytadigan jadval id ustuni bo‘yicha ko‘payish tartibida (ascending) saralanishi kerak.

Natijaning ko‘rinishi quyidagi misolda keltirilgan.

Misol 1:

Misol uchun kiritilgan ma'lumot:
Views table:

+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Kutilgan natija:
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
"""


class SQL:

    def author(self):
        query = """
        SELECT author_id 
        FROM Views
        WHERE author_id = viewer_id
        ORDER BY author_id ASC;
        """
        return query
