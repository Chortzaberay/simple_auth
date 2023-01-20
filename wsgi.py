from src import create_app
from config import DevConfig, ProductConfig

app = create_app(DevConfig)

if __name__ == "__main__":
    app.run(debug=True)

