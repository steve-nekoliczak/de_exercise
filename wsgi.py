import os

import config
from args import get_args

app = config.connex_app


if __name__ == "__main__":
    args = get_args()
    config.text_files_dir = args.text_files_dir
    app.run(debug=args.debug, port=args.port)
