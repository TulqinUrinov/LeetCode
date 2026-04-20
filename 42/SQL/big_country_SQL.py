"""
Katta davlatlarni topish
Jadval: World

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
name ustuni ushbu jadvalning asosiy kaliti hisoblanadi (ya'ni, har bir satrda bu ustun uchun qiymat yagona bo‘ladi). Jadvalning har bir satrida [name] = mamlakat nomi, uning qaysi continent = qit'aga tegishli ekani, area = maydoni, population = aholisi va gdp = yalpi ichki mahsuloti haqidagi ma'lumotlar berilgan.

Davlat katta bo'ladi agar:

Uning maydoni kamida 3 million km² bo‘lsa (ya'ni, 3000000 km² yoki undan katta), yoki
Aholisi kamida 25 million bo‘lsa (ya'ni, 25000000 yoki undan ko‘p).
Vazifa: Katta davlatlarning nomi, aholisi va maydonini topuvchi yechim yozing.

💡 Natijalar jadvalini istalgan tartibda chiqarishingiz mumkin.

Natijaning ko‘rinishi quyidagi misolda keltirilgan.

Misol 1:

Misol uchun kiritilgan ma'lumot:
World jadvali:

| name          | continent | area    | population | gdp          |
|---------------|-----------|---------|------------|--------------|
| Afg'oniston   | Osiyo     | 652230  | 25500100   | 20343000000  |
| Albaniya      | Yevropa   | 28748   | 2831741    | 12960000000  |
| Jazoir        | Afrika    | 2381741 | 37100000   | 188681000000 |
| Andorra       | Yevropa   | 468     | 78115      | 3712000000   |
| Angola        | Afrika    | 1246700 | 20609294   | 100990000000 |
Kutilgan natija:
| name        | population | area    |
|-------------|------------|---------|
| Afg'oniston | 25500100   | 652230  |
| Jazoir      | 37100000   | 2381741 |
"""

class SQL:

    def big_country(self):
        query = """
        SELECT name, population, area
        FROM World
        WHERE area > 30000000
        AND population > 25000000
        """
        return query
