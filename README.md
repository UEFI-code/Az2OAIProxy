# Azure to OpenAI Protocol Proxy

このプロジェクトは、AzureからのリクエストをOpenAIのAPIに転送するPython Flaskアプリケーションです。Azureからのリクエストを受け取り、それをOpenAIのAPIに転送します。これにより、ユーザーはAzureのプロトコルを使用してOpenAIの機能を利用することができます。

## 機能

- AzureからのリクエストをOpenAIのAPIに転送
- OpenAIのAPIからのレスポンスをAzureに返送

## セットアップ

1. 必要なライブラリをインストールします：

    ```bash
    pip install flask
    ```

2. `app.py`を実行します：

    ```bash
    python app.py
    ```

3. Nginxのリバースプロキシ設定：

    このプロジェクトはFlaskアプリケーションであり、本番環境で実行する場合は、通常、NginxなどのWebサーバーをリバースプロキシとして使用します。以下に、基本的なNginxの設定を示します：

    ```nginx
    server {
        listen 80;
        server_name your_domain_or_IP;

        location / {
            proxy_pass http://localhost:5000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
    ```

    この設定を適用するには、この設定を含むファイルをNginxの設定ディレクトリ（通常は/etc/nginx/sites-available/）に保存し、その後で/etc/nginx/sites-enabled/ディレクトリにシンボリックリンクを作成します。最後に、Nginxをリロードまたは再起動します。

    なお、`your_domain_or_IP`は適切なドメイン名またはIPアドレスに置き換えてください。

    もし、HTTPSを使用欲しい場合は、certbotを使用ください。

    ```bash
    sudo certbot --nginx
    ```

## 使用方法

POSTリクエストを`/chat/<model_name>`エンドポイントに送信します。リクエストヘッダーには`api-key`を含め、リクエストボディには`message`、`max_tokens`、`temperature`、`top_p`を含めます。

## 注意事項

このプロジェクトはデモンストレーション用であり、本番環境での使用は推奨されません。本番環境で使用する場合は、適切なエラーハンドリングとセキュリティ対策を行ってください。