import os
from api import create_app


# creating flask app, routing and database configs
app = create_app()

if __name__ == "__main__":
    print(f'starting sever in {os.getenv("DEFAULT_PORT")}',)
    app.run(host='localhost', port=os.getenv("DEFAULT_PORT"), debug=True)
