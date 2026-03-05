def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file: 
           html = file.read()
    text = ''
    inside_tag = False

    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            text += char

    clean_lines = [line.strip() for line in text.split('\n') if line.strip()]
    result = '\n'.join(clean_lines)

    with open(result_file, 'w', encoding='utf-8') as f:
        f.write(result)


if __name__ == '__main__':
    delete_html_tags('draft.html')
