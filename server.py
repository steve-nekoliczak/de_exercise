import argparse
import os

from config import connex_app, file_dir, text_files_dir
from exercise.builder import generate_ex


def get_args():
    ap = argparse.ArgumentParser('Process human language sentences into JSON.')

    # Add args
    ap.add_argument('-p', '--port', type=int,
                    help="Port number to run this service on.",
                    default=5011)

    ap.add_argument('-d', '--dummydata',
                    help="Initialize the database with dummy data.")

    ap.add_argument('-t', '--text-files-dir',
                    help="Directory to store uploaded text files.",
                    default=file_dir)

    a = ap.parse_args()

    return a


if __name__ == "__main__":
    args = get_args()

    text_files_dir = args.text_files_dir

    if args.dummydata:
        filename = os.path.abspath(os.path.join(os.getcwd(), 'die_stopfnadel.txt'))
        generate_ex(filename, 'Die Stopfnadel', 'H. C. Andersen')

    connex_app.run(debug=True, port=args.port)

