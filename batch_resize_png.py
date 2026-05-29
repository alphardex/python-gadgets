"""
批量将目录中的所有PNG图片缩小一定倍数
"""

import os
import sys
from pathlib import Path
from PIL import Image


def resize_images(input_dir, output_dir=None, scale_factor=0.5):
    """
    批量缩小目录中的PNG图片
    
    Args:
        input_dir: 输入目录路径
        output_dir: 输出目录路径（如果为None，则在原目录创建resized子目录）
        scale_factor: 缩放比例（默认0.5即缩小2倍）
    """
    input_path = Path(input_dir)
    
    # 检查输入目录是否存在
    if not input_path.exists():
        print(f"错误：目录 '{input_dir}' 不存在")
        return
    
    # 设置输出目录
    if output_dir is None:
        output_path = input_path / "resized"
    else:
        output_path = Path(output_dir)
    
    # 创建输出目录
    output_path.mkdir(parents=True, exist_ok=True)
    
    # 获取所有PNG文件
    png_files = list(input_path.glob("*.png")) + list(input_path.glob("*.PNG"))
    
    if not png_files:
        print(f"在目录 '{input_dir}' 中没有找到PNG图片")
        return
    
    print(f"找到 {len(png_files)} 个PNG图片")
    print(f"输出目录: {output_path}")
    print("-" * 50)
    
    success_count = 0
    error_count = 0
    
    for png_file in png_files:
        try:
            # 打开图片
            with Image.open(png_file) as img:
                # 获取原始尺寸
                original_size = img.size
                
                # 计算新尺寸
                new_width = int(img.width * scale_factor)
                new_height = int(img.height * scale_factor)
                new_size = (new_width, new_height)
                
                # 缩小图片（使用高质量重采样）
                resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
                
                # 保存到输出目录
                output_file = output_path / png_file.name
                resized_img.save(output_file, "PNG", optimize=True)
                
                print(f"✓ {png_file.name}: {original_size} -> {new_size}")
                success_count += 1
                
        except Exception as e:
            print(f"✗ 处理 {png_file.name} 时出错: {e}")
            error_count += 1
    
    # 输出统计信息
    print("-" * 50)
    print(f"处理完成！成功: {success_count}, 失败: {error_count}")


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="批量将目录中的PNG图片缩小2倍",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  python resize_png.py ./images                    # 缩小当前images目录的所有PNG
  python resize_png.py ./images -o ./output        # 输出到指定目录
  python resize_png.py ./images -s 0.3             # 缩小到原来的30%
        """
    )
    
    parser.add_argument(
        "input_dir",
        help="输入目录路径"
    )
    
    parser.add_argument(
        "-o", "--output",
        dest="output_dir",
        help="输出目录路径（默认为输入目录下的resized文件夹）"
    )
    
    parser.add_argument(
        "-s", "--scale",
        dest="scale_factor",
        type=float,
        default=0.5,
        help="缩放比例（默认0.5即缩小2倍，0-1之间）"
    )
    
    args = parser.parse_args()
    
    # 验证缩放比例
    if args.scale_factor <= 0 or args.scale_factor > 1:
        print("错误：缩放比例必须在0到1之间")
        sys.exit(1)
    
    # 执行缩放
    resize_images(args.input_dir, args.output_dir, args.scale_factor)


if __name__ == "__main__":
    # 如果直接运行脚本，使用当前目录
    if len(sys.argv) == 1:
        print("用法: python resize_png.py <目录路径> [-o 输出目录] [-s 缩放比例]")
        print("示例: python resize_png.py ./images")
        print("      python resize_png.py ./images -o ./output -s 0.5")
        sys.exit(1)
    
    main()