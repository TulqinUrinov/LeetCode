"""
Noto'g'ri tvitlar
Jadval: Tweets

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id — bu jadval uchun asosiy kalit (takrorlanmaydigan yagona qiymatga ega ustun) hisoblanadi. content — bu ustunda tvit matni saqlanadi va u faqat harf-raqam (alphanumeric characters) belgilaridan, undov belgisi '!', yoki bo'sh joy ' ' dan iborat bo'lishi mumkin. Boshqa maxsus belgilar qatnashmaydi. Ushbu jadval ijtimoiy tarmoq ilovasidagi barcha tvitlarni o‘z ichiga oladi.

Vazifa: Noto'g'ri tvitlar id raqamlarini topuvchi so‘rov yozing. Tvit noto'g'ri hisoblanadi, agar undagi matn uzunligi qat'iy 15 belgidan oshsa.

💡 Natijada qaytadigan jadval istalgan tartibda bo'lishi mumkin.

Natijaning ko'rinishi quyidagi misolda keltirilgan.

Misol 1:

Misol uchun kiritilgan ma'lumot:
Tweets jadvali:

+----------+------------------------------------------------+
| tweet_id | content                                        |
+----------+------------------------------------------------+
| 1        | Kod yozamiz                                    |
| 2        | Bu yerda 15 dan ko'p harf-raqam belgilari bor! |
+----------+------------------------------------------------+
Kutilgan natija:
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
Tushuntirish:
1-id raqamli tvit uzunligi 11 ta belgi. Bu — to'g'ri tvit.

2-id raqamli tvit uzunligi 46 ta belgi. Bu — noto'g'ri tvit.
"""


class SQL:

    def tweet(self):
        query = """
        SELECT tweet_id
        FROM Tweets
        WHERE LENGTH(content) > 15;
        """

        return query
