"""
分析codepen上你所收藏的pen的排名
"""
import json
from pathlib import Path
import looter as lt

encoding = 'utf-8'
total = []


def parse_json(path: Path):
    data = json.loads(path.read_text(encoding=encoding))
    pens = data[0]['data']['pens']['pens']
    results = []
    for pen in pens:
        result = {
            'title': pen['title'],
            'user': pen['owner']['username'],
            'url': pen['url'],
            'updatedAt': pen['updatedAt'],
            'comments': pen['counts']['comments'],
            'loves': pen['counts']['loves'],
            'views': pen['counts']['views']
        }
        results.append(result)
    return results


if __name__ == "__main__":
    for path in Path('.').glob('*.json'):
        total.extend(parse_json(path))
    lt.save(total, name='codepen_loved.csv', sort_by='loves', order='desc', no_duplicate=True)
