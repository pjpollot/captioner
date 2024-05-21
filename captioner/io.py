import os

from warnings import warn
from shutil import copyfile

from .content_block import ContentBlock

def _read_caption(file_path: str) -> str:
    if os.path.isfile(file_path):
        with open(file_path, "r") as f:
            return f.read()
    else:
        warn(f"WARNING: {file_path} is not a file or have not been found. Then, no caption will be added.")
        return ""

def folder_to_block(
        root_folder_path: str, 
        authorized_file_extensions: tuple[str,...], 
) -> ContentBlock:
    content_file = os.path.join(root_folder_path, f"root.txt")
    block = ContentBlock(
        name=os.path.basename(root_folder_path),
        content=_read_caption(content_file),
    )
    for endpoint in os.listdir(root_folder_path):
        endpoint_path = os.path.join(root_folder_path, endpoint)
        if endpoint_path.lower().endswith(authorized_file_extensions):
            # if it is a file, we add just one children
            content_file = os.path.join(root_folder_path, f"{endpoint.split(".")[0]}.txt")
            content = _read_caption(content_file)
            block.add_child_blocks(ContentBlock(
                name=endpoint_path,
                content=content,
            ))
        elif os.path.isdir(endpoint_path):
            # if it is a folder, we proceed the reading recursively
            children = folder_to_block(endpoint_path, authorized_file_extensions)
            block.add_child_blocks(children)
    return block


def block_to_folder(block: ContentBlock, target_folder_path: str) -> None:
    if not os.path.isdir(target_folder_path):
        raise ValueError(f"{target_folder_path} is not a directory.")
    project_name = block.name
    root_path = os.path.join(target_folder_path, project_name)
    os.makedirs(root_path, exist_ok=True)
    captions = block.to_captions()
    for i, (file_path, caption) in enumerate(captions.items()):
        filename, file_extension = os.path.basename(file_path).split(".")
        new_filename = f"{project_name}_{i}"
        copyfile(file_path, os.path.join(root_path, f"{new_filename}.{file_extension}"))
        with open(os.path.join(root_path, f"{new_filename}.txt"), "w") as f:
            f.write(caption)
