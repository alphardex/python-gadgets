"""
批量视频压缩
"""
import subprocess
import os
import time

def batch_extract_audio(input_dir, output_dir):
    # 支持的视频后缀
    video_extensions = ('.mp4', '.mkv', '.avi', '.flv', '.mov', '.wmv')
    
    # 如果输出文件夹不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 获取目录下所有视频文件
    video_files = [f for f in os.listdir(input_dir) if f.lower().endswith(video_extensions)]
    
    if not video_files:
        print("文件夹内没找到视频文件哦！")
        return

    print(f"找到 {len(video_files)} 个视频，准备开始‘脱水’提取音频...")
    start_time = time.time()

    for video_name in video_files:
        video_path = os.path.join(input_dir, video_name)
        # 生成音频文件名 (原文件名.mp3)
        audio_name = os.path.splitext(video_name)[0] + ".mp3"
        audio_path = os.path.join(output_dir, audio_name)

        print(f"正在处理: {video_name} ...")
        
        # FFmpeg 命令解释:
        # -i: 输入文件
        # -vn: 禁用视频（只取音频）
        # -acodec libmp3lame: 使用 mp3 编码器
        # -q:a 4: 使用动态码率 (VBR)，质量等级 4（约 160kbps），兼顾体积和清晰度
        # -y: 覆盖已存在文件
        cmd = [
            'ffmpeg',
            '-i', video_path,
            '-vn',
            '-acodec', 'libmp3lame',
            '-q:a', '4',
            audio_path,
            '-y'
        ]

        try:
            # 执行命令并隐藏输出窗口（如果想看进度可以去掉 stdout 和 stderr 参数）
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"✅ 完成: {audio_name}")
        except subprocess.CalledProcessError as e:
            print(f"❌ 失败: {video_name}, 错误信息: {e}")

    end_time = time.time()
    print(f"\n全部搞定！总耗时: {int(end_time - start_time)} 秒")
    print(f"音频文件保存在: {output_dir}")

if __name__ == "__main__":
    # --- 你只需要改这里 ---
    INPUT_FOLDER = r'D:\Code\python-gadgets'  # 视频所在的文件夹路径
    OUTPUT_FOLDER = r'D:\Code\python-gadgets' # 提取出的音频存放路径
    # ---------------------
    
    batch_extract_audio(INPUT_FOLDER, OUTPUT_FOLDER)