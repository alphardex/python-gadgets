"""
使用 requests 库实现类似 wget -i 的功能，自动处理重名文件
"""

import sys
import os
import requests
from urllib.parse import urlparse, unquote

def get_filename(url, response):
    """从 URL 或响应头提取文件名"""
    # 优先从 Content-Disposition 头获取
    cd = response.headers.get("Content-Disposition")
    if cd:
        for part in cd.split(";"):
            if "filename=" in part:
                fname = part.split("=")[1].strip().strip('"')
                return fname
    
    # 从 URL 路径提取
    path = urlparse(url).path
    filename = unquote(os.path.basename(path))
    return filename or "index.html"

def resolve_path(filepath):
    """处理文件重名，返回不冲突的文件路径"""
    if not os.path.exists(filepath):
        return filepath
    
    # 拆分文件名和扩展名
    dir_path = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)
    
    # 尝试添加序号
    counter = 1
    while True:
        new_name = f"{name}_{counter}{ext}"
        new_path = os.path.join(dir_path, new_name)
        if not os.path.exists(new_path):
            print(f"  ⚠ 文件已存在，重命名为: {new_name}")
            return new_path
        counter += 1

def download_file(url, output_dir, session):
    """下载单个文件，带进度条"""
    try:
        # 发起请求，流式下载
        response = session.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        # 获取文件名并处理重名
        filename = get_filename(url, response)
        filepath = os.path.join(output_dir, filename)
        filepath = resolve_path(filepath)
        
        # 获取文件大小
        total_size = int(response.headers.get("Content-Length", 0))
        downloaded = 0
        
        print(f"正在下载: {url}")
        if total_size:
            print(f"  -> {os.path.basename(filepath)} ({total_size/1024/1024:.1f} MB)")
        else:
            print(f"  -> {os.path.basename(filepath)}")
        
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    
                    # 显示进度条
                    if total_size > 0:
                        percent = downloaded / total_size * 100
                        bar_len = 40
                        filled = int(bar_len * downloaded / total_size)
                        bar = "█" * filled + "░" * (bar_len - filled)
                        print(f"\r  [{bar}] {percent:.1f}%", end="", flush=True)
        
        print(f"\r✓ 完成: {os.path.basename(filepath)}" + " " * 40)
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"\r✗ 下载失败: {e}" + " " * 40)
        return False
    except Exception as e:
        print(f"\r✗ 错误: {e}" + " " * 40)
        return False

def main():
    if len(sys.argv) < 2:
        print("用法: python wget_i.py <url文件> [输出目录]")
        print("示例: python wget_i.py urls.txt ./downloads")
        sys.exit(1)
    
    url_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    
    if not os.path.isfile(url_file):
        print(f"错误: 文件不存在 - {url_file}", file=sys.stderr)
        sys.exit(1)
    
    os.makedirs(output_dir, exist_ok=True)
    
    # 读取 URL 列表
    with open(url_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    
    if not urls:
        print("警告: 未找到有效 URL", file=sys.stderr)
        sys.exit(0)
    
    print(f"共找到 {len(urls)} 个 URL，开始下载...\n")
    
    # 使用会话保持连接
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (compatible; Python-downloader/1.0)"
    })
    
    success = 0
    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}]", end=" ")
        if download_file(url, output_dir, session):
            success += 1
        print()
    
    print(f"\n{'='*50}")
    print(f"完成: {success}/{len(urls)} 个文件下载成功")
    print(f"保存位置: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    main()