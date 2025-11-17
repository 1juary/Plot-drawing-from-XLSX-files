import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_value_distribution_from_excel(file_path, sheet_name, value_col, bins=10,
                                       title="数值分布直方图", xlabel="数值区间", ylabel="样本量"):
    """
    从Excel文件中读取数据并绘制数值分布直方图

    参数:
        file_path (str): Excel文件路径
        sheet_name (str): 工作表名称
        value_col (str/int): 要分析的列名或列索引（从0开始）
        bins (int/sequence): 区间数量或自定义区间边界
        title (str): 图表标题
        xlabel (str): X轴标签
        ylabel (str): Y轴标签
    """
    # 使用pandas读取Excel数据
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # 提取指定列数据
    values = df.iloc[:, value_col] if isinstance(value_col, int) else df[value_col]

    # 计算数值分布
    counts, bin_edges = np.histogram(values, bins=bins)

    # 生成区间标签
    bin_labels = [f"{bin_edges[i]:.1f}-{bin_edges[i + 1]:.1f}" for i in range(len(bin_edges) - 1)]

    # 绘制柱状图
    plt.figure(figsize=(10, 6))
    bars = plt.bar(bin_labels, counts, color='skyblue')

    # 添加数值标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height,
                 f'{int(height)}',
                 ha='center', va='bottom')

    # 图表装饰
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # 显示图表
    plt.show()


# 示例用法
if __name__ == "__main__":
    # 文件路径 (替换为你的Excel文件路径)
    excel_file = "example.xlsx"

    # 参数设置
    sheet = "Sheet1"  # 工作表名
    value_column = "年龄"  # 或列索引 (如 0 表示第一列)

    # 绘制图表
    plot_value_distribution_from_excel(
        file_path=excel_file,
        sheet_name=sheet,
        value_col=value_column,
        bins=5,  # 可以设置为整数或自定义区间边界如 [0, 20, 40, 60, 80, 100]
        title="年龄分布直方图",
        xlabel="年龄区间",
        ylabel="人数"
    )