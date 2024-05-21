"""Content block definition
"""

class ContentBlock:
    def __init__(self, name: str, content: str):
        self._name = name
        self._content = content
        self._child_blocks: list[ContentBlock] = []

    def add_child_blocks(self, *content_blocks) -> None:
        for i, content_block in enumerate(content_blocks):
            if isinstance(content_block, ContentBlock):
                self._child_blocks.append(content_block)
            else:
                raise ValueError(f"Children number {i} must be a content block in order to be added.")

    def to_dict(self) -> dict:
        data = {
            "name": self._name,
            "content": self._content,
            "children": [],
        }
        for child_block in self._child_blocks:
            child_data = child_block.to_dict()
            data["children"].append(child_data)
        return data
    
    def _captionning(self, prefix: str = "") -> list[tuple[str, str]]:
        content = self._content if prefix == "" else prefix + ", " + self._content
        if len(self._child_blocks) == 0:
            return [(self._name, content)]
        captions = []
        for child_block in self._child_blocks:
            captions += child_block._captionning(prefix=content)
        return captions
    
    def to_captions(self) -> dict[str, str]:
        caption_list = self._captionning()
        caption_dict = {}
        for name, caption in caption_list:
            caption_dict[name] = caption
        return caption_dict
    
    def get_child_blocks(self) -> list:
        return self._child_blocks.copy()

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, alternative_name: str) -> None:
        self._name = alternative_name
    
    @property
    def content(self) -> str:
        return self._content
    
    @content.setter
    def content(self, alternative_content: str) -> None:
        self._content = alternative_content


def dict_to_content_block(data: dict) -> ContentBlock:
    content_block = ContentBlock(
        name=data["name"],
        content=data["content"],
    )
    for child_data in data["children"]:
        child_content_block = dict_to_content_block(child_data)
        content_block.add_child_blocks(child_content_block)
    return content_block