# mrkdc 
> gh flavored markdown converter

This is a simple python script (could've been bash script but let's not go there) to convert Github falvored markdown to HTML.
The `markdown` package with some extensions, is used for conversion to HTML and then the `header` is added 
to the top of converted HTML for styling and this includes syntax highlighting.

> header
```html
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
```
## what does it look like?
> for some reason the syntax highlighting doesn't seem to work in `htmlpreview.github.io`

[Converted HTML](http://htmlpreview.github.io/?https://raw.githubusercontent.com/neelabalan/mrkdc/master/sample/output.html) from [sample](https://github.com/neelabalan/mrkdc/tree/master/sample) directory

## how to run?

```
python3 mrkdc.py file.md -o output.html

or 

python3 mrkdc.py file.md --browser
```


## dependencies

- [markdown](https://github.com/Python-Markdown/markdown) for markdown to HTML conversion
- [markdown-katex](https://github.com/mbarkhau/markdown-katex) for math support
- [tasklist](https://github.com/facelessuser/pymdown-extensions) for `- [ ]` kinda task list
- [click](https://github.com/pallets/click/) for arg parsing
- [github markdown css](https://github.com/sindresorhus/github-markdown-css) (`monospace` font)
- [highlightjs](https://github.com/highlightjs/highlight.js/) for syntax highlighting
- [bottle](https://github.com/bottlepy/bottle) for rendering html on browser
> will require to referesh the browser after every save



## why not use pandoc?

Pandoc is a beast. I am not going to be using most of the functionality it offers and I don't want to install 
all packages to just convert markdown to html. 

