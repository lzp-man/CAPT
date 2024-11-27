import argparse
import os

def split_jsonl(file_path, num_splits=4, output_dir='results'):
    try:
        # 打开原始文件
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except Exception as e:
        print(f"read file error: {e}")
        return

    # 计算每个分割文件应包含的行数
    split_size = len(lines) // num_splits

    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 获取文件名，不包括扩展名
    base_name = os.path.basename(file_path).rsplit('.', 1)[0]
    
    # 创建并写入分割文件
    for i in range(num_splits):
        part_path = os.path.join(output_dir, f'{base_name}_part{i + 1}.jsonl')
        try:
            with open(part_path, 'w', encoding='utf-8') as split_file:
                # 写入对应的行
                split_file.writelines(lines[i * split_size: (i + 1) * split_size if i < num_splits - 1 else len(lines)])

        except Exception as e:
            print(f"write error: {e}")

def main():
    parser = argparse.ArgumentParser(description="split")
    parser.add_argument("--file_path", type=str, required=True, help="file path")
    parser.add_argument("--num_splits", type=int, default=4, help="num to split")
    parser.add_argument("--output_dir", type=str, default='results', help="output dir")
    args = parser.parse_args()

    split_jsonl(args.file_path, args.num_splits, args.output_dir)

if __name__ == "__main__":
    main()
