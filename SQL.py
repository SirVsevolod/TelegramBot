import sqlite3

class SQLighter:

    def __init__(self, database_file):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def get_subscriptions(self, status1=True):
        """получаем всех активных подписчиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM subscriptions WHERE status1 = ?", (status1,)).fetchall()

    def subscriber_exist(self, user_id):
        """проверяем есть ли юзер в базе"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM subscriptions WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id, status1=True):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO subscriptions (user_id,status1) VALUES (?,?)", (user_id, status1))

    def update_subscription(self, user_id, status1):
        """Обновляем статус подписки"""
        with self.connection:
            return self.cursor.execute("UPDATE subscriptions SET status1 = ? WHERE user_id = ?", (status1, user_id))

    def close(self):
        self.connection.close()
