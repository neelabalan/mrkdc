import click
import markdown as md

header = '''
<head>
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@11.0.1/styles/a11y-light.min.css">
    <script src="https://unpkg.com/@highlightjs/cdn-assets@11.0.1/highlight.min.js"></script>

    <script>hljs.highlightAll();</script>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="github-markdown.css">

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

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.13.6/dist/katex.min.css"
        integrity="sha384-81hI3kRV62VEhJBKVz7JsJzaUcP5Ty/E1FFdkLh6yz8uWthgdssaWCD1j8R1r2iU" crossorigin="anonymous" />

    <style type="text/css">
        .katex img {
            display: block;
            position: absolute;
            width: 100%;
            height: inherit;
        }
    </style>
</head>
<article class="markdown-body">
'''


def run_conversion_to_html(mdfile, output):
    with open(mdfile, "r", encoding='utf-8') as input_file:
        text = input_file.read()
        html = md.markdown(text)
    with open(output, 'w', encoding='utf-8') as output_file:
        output_file.write(
            ''.join('<html>' + header + html + '\n</html>')
        )


@click.command()
@click.argument('mdfile', type=click.Path(exists=True))
@click.option('-o', '--output', required=False, type=str)
def main(mdfile, output):
    run_conversion_to_html(mdfile, output)

if __name__ == '__main__':
    main()
