def get_style(style_string):
    style_string = style_string.replace('ParagraphStyle/', '')
    style_string = style_string.replace('CharacterStyle/', '')
    style_string = style_string.replace('$ID/', '')
    return style_string
