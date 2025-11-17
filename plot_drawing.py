import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from faker import Faker  # 用于生成随机姓名

# 初始化Faker生成器
fake = Faker('zh_CN')


def generate_random_data(num_records=100):
    """生成包含随机年龄和姓名的DataFrame"""
    data = {
        '姓名': [fake.name() for _ in range(num_records)],
        '年龄': np.random.normal(loc=35, scale=10, size=num_records).astype(int)
    }
    # 确保年龄在合理范围内(0-100)
    data['年龄'] = np.clip(data['年龄'], 0, 100)
    return pd.DataFrame(data)


def plot_value_distribution_from_data(data,
                                      value_col,
                                      bins=10,
                                      title="Numerical Distribution Histogram",
                                      xlabel="Bin_edge",
                                      ylabel="Samples qty"):
    """
    从DataFrame中读取数据并绘制数值分布直方图

    参数:
        data (DataFrame): 包含数据的DataFrame
        value_col (str/int): 要分析的列名或列索引（从0开始）
        bins (int/sequence): 区间数量或自定义区间边界
        title (str): 图表标题
        xlabel (str): X轴标签
        ylabel (str): Y轴标签
    """
    # 提取指定列数据
    values = data.iloc[:, value_col] if isinstance(value_col, int) else data[value_col]

    # 计算数值分布
    counts, bin_edges = np.histogram(values, bins=bins)

    # 生成区间标签
    bin_labels = [f"{bin_edges[i]:.1f}-{bin_edges[i + 1]:.1f}" for i in range(len(bin_edges) - 1)]

    # 计算关键统计数据
    stats = {
        "Mean": np.mean(values),
        "Median": np.median(values),
        "STD": np.std(values),
        "Min": np.min(values),
        "Max": np.max(values),
        "Length": len(values),
        "Skew": pd.Series(values).skew(),
        "Kurt": pd.Series(values).kurt()
    }

    # 将统计信息格式化为字符串
    stats_text = "\n".join([f"{k}: {v:.2f}" if isinstance(v, (float, np.floating)) else f"{k}: {v}"
                            for k, v in stats.items()])

    # 绘制柱状图
    plt.figure(figsize=(12, 6))
    bars = plt.bar(bin_labels, counts, color='skyblue')

    # 添加数值标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.,
                 height,
                 f'{int(height)}',
                 ha='center',
                 va='bottom')

    # 在图表右侧添加统计信息
    plt.text(0.95, 0.95, stats_text,
             transform=plt.gca().transAxes,
             verticalalignment='top',
             horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

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
    # 生成随机数据
    random_data = generate_random_data(num_records=200)

    # 显示前5行数据
    print("生成的随机数据示例:")
    print(random_data.head())

    # 参数设置
    value_column = "年龄"  # 要分析的列名

    # 绘制图表
    plot_value_distribution_from_data(
        data=random_data,
        value_col=value_column,
        bins=5,  # 可以设置为整数或自定义区间边界如 [0, 20, 40, 60, 80, 100]
        title="Numerical Distribution Histogram",
        xlabel="Age",
        ylabel="Qty"
    )