"""
自动生成CSS项目文件
"""
from pathlib import Path
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Document</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
  </body>
</html>
"""
CSS_TEMPLATE = """body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
"""
Path('index.html').write_text(HTML_TEMPLATE)
Path('style.scss').write_text(CSS_TEMPLATE)