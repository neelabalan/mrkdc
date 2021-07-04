import click
import markdown as md
from bottle import static_file, route, run


header = '''
<head>
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@11.0.1/styles/a11y-light.min.css">
    <script src="https://unpkg.com/@highlightjs/cdn-assets@11.0.1/highlight.min.js"></script>

    <script>hljs.highlightAll();</script>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/neelabalan/github-markdown-css@main/github-markdown.css">

    <style>
        .markdown-body {
            box-sizing: border-box;
            min-width: 200px;
            max-width: 980px;
            margin: 0 auto;
            padding: 45px;
        }

        @media (max-width: 767px) {
            .markdown-body {
                padding: 15px;
            }
        }
    </style>
</head>
<article class="markdown-body">
'''


def run_conversion_to_html(mdfile, output):
    with open(mdfile, "r", encoding='utf-8') as input_file:
        html = md.markdown(
            input_file.read(),
            extensions = ['fenced_code', 'tasklist', 'markdown_katex', 'tables']
        )
    with open(output, 'w', encoding='utf-8') as output_file:
        output_file.write(
            ''.join('<html>' + header + html + '\n</html>')
        )


def serve_static(mdfile):
    @route('/')
    def html():
        run_conversion_to_html(mdfile, 'temp.html')
        return static_file('temp.html', root='.')


@click.command()
@click.argument('mdfile', type=click.Path(exists=True))
@click.option('-o', '--output', type=str)
@click.option('-b', '--browser', is_flag=True, type=bool)
def main(mdfile, output, browser):
    if browser:
        try:
            serve_static(mdfile)
            run(reloader=True, debug=False)
        except KeyboardInterrupt:
            pass #cleanup temp
    else:
        if not output:
            raise Exception('Output filename needs to be provided')
        run_conversion_to_html(mdfile, output)


if __name__ == '__main__':
    main()
