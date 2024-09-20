from django.shortcuts import render
import mysql.connector

def your_view(request):
    # データベースへの接続情報
    config = {
        'user': 'ユーザー名',         # MySQLのユーザー名
        'password': 'パスワード',     # MySQLのパスワード
        'host': 'localhost',
        'database': 'crm_db'         # 使用するデータベース名
    }

    # 接続を作成
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # ここでクエリを実行するコードを書く
    
    # 接続確認
    if conn.is_connected():
        print("接続成功")
    else:
        print("接続失敗")

    # 接続を閉じる
    cursor.close()
    conn.close()

    return render(request, 'your_template.html')  # レンダリングするテンプレートを指定

