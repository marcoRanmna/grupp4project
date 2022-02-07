# from website import create_app
#
# app = create_app()
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
from website import create_app
import dotenv


if __name__ == '__main__':
    dotenv.load_dotenv()
    create_app().run(debug=True)