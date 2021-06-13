import markdown as md
extensions = ['fenced_code', 'tasklist', 'markdown_katex', 'tables']
md.markdownFromFile(
    input='file.md',
    extensions=extensions,
    output='output.html',
    encoding='utf8',
)
