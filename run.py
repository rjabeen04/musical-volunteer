from app import create_app

app = create_app()
app.secret_key = 'super_secret_key'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
