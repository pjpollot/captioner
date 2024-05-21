import os

from captioner.io import folder_to_block, block_to_folder

def test_io():
    example_folder_path = os.path.join(
        os.path.dirname(__file__),
        "../data_examples/animals",
    )
    block_1 = folder_to_block(example_folder_path, ("jpg"))
    assert len(block_1.to_captions()) == 6
    block_2 = folder_to_block(example_folder_path, ("jpg", "jpeg"))
    assert len(block_2.to_captions()) == 7
    cache_path = os.path.join(
        os.path.dirname(__file__),
        "../cache",
    )
    os.makedirs(cache_path, exist_ok=True)
    block_to_folder(block_2, cache_path)
    assert os.path.isdir(os.path.join(cache_path, block_2.name))

