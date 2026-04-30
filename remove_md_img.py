"""
去除指定 Markdown 文件中的所有图片
"""
import re
import os
import argparse

def remove_images_from_md(input_path, output_path=None):
    """
    去除指定 Markdown 文件中的所有图片语法 ![](...)
    """
    # 如果没有指定输出路径，则在原文件名后加上 _no_imgs
    if not output_path:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_no_imgs{ext}"

    try:
        # 读取文件内容
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 正则表达式匹配 Markdown 图片格式：![任意文字](任意链接)
        # 解释：
        # !\[    匹配 "!["
        # .*?    非贪婪匹配替代文本 (alt text)
        # \]     匹配 "]"
        # \(     匹配 "("
        # .*?    非贪婪匹配图片链接
        # \)     匹配 ")"
        pattern = r'!\[.*?\]\(.*?\)'
        
        # 将匹配到的图片语法替换为空字符串
        cleaned_content = re.sub(pattern, '', content)

        # 写入新文件
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)

        print(f"✅ 成功！已去除图片，新文件保存至: {output_path}")

    except FileNotFoundError:
        print(f"❌ 错误：找不到文件 '{input_path}'，请检查路径是否正确。")
    except Exception as e:
        print(f"❌ 发生未知错误: {e}")

if __name__ == "__main__":
    # 设置命令行参数解析，方便在终端直接使用
    parser = argparse.ArgumentParser(description="一键去除 Markdown 文件中的所有图片")
    parser.add_argument("input_file", help="要处理的 Markdown 文件路径")
    parser.add_argument("-o", "--output_file", help="输出的文件路径（可选）", default=None)
    
    args = parser.parse_args()
    
    remove_images_from_md(args.input_file, args.output_file)