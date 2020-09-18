# -*- coding: utf-8 -*-

from pyfs_auth import AppAccessToken, final_app_access_token


class Application(AppAccessToken):
    def __init__(self, appid=None, secret=None, ticket=None, token=None, storage=None):
        super(Application, self).__init__(appid=appid, secret=secret, ticket=ticket, token=token, storage=storage)
        # 校验应用管理员, Refer: https://open.feishu.cn/document/ukTMukTMukTM/uITN1EjLyUTNx4iM1UTM
        self.IS_USER_ADMIN = self.OPEN_DOMAIN + '/open-apis/application/v3/is_user_admin?open_id={open_id}&employee_id={employee_id}'

    def is_user_admin(self, open_id=None, employee_id=None, appid=None, secret=None, ticket=None, token=None, storage=None):
        token = final_app_access_token(self, appid=appid, secret=secret, ticket=ticket, token=token, storage=storage)
        return self.get(self.IS_USER_ADMIN, open_id=open_id or '', employee_id=employee_id or '', token=token)


application = Application()
is_user_admin = application.is_user_admin
