import os
from config import connex_app as application
from server import get_args
import config

activate_this = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'venv', 'bin', 'activate_this.py')

if __name__ == "__main__":
    args = get_args()
    config.text_files_dir = args.text_files_dir

    with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))

    application.run(debug=args.debug, port=args.port)

