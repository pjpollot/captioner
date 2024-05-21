import json

from argparse import ArgumentParser

from captioner.io import folder_to_block

def get_arguments(): 
    parser = ArgumentParser("Folder to json")
    parser.add_argument(
        "--root_folder",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--output_file",
        type=str,
        required=False,
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
    block = folder_to_block(args.root_folder, tuple(args.extensions))
    data = block.to_dict()
    with open(args.output_file, "w") as f:
        json.dump(data, f, indent=4)


