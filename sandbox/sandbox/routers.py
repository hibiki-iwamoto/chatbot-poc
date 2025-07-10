# myproject/routers.py

class AuthRouter:
    """
    'auth' アプリケーションのモデルに関するすべてのデータベース操作を
    'auth_db' に向けるためのルーター。
    """
    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin', 'two_factor', 'django_otp'}

    def db_for_read(self, model, **hints):
        """
        'auth' アプリ関連の読み込み操作は 'auth_db' を使用する。
        """
        if model._meta.app_label in self.route_app_labels:
            return 'auth_db'
        return None # Noneを返すとsettings.pyの'default'が使われる

    def db_for_write(self, model, **hints):
        """
        'auth' アプリ関連の書き込み操作は 'auth_db' を使用する。
        """
        if model._meta.app_label in self.route_app_labels:
            return 'auth_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        'auth' アプリ関連のオブジェクト間のリレーションを許可する。
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        'auth_db' には 'auth' アプリ関連のモデルのみマイグレーションする。
        それ以外のアプリは 'default' DB にマイグレーションする。
        """
        if app_label in self.route_app_labels:
            return db == 'auth_db'
        return db == 'default'