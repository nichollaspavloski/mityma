import os
from api.server import create_app

app = create_app()

if __name__ == "__main__":
    print(f'starting sever in {os.getenv("DEFAULT_PORT")}',)
    app.run(host='172.18.0.1', port=os.getenv("DEFAULT_PORT"), debug=True)
