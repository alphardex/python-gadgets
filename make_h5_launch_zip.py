"""
制作H5上线压缩包
"""
from pathlib import Path
import shutil

launch_path = Path('./线上')
template_path = launch_path / 'template'
html_files = list(Path('.').glob('*.html'))
shutil.rmtree(launch_path, ignore_errors=True)
shutil.copytree('css', launch_path / 'css')
shutil.copytree('js', launch_path / 'js')
shutil.copytree('images', launch_path / 'images')
template_path.mkdir()
[shutil.copy(html_file, template_path) for html_file in html_files]
html_filenames = [str(html_file) for html_file in html_files]
replaced_html_filenames = [html_filename.replace(
    'index.html', 'main.html') if html_filename == 'index.html' else html_filename for html_filename in html_filenames]
renamed_html_filenames = [
    f"{name.split('.')[0]}.{name.split('.')[1][:-1]}" for name in replaced_html_filenames]
[(template_path / origin_name).rename((template_path / renamed_name))
 for origin_name, renamed_name in zip(html_filenames, renamed_html_filenames)]
shutil.make_archive('线上', 'zip', launch_path)
shutil.rmtree(launch_path, ignore_errors=True)
