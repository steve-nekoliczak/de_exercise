import argparse
import os

import config
from exercise.builder import generate_ex


def get_args():
    ap = argparse.ArgumentParser('Create exercises from German text.')

    # Add args
    ap.add_argument('-d', '--debug',
                    action='store_true',
                    help="Enable debugging mode.")

    ap.add_argument('-p', '--port', type=int,
                    help="Port number to run this service on.",
                    default=5011)

    ap.add_argument('-t', '--text-files-dir',
                    help="Directory to store uploaded text files.",
                    default=config.text_files_dir)

    a = ap.parse_args()

    return a


if __name__ == "__main__":
    args = get_args()

    config.text_files_dir = args.text_files_dir

    config.connex_app.run(debug=args.debug, port=args.port)

