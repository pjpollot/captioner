from captioner.content_block import ContentBlock, dict_to_content_block

def test_blocks():
    # block definition
    block = ContentBlock(
        name="root",
        content="1boy, white_background",
    )
    sweater_image = ContentBlock(
        name="sweater.png",
        content="sweater, turtleneck",
    )
    costume_category = ContentBlock(
        name="costume",
        content="white_shirt, black_jacket, necktie"
    )
    hat_image = ContentBlock(
        name="hat.png",
        content="hat"
    )
    cane_image = ContentBlock(
        name="cane.png",
        content="cane",
    )
    costume_category.add_child_blocks(hat_image, cane_image)
    block.add_child_blocks(sweater_image, costume_category)
    # expected captions
    expected_captions = {
        "sweater.png": "1boy, white_background, sweater, turtleneck",
        "hat.png": "1boy, white_background, white_shirt, black_jacket, necktie, hat",
        "cane.png": "1boy, white_background, white_shirt, black_jacket, necktie, cane",
    }
    captions = block.to_captions()
    for name, caption in captions.items():
        assert expected_captions[name] == caption


def test_blocks_from_dict():
    # dict definition
    data = {
        "name": "root",
        "content": "",
        "children": [
            {
                "name": "rainy",
                "content": "clouds, rain",
                "children": [
                    {
                        "name": "rainy_night.png",
                        "content": "nighttime",
                        "children": [],
                    },
                    {
                        "name": "rainy_day.webp",
                        "content": "daytime",
                        "children": [],
                    },
                ],
            },
            {
                "name": "blue_sky.jpg",
                "content": "blue_sky, no_clouds",
                "children": [],
            },
        ]
    }
    captions = dict_to_content_block(data).to_captions()
    # expected captions
    expected_captions = {
        "rainy_night.png": "clouds, rain, nighttime",
        "rainy_day.webp": "clouds, rain, daytime", 
        "blue_sky.jpg": "blue_sky, no_clouds",
    }
    for name, caption in captions.items():
        assert expected_captions[name] == caption