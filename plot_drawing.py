import pandas as pd
import matplotlib.pyplot as plt


def plot_bar_chart_from_excel(file_path, sheet_name, x_col, y_col, title="柱状图", xlabel="X轴", ylabel="Y轴"):
    """
    从Excel文件中读取数据并绘制柱状图 (使用pandas)

    参数:
        file_path (str): Excel文件路径
        sheet_name (str): 工作表名称
        x_col (str/int): 作为X轴的列名或列索引（从0开始）
        y_col (str/int): 作为Y轴的列名或列索引
        title (str): 图表标题
        xlabel (str): X轴标签
        ylabel (str): Y轴标签
    """
    # 使用pandas读取Excel数据
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # 提取指定列数据
    x_data = df.iloc[:, x_col] if isinstance(x_col, int) else df[x_col]
    y_data = df.iloc[:, y_col] if isinstance(y_col, int) else df[y_col]

    # 绘制柱状图
    plt.figure(figsize=(10, 6))
    bars = plt.bar(x_data, y_data, color='skyblue')

    # 添加数值标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height,
                 f'{height:.1f}',
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
    x_column = "产品"  # 或列索引 (如 0 表示第一列)
    y_column = "销量"  # 或列索引 (如 1 表示第二列)

    # 绘制图表
    plot_bar_chart_from_excel(
        file_path=excel_file,
        sheet_name=sheet,
        x_col=x_column,
        y_col=y_column,
        title="销售数据柱状图 (Pandas版)",
        xlabel="产品名称",
        ylabel="销售量"
    )