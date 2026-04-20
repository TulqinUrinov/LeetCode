"""Ishchilarning bonuslari
Jadval: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| empId       | int     |
| name        | varchar |
| supervisor  | int     |
| salary      | int     |
+-------------+---------+
empId — bu jadval uchun yagona qiymatlarga ega ustun hisoblanadi. Jadvalning har bir qatori xodimning ismi, ID raqami, maoshi va ularning managerId (ya'ni, rahbari ID raqami) haqidagi ma'lumotlarni o‘z ichiga oladi.

Jadval: Bonus

+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+
empId — bu jadval uchun yagona qiymatlarga ega ustun hisoblanadi. empId — bu Employee jadvalidagi empId ustuniga murojaat qiluvchi tashqi kalit hisoblanadi. Jadvalning har bir qatori xodimning id raqami va unga tegishli bonus miqdorini o‘z ichiga oladi.

Vazifa: Bonus miqdori 1000 dan kam bo‘lgan har bir xodimning ismi va bonus miqdorini ko‘rsatadigan so‘rov yozing.

💡 Natijada qaytadigan jadval istalgan tartibda bo‘lishi mumkin.

Natijaning ko‘rinishi quyidagi misolda keltirilgan.

Misol 1:

Misol uchun kiritilgan ma'lumot:
Employee jadvali:

+-------+--------+------------+--------+
| empId | name   | supervisor | salary |
+-------+--------+------------+--------+
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |
+-------+--------+------------+--------+

Bonus table:
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
Kutilgan natija:
+------+-------+
| name | bonus |
+------+-------+
| Brad | null  |
| John | null  |
| Dan  | 500   |
+------+-------+
"""


class SQL:

    def bonus(self):
        query = """
        SELECT Employee.empId, Bonus.bonus FROM Employee 
        LEFT JOIN Bonus ON Employee.empId = Bonus.empId
        WHERE Bonus.bonus < 1000 OR Bonus.bonus IS NULL;
        """
        return query
