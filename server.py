import argparse
import os

from config import connex_app
from exercise.builder import generate_ex


def get_args():
    ap = argparse.ArgumentParser('Process human language sentences into JSON.')

    # Add args
    ap.add_argument('-p', '--port', type=int,
                    help="Port number to run this service on.",
                    default=5011)

    ap.add_argument('-d', '--dummydata',
                    help="Initialize the database with dummy data.")

    a = ap.parse_args()

    return a


if __name__ == "__main__":
    args = get_args()

    if args.dummydata:
        filename = os.path.abspath(os.path.join(os.getcwd(), 'die_stopfnadel.txt'))
        generate_ex(filename, 'Die Stopfnadel', 'H. C. Andersen')

    connex_app.run(debug=True, port=args.port)

