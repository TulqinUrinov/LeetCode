"""
Mijozni kim tavsiya qilganini aniqlash
Jadval: Customer

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
SQL tilida id ustuni ushbu jadval uchun asosiy kalit hisoblanadi. Jadvalning har bir qatori mijozning id -id raqami, name - ismi va referee_id - uni tavsiya qilgan mijozning id raqamini ifodalaydi.

Vazifa id = 2 bo‘lgan mijoz tomonidan tavsiya qilinmagan mijozlarning ismlarini toping.

💡 Natija qaytadigan jadval istalgan tartibda bo‘lishi mumkin.

Natijaning ko‘rinishi quyidagi misolda keltirilgan.

Misol 1:

Misol uchun kiritilgan ma'lumot:
Customer jadvali:

+----+------+---------------+
| id | name    | referee_id |
+----+------+---------------+
| 1  | Anvar   | null       |
| 2  | Azimjon | null       |
| 3  | Oybek   | 2          |
| 4  | Otabek  | null       |
| 5  | Olim    | 1          |
| 6  | Diyor   | 2          |
+----+------+---------------+
Kutilgan natija:
+---------+
| name    |
+---------+
| Anvar   |
| Azimjon |
| Otabek  |
| Olim    |
+---------+
"""

class SQL:

    def prefer(self):
        query = """
        SELECT name 
        FROM Customer
        WHERE referee_id != 2
        """

        return query
