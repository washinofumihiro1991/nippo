# -*- coding: utf-8 -*-
from .models import Report, Comment
from django.contrib.auth.models import User
from django.test.client import Client
from django.db.models import Q
from django.test import TestCase, RequestFactory


# ユーザの作成
def create_user(self, username, password):
    return User.objects.create_user(username=username, email=None, password=password)


# 日報の作成
def create_report(self, title, content, user, time):
    return Report.objects.create(title=title, content_Y=content, user=user, user_post_time=time)


# 日報の削除
def delete_report(self, report_id):
    Report.objects.get(id=report_id).delete()


# 日報に対してのコメントの作成
def create_comment(self, report, comment, comment_user, comment_time):
    return Comment.objects.create(report=report, comment=comment, comment_user=comment_user,
                                     comment_time=comment_time)


# コメントの削除
def delete_comment(self, comment_id):
    Report.objects.get(id=comment_id).delete()


#  ユーザの作成とログイン関係のテスト
class UserTest(TestCase):
    @classmethod
    def setUpClass(cls):
        # print("setupclass")
        cls.user_id = ['Terry', 'Dai', 'Allen']
        cls.no_user_id = ""
        cls.password = cls.user_id
        cls.no_password = ""
        cls.error_password = "error_password"

    @classmethod
    def tearDownClass(cls):
        print("Success test")

    def test_make_user(self):
        # ユーザの作成と呼び出し
        user_1 = create_user(self, self.user_id[0], self.password[0])
        user_2 = create_user(self, self.user_id[1], self.no_password)

        # 作成したユーザのIDとパスワードが一致しているか確認
        # ID、パスワード共に入力されたとき
        self.assertEquals(user_1.username, self.user_id[0])
        self.assertTrue(user_1.check_password(self.password[0]))

        # IDは入力され、パスワードが入力されなかったとき
        self.assertEquals(user_2.username, self.user_id[1])
        self.assertTrue(user_2.check_password(self.no_password))

    def test_not_make_user(self):
        # ユーザが作成できないことを確認
        self.assertRaises(ValueError, lambda: User.objects.create_user(self.no_user_id, None, self.no_password))

        # 作成したユーザがログインできるかどうか

    def test_login(self):
        # ユーザを作成
        create_user(self, self.user_id[0], self.password[0])

        # 作成したユーザでログインできるかを確認
        client_user = Client()
        self.assertTrue(client_user.login(username=self.user_id[0], password=self.password[0]))

        # 異なるID、パスワードでログインできないかどうか

    def test_not_login(self):
        # ユーザを作成
        create_user(self, self.user_id[0], self.password[0])

        # 作成したユーザに異なるパスワードでログインできないかを確認
        client_user = Client()
        self.assertFalse(client_user.login(username=self.user_id[0], password=self.error_password))


# 日報作成や削除、編集のテスト
class ReportTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.title = ['report', 'test', 'daily']
        cls.content = ['content', 'text', 'plan']
        cls.user = ['Terry', 'Dai', 'Allen']
        cls.time = ['2006-04-01 12:34:56', '2010-12-25 00:00:00', '2016-08-24 15:43:06']

    @classmethod
    def tearDownClass(cls):
        print("Success test")

    # データベースの初期状態の確認(何も入力されていないか確認)
    def test_init_database(self):
        saved_report = Report.objects.all()
        self.assertEquals(saved_report.count(), 0)

    # 日報の各項目の入力、編集、削除をきるか確認
    def test_report_add(self):
        # 各データの入力と呼び出し
        report = create_report(self, self.title[0], self.content[0], self.user[0], self.time[0])

        # 各データが一致しているかを確認
        self.assertEquals(report.title, self.title[0])
        self.assertEquals(report.content_Y, self.content[0])
        self.assertEquals(report.user, self.user[0])
        self.assertEquals(report.user_post_time, self.time[0])

        # 日報の編集
        report.title = self.title[1]
        report.content_Y = self.content[1]
        report.user = self.user[1]
        report.user_post_time = self.time[1]

        self.assertEquals(report.title, self.title[1])
        self.assertEquals(report.content_Y, self.content[1])
        self.assertEquals(report.user, self.user[1])
        self.assertEquals(report.user_post_time, self.time[1])

        # 日報の削除
        report_id = report.id
        # print(report_id)
        report = delete_report(self, report_id)

        # 各データが削除されているかを確認
        # self.assertRaises(ValueError, lambda: User.objects.create_user(self.no_user_id, None, self.no_password))
        self.assertRaises(AttributeError, lambda: report.title)
        self.assertRaises(AttributeError, lambda: report.content_Y)
        self.assertRaises(AttributeError, lambda: report.user)
        self.assertRaises(AttributeError, lambda: report.time)
        self.assertEquals(report, None)


# コメントのテスト
class CommentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.title = ['report', 'test', 'daily']
        cls.content = ['content', 'text', 'plan']
        cls.user = ['Terry', 'Dai', 'Allen']
        cls.time = ['2006-04-01 12:34:56', '2010-12-25 00:00:00', '2016-08-24 15:43:06']

        cls.comment = ['Great', 'Good', 'Bad']
        cls.comment_user = ['Allen', 'Terry', 'Dai']
        cls.comment_time = ['2010-12-25 00:00:00', '2016-08-24 15:43:06', '2006-04-01 12:34:56']

    @classmethod
    def tearDownClass(cls):
        print("Success test")

    # コメントの入力、編集、削除できるかを確認
    def test_immpression_add(self):
        report = create_report(self, self.title[0], self.content[0], self.user[0], self.time[0])
        comment = create_comment(self, report, self.comment[0], self.comment_user[0], self.comment_time[0])

        # 各日報にコメントが入力されているかを確認
        self.assertEquals(comment.comment, self.comment[0])
        self.assertEquals(comment.comment_user, self.comment_user[0])
        self.assertEquals(comment.comment_time, self.comment_time[0])

        # コメントの編集
        comment.comment = self.comment[1]
        comment.comment_user = self.comment_user[1]
        comment.comment_time = self.comment_time[1]

        # 編集されているかを確認
        self.assertEquals(comment.comment, self.comment[1])
        self.assertEquals(comment.comment_user, self.comment_user[1])
        self.assertEquals(comment.comment_time, self.comment_time[1])

        # コメントの削除
        report_id = report.id
        comment_id = Report.objects.all().prefetch_related("comments").get(id=report_id).comments.values()[0]['id']
        comment = delete_comment(self, comment_id)

        # 各データが削除されているかを確認
        self.assertRaises(AttributeError, lambda: comment.comment)
        self.assertRaises(AttributeError, lambda: comment.comment_user)
        self.assertRaises(AttributeError, lambda: comment.comment_time)
        self.assertEquals(comment, None)

#
# # 各URLに遷移できるかを確認
# class UrlAuthTest(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.user_id = ['Terry', 'Dai', 'Allen']
#         cls.no_user_id = ""
#         cls.password = cls.user_id
#         cls.no_password = ""
#         cls.error_password = "error_password"
#
#         cls.title = ['report', 'test', 'daily']
#         cls.content = ['content', 'text', 'plan']
#         cls.user = cls.user_id
#         cls.time = ['2006-04-01 12:34:56', '2010-12-25 00:00:00', '2016-08-24 15:43:06']
#
#         cls.comment = ['Great', 'Good', 'Bad']
#         cls.comment_user = ['Allen', 'Terry', 'Dai']
#         cls.comment_time = ['2010-12-25 00:00:00', '2016-08-24 15:43:06', '2006-04-01 12:34:56']
#
#         cls.transition_url = ['/report/', '/report/add/', '/report/search/',
#                               '/report/mod/', '/report/browse/',
#                               '/comment/', '/comment/add/',
#                               '/comment/mod/']
#         cls.url_followed_by_one = ['/report/mod/', '/report/browse/',
#                                    '/comment/', '/comment/add/']
#         cls.url_followed_by_two = ['/comment/mod/']
#         cls.redirect_request_url = ['/report/del/', '/comment/del/']
#         cls.redirect_response_url = ['/report/', '/comment/']
#
#     @classmethod
#     def tearDownClass(cls):
#         print("Success test")
#
#     # ログイン状態によるページへのアクセスの可否をテスト
#     def test_auth(self):
#         # ユーザの作成
#         create_user(self, self.user_id[0], self.password[0])
#         client_user = Client()
#         client_user.login(username=self.user_id[0], password=self.password[0])
#
#         # データベースを作成
#         report = create_report(self, self.title[0], self.content[0], self.user[0], self.time[0])
#         for i in range(1, len(self.title)):
#             create_report(self, self.title[i], self.content[i], self.user[i], self.time[i])
#
#         start_report_id = report.id
#         for i in range(len(self.comment)):
#             init_report = Report.objects.get(id=start_report_id + i)
#             comment = create_comment(self, init_report, self.comment[i], self.comment_user[i], self.comment_time[i])
#
#         comment_id = comment.id
#         end_report_id = init_report.id
#         # ページ遷移できているかを確認
#
#         for i in self.transition_url:
#             if i in self.url_followed_by_one:
#                 url = i + str(start_report_id) + '/'
#             elif i in self.url_followed_by_two:
#                 url = i + str(start_report_id) + '/' + str(comment_id) + '/'
#             else:
#                 url = i
#             response_data = client_user.get(url)
#             # print(url)
#             self.assertEqual(response_data.status_code, 200)
#
#         # リダイレクトできているかを確認
#         for i in range(len(self.redirect_request_url)):
#             if self.redirect_request_url[i] == '/report/del/':
#                 url = self.redirect_request_url[i] + str(start_report_id) + '/'
#                 redirect_url = self.redirect_response_url[i]
#             elif self.redirect_request_url[i] == '/comment/del/':
#                 url = self.redirect_request_url[i] + str(end_report_id) + '/' + str(comment_id) + '/'
#                 redirect_url = self.redirect_response_url[i] + str(end_report_id) + '/'
#             # print(url)
#             response_data = client_user.get(url)
#             self.assertRedirects(response_data, redirect_url)


# View.pyの各機能のテスト
class ViewsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        # print("setupclass")
        cls.user_id = ['Terry', 'Dai', 'Allen']
        cls.password = cls.user_id

        cls.title = ['report', 'test', 'daily']
        cls.content = ['content', 'text', 'plan']
        cls.user = cls.user_id
        cls.time = ['2006-04-01 12:34:56', '2010-12-25 00:00:00', '2016-08-24 15:43:06']

        cls.search_keyword = 'Terry'

    @classmethod
    def tearDownClass(cls):
        print("Success test")

    # 検索機能できるかどうかのテスト
    def test_search(self):
        # テストコード内の検索に使用するキーワード
        # keyword = 'Terry'

        # データベースを作成
        for i in range(len(self.title)):
            create_report(self, self.title[i], self.content[i], self.user[i], self.time[i])

        # 検索ページ(report_list.html)の呼び出し
        client_user = Client()
        response_data = client_user.post('/report/search/', {'Search': self.search_keyword})

        # 確認用
        # for  i in response_data.context['reports']:
        #     print(i.title, i.content_Y, i.user, i.user_post_time)

        # テストコード内でフィルターをかける
        # ほとんどviews.report_searchと同じ
        keyword = self.search_keyword.split()
        queries1 = [Q(user_post_time__icontains=word) for word in keyword]
        queries2 = [Q(user__icontains=word) for word in keyword]
        queries3 = [Q(title__icontains=word) for word in keyword]
        queries4 = [Q(content_Y__icontains=word) for word in keyword]
        query = queries1.pop(0)

        for item in queries1:
            query |= item
        for item in queries2:
            query |= item
        for item in queries3:
            query |= item
        for item in queries4:
            query |= item

        input_report = Report.objects.filter(query).order_by('id')

        # Searchクラスが正常に検索できているかをテスト
        for i, j in zip(response_data.context['reports'], input_report):
            self.assertEquals(i.title, j.title)
            self.assertEquals(i.content_Y, j.content_Y)
            self.assertEquals(i.user, j.user)
            self.assertEquals(i.user_post_time, j.user_post_time)
