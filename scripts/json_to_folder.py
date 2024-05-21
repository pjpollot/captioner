import os
import json

from argparse import ArgumentParser

from captioner.content_block import dict_to_content_block
from captioner.io import block_to_folder

def get_arguments(): 
    parser = ArgumentParser("Folder to json")
    parser.add_argument(
        "--input_file",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--target_folder",
        type=str,
        default=os.path.join(os.path.dirname(__file__), "../cache"),
    )
    parser.add_argument(
        "--extensions",
        nargs="+",
        type=str,
        default=["jpg", "jpeg", "png", "webp"],
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = get_arguments()
    with open(args.input_file, "r") as f:
        data = json.load(f)
    block = dict_to_content_block(data)
    os.makedirs(args.target_folder, exist_ok=True)
    block_to_folder(block, args.target_folder)


