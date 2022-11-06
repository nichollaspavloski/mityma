from api.server import create_app

app = create_app()

if __name__ == "__main__":
    print("starting sever in 8080")
    app.run(host='172.18.0.1', port=8080, debug=True)
