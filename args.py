import argparse

from config import port, text_files_dir


def get_args():
    ap = argparse.ArgumentParser('Create exercises from German text.')

    # Add args
    ap.add_argument('-d', '--debug',
                    action='store_true',
                    help="Enable debugging mode.")

    ap.add_argument('-p', '--port', type=int,
                    help="Port number to run this service on.",
                    default=port)

    ap.add_argument('-t', '--text-files-dir',
                    help="Directory to store uploaded text files.",
                    default=text_files_dir)

    return ap.parse_args()
