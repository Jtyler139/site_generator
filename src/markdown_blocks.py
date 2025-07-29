def markdown_to_blocks(markdown):
    new_blocks = []
    blocks = markdown.split('\n\n')
    for block in blocks:
        block = block.strip()
        if block != '':
            new_blocks.append(block)
    return new_blocks
    