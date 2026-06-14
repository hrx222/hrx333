#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成适合数据分析初学者的10个训练项目"""

import json

def escape_string(s):
    """Escape single quotes and backslashes in strings for TypeScript single-quoted strings"""
    if isinstance(s, str):
        return s.replace('\\', '\\\\').replace("'", "\\'")
    return s

projects_data = [
    {
        "id": "python-basics",
        "title": "Python数据分析基础",
        "titleEn": "Python Basics for Data Analysis",
        "difficulty": "入门",
        "duration": "2小时",
        "description": "学习Python中用于数据分析的基本语法和数据结构，为后续学习打下坚实基础。",
        "objectives": [
            "掌握列表、字典、元组的基本操作",
            "学会使用NumPy创建和操作数组",
            "理解Python基本数据结构在数据分析中的应用"
        ],
        "prerequisites": ["零基础可学"],
        "techStack": ["Python", "NumPy"],
        "content": {
            "theory": """Python是数据分析领域最流行的编程语言之一，它的语法简洁易学，功能强大。

数据分析中常用的Python数据结构：
1. 列表(List)：有序的可变集合，用于存储一系列数据
2. 字典(Dict)：键值对形式存储数据，便于快速查找
3. 元组(Tuple)：有序的不可变集合，用于存储固定数据
4. 集合(Set)：无序不重复的元素集合，用于去重

NumPy是Python数据分析的基础库，提供了高效的多维数组对象ndarray。""",
            "codeExample": {
                "language": "python",
                "code": """import numpy as np

# 列表基本操作
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(f"平方后: {squared}")

# 字典操作
data = {'name': '张三', 'score': 85}
print(f"姓名: {data['name']}")

# NumPy数组创建
arr = np.array([1, 2, 3, 4, 5])
print(f"数组: {arr}")
print(f"均值: {arr.mean()}")
print(f"标准差: {arr.std()}")

# 数组运算
arr2 = arr * 2
print(f"翻倍: {arr2}")"""
            }
        },
        "quiz": [
            {
                "id": "py-q1",
                "type": "choice",
                "question": "下列哪个是Python中用于存储键值对的数据结构？",
                "options": ["列表(List)", "字典(Dict)", "元组(Tuple)", "集合(Set)"],
                "correctAnswer": "字典(Dict)",
                "explanation": "字典(Dict)使用键值对的形式存储数据，格式为{key: value}，可以通过键快速查找对应的值。"
            },
            {
                "id": "py-q2",
                "type": "choice",
                "question": "NumPy中用于创建数组的核心对象是什么？",
                "options": ["list", "array", "ndarray", "matrix"],
                "correctAnswer": "ndarray",
                "explanation": "ndarray是NumPy的多维数组对象(N-dimensional array)，是NumPy中存储和操作数据的主要方式。"
            },
            {
                "id": "py-q3",
                "type": "code",
                "question": "如何创建一个包含1到5的一维NumPy数组？",
                "correctAnswer": "np.array([1,2,3,4,5])",
                "explanation": "使用np.array()函数将Python列表转换为NumPy数组。",
                "codeSnippet": "_____([1, 2, 3, 4, 5])",
                "codeOptions": ["np.array", "np.list", "np.numpy", "np.create"]
            },
            {
                "id": "py-q4",
                "type": "choice",
                "question": "如何计算数组 [10, 20, 30, 40] 的平均值？",
                "options": ["[10,20,30,40].mean()", "mean([10,20,30,40])", "arr.mean() 其中arr是数组", "avg(10,20,30,40)"],
                "correctAnswer": "arr.mean() 其中arr是数组",
                "explanation": "NumPy数组对象有.mean()方法可以直接计算均值，前提是先将列表转换为数组。"
            },
            {
                "id": "py-q5",
                "type": "code",
                "question": "如何创建一个从0到9的一维数组？",
                "correctAnswer": "np.arange(10)",
                "explanation": "np.arange(start, stop, step) 可以创建规律数组，np.arange(10) 等价于 [0,1,2,3,4,5,6,7,8,9]。",
                "codeSnippet": "np._____(10)",
                "codeOptions": ["arange", "array", "range", "create"]
            },
            {
                "id": "py-q6",
                "type": "choice",
                "question": "元组(Tuple)和列表(List)的主要区别是什么？",
                "options": ["元组可以修改", "列表可以修改", "没有区别", "元组不支持索引"],
                "correctAnswer": "列表可以修改",
                "explanation": "元组(Tuple)是不可变的，创建后不能修改；列表(List)是可变的，可以添加、删除或修改元素。"
            },
            {
                "id": "py-q7",
                "type": "code",
                "question": "如何将字符串列表 ['a', 'b', 'c'] 转换为NumPy字符数组？",
                "correctAnswer": "np.array(['a', 'b', 'c'])",
                "explanation": "使用np.array()可以将Python列表（包括字符串列表）转换为NumPy数组。",
                "codeSnippet": "np._____(['a', 'b', 'c'])",
                "codeOptions": ["array", "chararray", "string", "text"]
            },
            {
                "id": "py-q8",
                "type": "choice",
                "question": "计算数组 [5, 10, 15, 20] 所有元素总和的正确方式是？",
                "options": ["sum = 5+10+15+20", "arr.sum() 其中arr是数组", "total([5,10,15,20])", "5+10+15+20.sum()"],
                "correctAnswer": "arr.sum() 其中arr是数组",
                "explanation": "NumPy数组使用.sum()方法计算元素总和，这是最简洁高效的方式。"
            },
            {
                "id": "py-q9",
                "type": "code",
                "question": "如何创建一个3x3的全零矩阵？",
                "correctAnswer": "np.zeros((3, 3))",
                "explanation": "np.zeros(shape) 创建指定形状的全零数组，(3,3)表示3行3列的二维数组。",
                "codeSnippet": "np._____((3, 3))",
                "codeOptions": ["zeros", "zero", "empty", "ones"]
            },
            {
                "id": "py-q10",
                "type": "choice",
                "question": "集合(Set)的主要特点是什么？",
                "options": ["有序且可重复", "无序且可重复", "无序且不重复", "有序且不重复"],
                "correctAnswer": "无序且不重复",
                "explanation": "集合(Set)有两个核心特点：1)无序，意味着元素没有固定顺序；2)不重复，自动去除重复元素。"
            }
        ]
    },
    {
        "id": "pandas-dataframe",
        "title": "Pandas数据框操作",
        "titleEn": "Pandas DataFrame Operations",
        "difficulty": "入门",
        "duration": "3小时",
        "description": "学习Pandas数据框的创建、查看、选择、筛选等核心操作，掌握数据分析的基本工具。",
        "objectives": [
            "掌握DataFrame的创建和基本查看方法",
            "学会行列选择和条件筛选",
            "理解数据索引和数据选择方法"
        ],
        "prerequisites": ["Python基础"],
        "techStack": ["Pandas"],
        "content": {
            "theory": """Pandas是Python数据分析中最核心的库，提供了高性能、易用的数据结构和数据分析工具。

DataFrame是Pandas中最常用的数据结构，它可以看作是一个表格型的数据结构，由行和列组成。

DataFrame的核心操作：
1. 创建：可以从字典、CSV文件、Excel文件等创建
2. 查看：head()查看前几行，info()查看信息，describe()查看统计信息
3. 选择：列选择用 df['列名']，行选择用 df.loc[] 或 df.iloc[]
4. 筛选：使用条件表达式筛选数据

常用的数据选择方法：
- df['column']：选择单列，返回Series
- df[['col1', 'col2']]：选择多列，返回DataFrame
- df.loc[条件]：按标签选择
- df.iloc[位置]：按位置选择""",
            "codeExample": {
                "language": "python",
                "code": """import pandas as pd

# 创建DataFrame
data = {
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, 30, 35, 28],
    '城市': ['北京', '上海', '广州', '深圳']
}
df = pd.DataFrame(data)

# 查看数据
print(df.head())
print(df.info())

# 列选择
print(df['姓名'])

# 条件筛选：筛选年龄大于28的人
result = df[df['年龄'] > 28]
print(result)

# 新增列
df['是否在京'] = df['城市'] == '北京'
print(df)"""
            }
        },
        "quiz": [
            {
                "id": "pd-q1",
                "type": "choice",
                "question": "如何查看DataFrame的前5行数据？",
                "options": ["df.head()", "df.head(5)", "df.first()", "df.top()"],
                "correctAnswer": "df.head()",
                "explanation": "df.head()默认显示前5行，df.head(n)可以指定显示前n行。这是快速查看数据结构的常用方法。"
            },
            {
                "id": "pd-q2",
                "type": "code",
                "question": "如何选择'姓名'这一列数据？",
                "correctAnswer": "df['姓名']",
                "explanation": "使用 df['列名'] 或 df.列名 来选择单列，返回一个Series对象。",
                "codeSnippet": "df._____",
                "codeOptions": ["['姓名']", "[姓名]", ".姓名", "['name']"]
            },
            {
                "id": "pd-q3",
                "type": "choice",
                "question": "如何筛选年龄大于30的记录？",
                "options": ["df[df.年龄>30]", "df.filter(年龄>30)", "df.select(年龄>30)", "df.where(年龄>30)"],
                "correctAnswer": "df[df.年龄>30]",
                "explanation": "使用布尔条件进行筛选，df[df['列名'] 条件] 是标准的筛选语法。"
            },
            {
                "id": "pd-q4",
                "type": "code",
                "question": "如何查看DataFrame的数据类型和缺失值信息？",
                "correctAnswer": "df.info()",
                "explanation": "df.info()显示DataFrame的列名、数据类型、缺失值数量等重要信息，是了解数据结构的第一个步骤。",
                "codeSnippet": "df._____()",
                "codeOptions": ["info", "describe", "dtypes", "shape"]
            },
            {
                "id": "pd-q5",
                "type": "choice",
                "question": "df.loc 和 df.iloc 的主要区别是什么？",
                "options": ["loc按标签，iloc按位置", "iloc按标签，loc按位置", "没有区别", "loc用于列，iloc用于行"],
                "correctAnswer": "loc按标签，iloc按位置",
                "explanation": "df.loc[] 基于行/列的标签（名称）进行选择，df.iloc[] 基于行/列的整数位置进行选择。"
            },
            {
                "id": "pd-q6",
                "type": "code",
                "question": "如何添加一个新列'分数'到DataFrame？",
                "correctAnswer": "df['分数'] = [85, 90, 78, 92]",
                "explanation": "直接通过赋值的方式添加新列，等号右边可以是列表、常量或数组，长度需与DataFrame行数一致。",
                "codeSnippet": "df[_____] = [85, 90, 78, 92]",
                "codeOptions": ["'分数'", "\"分数\"", "分数", "score"]
            },
            {
                "id": "pd-q7",
                "type": "choice",
                "question": "如何获取DataFrame的形状(行数和列数)？",
                "options": ["df.shape", "df.size", "df.dimensions", "df.length"],
                "correctAnswer": "df.shape",
                "explanation": "df.shape返回一个元组(df.shape[0]是行数，df.shape[1]是列数)，是快速了解数据规模的方式。"
            },
            {
                "id": "pd-q8",
                "type": "code",
                "question": "如何选择第3到第5行数据？",
                "correctAnswer": "df.iloc[2:5]",
                "explanation": "df.iloc[2:5]使用位置索引，选择第3、4、5行（索引2,3,4）。注意iloc是左闭右开区间。",
                "codeSnippet": "df._____[2:5]",
                "codeOptions": ["iloc", "loc", "ix", "get"]
            },
            {
                "id": "pd-q9",
                "type": "choice",
                "question": "df.describe() 返回什么信息？",
                "options": ["数据的基本统计信息", "数据的详细说明", "列的数据类型", "数据的索引信息"],
                "correctAnswer": "数据的基本统计信息",
                "explanation": "df.describe()返回数值列的计数、均值、标准差、最小值、分位数、最大值等统计信息。"
            },
            {
                "id": "pd-q10",
                "type": "code",
                "question": "如何重命名'年龄'列为'user_age'？",
                "correctAnswer": "df.rename(columns={'年龄': 'user_age'})",
                "explanation": "df.rename(columns=字典)可以重命名列，字典的键是原列名，值是新列名。",
                "codeSnippet": "df._____(columns={'年龄': 'user_age'})",
                "codeOptions": ["rename", "rename_column", "change_name", "set_names"]
            }
        ]
    },
    {
        "id": "data-cleaning",
        "title": "数据清洗与预处理",
        "titleEn": "Data Cleaning and Preprocessing",
        "difficulty": "入门",
        "duration": "3小时",
        "description": "学习处理缺失值、重复值、异常值等常见数据问题，掌握数据分析中最重要的数据清洗技能。",
        "objectives": [
            "学会识别和处理缺失值",
            "掌握去除重复数据的方法",
            "能够识别和处理异常值"
        ],
        "prerequisites": ["Pandas基础"],
        "techStack": ["Pandas", "NumPy"],
        "content": {
            "theory": """数据清洗是数据分析中最耗时的环节，通常占据分析师60%-80%的时间。脏数据会导致分析结果出现偏差，因此数据清洗至关重要。

常见的数据问题及处理方法：

1. 缺失值(Missing Values)
   - 识别：df.isnull().sum() 查看每列缺失数量
   - 处理方法：
     * 删除：df.dropna() 删除包含缺失值的行/列
     * 填充：df.fillna(值) 用指定值填充
     * 插补：用均值、中位数、众数等填充

2. 重复值(Duplicates)
   - 识别：df.duplicated().sum() 统计重复行数
   - 处理：df.drop_duplicates() 删除重复行

3. 异常值(Outliers)
   - 识别方法：箱线图、3倍标准差原则
   - 处理：根据业务逻辑判断是保留还是修正""",
            "codeExample": {
                "language": "python",
                "code": """import pandas as pd
import numpy as np

# 创建带缺失值和重复值的数据
data = {
    '姓名': ['张三', '李四', '张三', '王五', None],
    '年龄': [25, 30, 25, 28, 35],
    '分数': [85, None, 90, 78, 88]
}
df = pd.DataFrame(data)

# 查看缺失值
print(df.isnull().sum())

# 处理缺失值：用均值填充分数
df['分数'] = df['分数'].fillna(df['分数'].mean())

# 删除姓名缺失的行
df = df.dropna(subset=['姓名'])

# 去除重复行
df = df.drop_duplicates()

print(df)"""
            }
        },
        "quiz": [
            {
                "id": "dc-q1",
                "type": "choice",
                "question": "如何统计每列的缺失值数量？",
                "options": ["df.isnull().sum()", "df.missing()", "df.na_count()", "df.null()"],
                "correctAnswer": "df.isnull().sum()",
                "explanation": "isnull()返回布尔DataFrame，sum()对每列求和，得到每列缺失值的数量。"
            },
            {
                "id": "dc-q2",
                "type": "code",
                "question": "如何删除包含缺失值的整行数据？",
                "correctAnswer": "df.dropna()",
                "explanation": "dropna()默认删除任何含有缺失值的行，axis=1时删除列。",
                "codeSnippet": "df._____()",
                "codeOptions": ["dropna", "remove_na", "delete_na", "clear_na"]
            },
            {
                "id": "dc-q3",
                "type": "choice",
                "question": "用均值填充缺失值，应该使用哪个方法？",
                "options": ["df.fillna(均值)", "df.fillna(df.mean())", "df.fill_mean()", "df.impute(均值)"],
                "correctAnswer": "df.fillna(df.mean())",
                "explanation": "fillna()用于填充缺失值，df.mean()计算每列均值，这样可以对数值列智能填充。"
            },
            {
                "id": "dc-q4",
                "type": "code",
                "question": "如何删除完全相同的重复行？",
                "correctAnswer": "df.drop_duplicates()",
                "explanation": "drop_duplicates()删除完全相同的重复行，keep='first'保留第一条，keep='last'保留最后一条。",
                "codeSnippet": "df._____()",
                "codeOptions": ["drop_duplicates", "remove_duplicates", "delete_duplicates", "unique"]
            },
            {
                "id": "dc-q5",
                "type": "choice",
                "question": "箱线图中，高于上四分位数1.5倍IQR的数据点称为？",
                "options": ["缺失值", "正常值", "异常值", "边界值"],
                "correctAnswer": "异常值",
                "explanation": "箱线图中，超过上四分位数+1.5*IQR或下四分位数-1.5*IQR的数据点被认为是异常值。IQR是四分位距。"
            },
            {
                "id": "dc-q6",
                "type": "code",
                "question": "删除'姓名'列中有缺失值的行，应该怎么写？",
                "correctAnswer": "df.dropna(subset=['姓名'])",
                "explanation": "dropna的subset参数指定只考虑某些列的缺失值，括号内是列名列表。",
                "codeSnippet": "df.dropna(_____=['姓名'])",
                "codeOptions": ["subset", "columns", "axis", "on"]
            },
            {
                "id": "dc-q7",
                "type": "choice",
                "question": "df.duplicated() 返回的是什么类型的数据？",
                "options": ["DataFrame", "Series(bool)", "Array", "Scalar"],
                "correctAnswer": "Series(bool)",
                "explanation": "duplicated()返回一个布尔Series，True表示该行是重复行（之前见过），用于筛选或统计重复行数量。"
            },
            {
                "id": "dc-q8",
                "type": "code",
                "question": "将缺失值填充为0的正确写法是？",
                "correctAnswer": "df.fillna(0)",
                "explanation": "fillna()方法用指定值填充缺失值，0是常用的填充值之一，也可以用均值、中位数等。",
                "codeSnippet": "df._____(0)",
                "codeOptions": ["fillna", "replace_na", "change_na", "fill"]
            },
            {
                "id": "dc-q9",
                "type": "choice",
                "question": "处理缺失值时，什么情况适合使用删除法？",
                "options": ["缺失比例很大", "缺失比例很小", "任何情况", "数据量大时"],
                "correctAnswer": "缺失比例很小",
                "explanation": "当缺失值比例很小（<5%）时，删除缺失行对数据整体分布影响不大；当缺失比例大时，应考虑填充法。"
            },
            {
                "id": "dc-q10",
                "type": "code",
                "question": "检查是否有重复行并统计数量？",
                "correctAnswer": "df.duplicated().sum()",
                "explanation": "duplicated()返回布尔Series，sum()统计True的数量，即重复行的数量。",
                "codeSnippet": "df.duplicated()._____()",
                "codeOptions": ["sum", "count", "mean", "total"]
            }
        ]
    },
    {
        "id": "data-visualization",
        "title": "数据可视化基础",
        "titleEn": "Data Visualization Basics",
        "difficulty": "入门",
        "duration": "3小时",
        "description": "学习使用Matplotlib和Seaborn创建各种统计图表，将数据以直观的方式呈现出来。",
        "objectives": [
            "掌握Matplotlib的基本绘图方法",
            "学会使用Seaborn创建美观的统计图表",
            "能够根据数据特点选择合适的图表类型"
        ],
        "prerequisites": ["Pandas基础"],
        "techStack": ["Matplotlib", "Seaborn", "Pandas"],
        "content": {
            "theory": """数据可视化是数据分析结果展示的重要手段，好的可视化能让数据故事更加生动。

常用图表类型及适用场景：

1. 折线图(Line Plot)
   - 适用于：展示数据随时间变化的趋势
   - 例子：股票价格走势、月度销售额变化

2. 柱状图(Bar Plot)
   - 适用于：比较不同类别的数据大小
   - 例子：各产品销量对比、各城市人口对比

3. 散点图(Scatter Plot)
   - 适用于：展示两个变量之间的关系
   - 例子：身高与体重关系、面积与价格关系

4. 直方图(Histogram)
   - 适用于：展示数据的分布情况
   - 例子：用户年龄分布、考试成绩分布

5. 饼图(Pie Chart)
   - 适用于：展示各部分占比
   - 例子：市场份额、预算分配

Matplotlib是Python绘图的基础库，Seaborn基于Matplotlib提供了更美观的统计图表API。""",
            "codeExample": {
                "language": "python",
                "code": """import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建示例数据
data = pd.DataFrame({
    '月份': ['1月', '2月', '3月', '4月', '5月'],
    '销售额': [120, 135, 150, 142, 168]
})

# 折线图
plt.figure(figsize=(10, 4))
plt.plot(data['月份'], data['销售额'], marker='o')
plt.title('月度销售额趋势')
plt.xlabel('月份')
plt.ylabel('销售额(万元)')
plt.grid(True)
plt.show()

# 柱状图
plt.figure(figsize=(10, 4))
sns.barplot(x='月份', y='销售额', data=data)
plt.title('月度销售额对比')
plt.show()"""
            }
        },
        "quiz": [
            {
                "id": "vis-q1",
                "type": "choice",
                "question": "展示数据随时间变化的趋势，应该使用哪种图表？",
                "options": ["折线图", "柱状图", "饼图", "散点图"],
                "correctAnswer": "折线图",
                "explanation": "折线图适合展示数据随时间变化的趋势，能直观显示上升、下降、波动等模式。"
            },
            {
                "id": "vis-q2",
                "type": "code",
                "question": "如何设置中文字体显示？",
                "correctAnswer": "plt.rcParams['font.sans-serif'] = ['SimHei']",
                "explanation": "Matplotlib需要单独设置中文字体，rcParams用于设置全局绘图参数。",
                "codeSnippet": "plt._____['font.sans-serif'] = ['SimHei']",
                "codeOptions": ["rcParams", "rc", "config", "settings"]
            },
            {
                "id": "vis-q3",
                "type": "choice",
                "question": "比较多个类别的数据大小，适合使用什么图表？",
                "options": ["散点图", "折线图", "柱状图", "直方图"],
                "correctAnswer": "柱状图",
                "explanation": "柱状图通过柱子的高度对比不同类别的数值大小，是比较数据的经典方式。"
            },
            {
                "id": "vis-q4",
                "type": "code",
                "question": "如何创建子图布局（2行2列）？",
                "correctAnswer": "plt.subplots(2, 2)",
                "explanation": "subplots(nrows, ncols)创建子图网格，返回fig和axes对象用于分别控制画布和子图。",
                "codeSnippet": "plt._____(2, 2)",
                "codeOptions": ["subplots", "subplot", "figure", "add_subplots"]
            },
            {
                "id": "vis-q5",
                "type": "choice",
                "question": "展示两个变量之间的关系，适合使用什么图表？",
                "options": ["饼图", "柱状图", "散点图", "直方图"],
                "correctAnswer": "散点图",
                "explanation": "散点图用点的位置表示两个变量的值，能够直观展示变量之间的相关关系。"
            },
            {
                "id": "vis-q6",
                "type": "code",
                "question": "如何设置图表标题？",
                "correctAnswer": "plt.title('标题')",
                "explanation": "title()方法设置图表标题，通常放在绘图代码的最后或show()之前。",
                "codeSnippet": "plt._____('月度销售趋势')",
                "codeOptions": ["title", "set_title", "heading", "caption"]
            },
            {
                "id": "vis-q7",
                "type": "choice",
                "question": "展示数据的分布情况，适合使用什么图表？",
                "options": ["折线图", "饼图", "直方图", "散点图"],
                "correctAnswer": "直方图",
                "explanation": "直方图将数据分成多个区间，统计每个区间的数据数量，能展示数据的频率分布。"
            },
            {
                "id": "vis-q8",
                "type": "code",
                "question": "如何显示网格线？",
                "correctAnswer": "plt.grid(True)",
                "explanation": "grid(True)添加网格线，grid(False)隐藏网格线，使图表更易读。",
                "codeSnippet": "plt._____(True)",
                "codeOptions": ["grid", "show_grid", "lines", "guide"]
            },
            {
                "id": "vis-q9",
                "type": "choice",
                "question": "Seaborn的barplot默认会显示什么？",
                "options": ["标准差", "均值", "总和", "计数"],
                "correctAnswer": "均值",
                "explanation": "Seaborn的barplot默认显示均值并附带置信区间，适合比较不同类别的均值差异。"
            },
            {
                "id": "vis-q10",
                "type": "code",
                "question": "如何保存图表为PNG文件？",
                "correctAnswer": "plt.savefig('chart.png')",
                "explanation": "savefig()保存图表，需在show()之前调用，常用格式包括png、jpg、pdf等。",
                "codeSnippet": "plt._____('chart.png')",
                "codeOptions": ["savefig", "export", "download", "write"]
            }
        ]
    },
    {
        "id": "groupby-aggregation",
        "title": "分组与聚合操作",
        "titleEn": "GroupBy and Aggregation",
        "difficulty": "初级",
        "duration": "2小时",
        "description": "学习使用groupby进行数据分组，掌握各种聚合函数的使用方法。",
        "objectives": [
            "理解groupby的工作原理",
            "掌握单一列和多个列的分组方法",
            "学会使用多种聚合函数"
        ],
        "prerequisites": ["Pandas基础"],
        "techStack": ["Pandas"],
        "content": {
            "theory": """分组聚合是数据分析中最常用的操作之一，用于将数据按某个维度分组后进行统计。

groupby的工作流程（Split-Apply-Combine）：
1. Split（拆分）：按一个或多个列将数据分成多个组
2. Apply（应用）：对每个组应用一个或多个聚合函数
3. Combine（合并）：将结果合并成新的数据结构

常用聚合函数：
- count()：计数
- sum()：求和
- mean()：均值
- median()：中位数
- std()：标准差
- min()：最小值
- max()：最大值
- agg()：自定义聚合

多函数聚合：
df.groupby('列').agg({'列1': 'sum', '列2': 'mean'})""",
            "codeExample": {
                "language": "python",
                "code": """import pandas as pd

# 创建销售数据
data = {
    '部门': ['销售部', '技术部', '销售部', '技术部', '销售部'],
    '员工': ['张三', '李四', '王五', '赵六', '孙七'],
    '销售额': [100, 80, 120, 90, 110],
    '订单数': [10, 8, 12, 9, 11]
}
df = pd.DataFrame(data)

# 按部门分组，计算销售额均值
sales_by_dept = df.groupby('部门')['销售额'].mean()
print(sales_by_dept)

# 多列分组
result = df.groupby(['部门', '员工']).agg({
    '销售额': 'sum',
    '订单数': 'mean'
})
print(result)

# 使用agg添加多个聚合
stats = df.groupby('部门')['销售额'].agg(['sum', 'mean', 'max'])
print(stats)"""
            }
        },
        "quiz": [
            {
                "id": "ga-q1",
                "type": "choice",
                "question": "groupby的工作流程是什么？",
                "options": ["拆分-应用-合并", "合并-拆分-应用", "应用-合并-拆分", "拆分-合并-应用"],
                "correctAnswer": "拆分-应用-合并",
                "explanation": "groupby遵循Split-Apply-Combine流程：先拆分数据为多个组，对每组应用聚合函数，最后合并结果。"
            },
            {
                "id": "ga-q2",
                "type": "code",
                "question": "按'部门'列分组并计算'工资'列的均值？",
                "correctAnswer": "df.groupby('部门')['工资'].mean()",
                "explanation": "groupby('列名')[要聚合的列].聚合函数() 是基本的分组聚合语法。",
                "codeSnippet": "df._____('部门')['工资'].mean()",
                "codeOptions": ["groupby", "group", "aggregate", "split"]
            },
            {
                "id": "ga-q3",
                "type": "choice",
                "question": "如何对不同列应用不同的聚合函数？",
                "options": ["df.groupby().agg({})", "df.groupby().apply({})", "df.groupby().transform({})", "df.groupby().aggregate({})"],
                "correctAnswer": "df.groupby().agg({})",
                "explanation": "agg()方法接受字典参数，键是列名，值是聚合函数名称，可以对不同列使用不同聚合。"
            },
            {
                "id": "ga-q4",
                "type": "code",
                "question": "同时计算分组后的总和与均值？",
                "correctAnswer": "agg(['sum', 'mean'])",
                "explanation": "agg(['func1', 'func2'])可以对同一列应用多个聚合函数，返回多列结果。",
                "codeSnippet": "['销售额'].agg([_____])",
                "codeOptions": ["'sum', 'mean'", "'mean', 'sum'", "'count', 'sum'", "'max', 'min'"]
            },
            {
                "id": "ga-q5",
                "type": "choice",
                "question": "count()和size()有什么区别？",
                "options": ["count()不包括NaN，size()包括", "count()包括NaN，size()不包括", "没有区别", "count()返回Series，size()返回DataFrame"],
                "correctAnswer": "count()不包括NaN，size()包括",
                "explanation": "count()统计非空值的数量，而size()统计每组的总行数（包括NaN）。这是重要区别！"
            },
            {
                "id": "ga-q6",
                "type": "code",
                "question": "按多个列'部门'和'城市'分组？",
                "correctAnswer": "groupby(['部门', '城市'])",
                "explanation": "groupby接受列名列表进行多列分组，列表顺序决定分组层级。",
                "codeSnippet": "df._____(['部门', '城市'])",
                "codeOptions": ["groupby", "group", "aggregate", "clusterby"]
            },
            {
                "id": "ga-q7",
                "type": "choice",
                "question": "分组后如何计算每组的记录数？",
                "options": ["count()", "len()", "size()", "num()"],
                "correctAnswer": "size()",
                "explanation": "size()返回每组的元素总数（包括NaN），返回Series；count()返回非空值数量。"
            },
            {
                "id": "ga-q8",
                "type": "code",
                "question": "计算分组后标准差的正确写法是？",
                "correctAnswer": "std()",
                "explanation": "std()计算标准差，反映数据的离散程度。与mean()、sum()等用法相同。",
                "codeSnippet": "['分数']._____()",
                "codeOptions": ["std", "standard", "stdev", "deviation"]
            },
            {
                "id": "ga-q9",
                "type": "choice",
                "question": "df.groupby('A').B.mean() 和 df.groupby('A')['B'].mean() 哪个正确？",
                "options": ["两者都正确", "只有第一个正确", "只有第二个正确", "两者都不正确"],
                "correctAnswer": "两者都正确",
                "explanation": "两种写法等价，df.groupby('A').B.mean()更简洁，df.groupby('A')['B'].mean()更明确。"
            },
            {
                "id": "ga-q10",
                "type": "code",
                "question": "使用transform计算分组均值？",
                "correctAnswer": "transform('mean')",
                "explanation": "transform()返回一个与原数据框等长的Series，适合添加到原数据框作为新列。",
                "codeSnippet": "'分数'._____('mean')",
                "codeOptions": ["transform", "apply", "agg", "map"]
            }
        ]
    },
    {
        "id": "descriptive-statistics",
        "title": "描述性统计分析",
        "titleEn": "Descriptive Statistics Analysis",
        "difficulty": "初级",
        "duration": "2小时",
        "description": "学习计算和使用各种描述性统计量，全面了解数据的分布特征。",
        "objectives": [
            "掌握集中趋势指标的计算方法",
            "理解离散程度指标的含义",
            "学会解读统计报告"
        ],
        "prerequisites": ["Pandas基础"],
        "techStack": ["Pandas", "NumPy", "SciPy"],
        "content": {
            "theory": """描述性统计是对数据基本特征的总结和描述，是数据分析的基础。

一、集中趋势指标（描述数据中心位置）：
1. 均值(Mean)：所有数值的平均，易受极端值影响
2. 中位数(Median)：排序后位于中间的数，不受极端值影响
3. 众数(Mode)：出现最多的数值，适用于分类数据

二、离散程度指标（描述数据分散程度）：
1. 方差(Variance)：各数据与均值差平方的平均值
2. 标准差(Standard Deviation)：方差的平方根，与原数据单位相同
3. 极差(Range)：最大值与最小值之差
4. 四分位距(IQR)：Q3与Q1之差，用于识别异常值

三、分布形状：
1. 偏度(Skewness)：数据分布的对称程度
2. 峰度(Kurtosis)：数据分布的尖峭程度""",
            "codeExample": {
                "language": "python",
                "code": """import pandas as pd
import numpy as np
from scipy import stats

# 创建示例数据
data = pd.DataFrame({
    '分数': [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
})

# 集中趋势
print(f"均值: {data['分数'].mean()}")
print(f"中位数: {data['分数'].median()}")
print(f"众数: {data['分数'].mode()[0]}")

# 离散程度
print(f"方差: {data['分数'].var()}")
print(f"标准差: {data['分数'].std()}")
print(f"极差: {data['分数'].max() - data['分数'].min()}")
print(f"IQR: {data['分数'].quantile(0.75) - data['分数'].quantile(0.25)}")

# 分布形状
print(f"偏度: {stats.skew(data['分数'])}")
print(f"峰度: {stats.kurtosis(data['分数'])}")

# 完整统计报告
print(data['分数'].describe())"""
            }
        },
        "quiz": [
            {
                "id": "ds-q1",
                "type": "choice",
                "question": "均值的优点和缺点是什么？",
                "options": ["稳定但易受极端值影响", "易受极端值影响但稳定", "对极端值不敏感", "只适用于分类数据"],
                "correctAnswer": "稳定但易受极端值影响",
                "explanation": "均值计算稳定，使用所有数据，但极端值会显著影响结果，此时中位数更合适。"
            },
            {
                "id": "ds-q2",
                "type": "code",
                "question": "计算中位数的函数是？",
                "correctAnswer": "median()",
                "explanation": "median()计算中位数，是描述集中趋势的重要指标，不受极端值影响。",
                "codeSnippet": "df['分数']._____()",
                "codeOptions": ["median", "middle", "center", "avg()"]
            },
            {
                "id": "ds-q3",
                "type": "choice",
                "question": "标准差和方差的关系是什么？",
                "options": ["标准差是方差的平方根", "方差是标准差的平方根", "两者没有直接关系", "标准差等于方差"],
                "correctAnswer": "方差是标准差的平方根",
                "explanation": "标准差 = √方差。标准差与原数据单位相同，更容易解释；方差是标准差的平方。"
            },
            {
                "id": "ds-q4",
                "type": "code",
                "question": "计算75%分位数的正确写法是？",
                "correctAnswer": "quantile(0.75)",
                "explanation": "quantile(p)计算第p分位数，quantile(0.75)即75%分位数，也叫第三四分位数Q3。",
                "codeSnippet": "df['分数'].quantile(_____)",
                "codeOptions": ["0.75", "0.25", "0.5", "1.0"]
            },
            {
                "id": "ds-q5",
                "type": "choice",
                "question": "偏度大于0表示什么分布特征？",
                "options": ["右偏/正偏", "左偏/负偏", "对称分布", "均匀分布"],
                "correctAnswer": "右偏/正偏",
                "explanation": "偏度>0表示右偏（正偏），即右侧有较长尾巴，均值大于中位数；偏度<0表示左偏。"
            },
            {
                "id": "ds-q6",
                "type": "code",
                "question": "如何一次性获取所有描述性统计量？",
                "correctAnswer": "describe()",
                "explanation": "describe()返回计数、均值、标准差、最小值、25%、50%、75%分位数和最大值。",
                "codeSnippet": "df['分数']._____()",
                "codeOptions": ["describe", "summary", "statistics", "report"]
            },
            {
                "id": "ds-q7",
                "type": "choice",
                "question": "IQR（四分位距）是什么的差值？",
                "options": ["Q3和Q1", "最大值和最小值", "均值和中位数", "Q2和Q1"],
                "correctAnswer": "Q3和Q1",
                "explanation": "IQR = Q3 - Q1，表示中间50%数据的范围，是识别异常值的重要指标。"
            },
            {
                "id": "ds-q8",
                "type": "code",
                "question": "使用SciPy计算偏度？",
                "correctAnswer": "stats.skew(data)",
                "explanation": "scipy.stats.skew()计算偏度，正值表示右偏，负值表示左偏，0表示对称分布。",
                "codeSnippet": "stats._____(data)",
                "codeOptions": ["skew", "skewness", "skew_data", "distribution"]
            },
            {
                "id": "ds-q9",
                "type": "choice",
                "question": "为什么有时候中位数比均值更适合描述数据中心？",
                "options": ["中位数不受极端值影响", "中位数计算更简单", "均值不能用于数据分析", "中位数更常用"],
                "correctAnswer": "中位数不受极端值影响",
                "explanation": "当数据存在极端值时，均值会被拉偏，而中位数作为位置中心，不受极端值影响。"
            },
            {
                "id": "ds-q10",
                "type": "code",
                "question": "计算方差的方法是？",
                "correctAnswer": "var()",
                "explanation": "var()计算方差，是各数据与均值差平方的平均值，反映数据的离散程度。",
                "codeSnippet": "df['分数']._____()",
                "codeOptions": ["var", "variance", "var_", "variation"]
            }
        ]
    },
    {
        "id": "pivot-table",
        "title": "数据透视表与交叉分析",
        "titleEn": "Pivot Table and Cross Analysis",
        "difficulty": "初级",
        "duration": "2小时",
        "description": "学习使用数据透视表进行多维度数据分析，掌握交叉表的创建和使用。",
        "objectives": [
            "掌握pivot_table的创建方法",
            "学会使用crosstab进行交叉分析",
            "能够进行多维度数据汇总"
        ],
        "prerequisites": ["Pandas基础", "分组聚合"],
        "techStack": ["Pandas"],
        "content": {
            "theory": """数据透视表是数据分析中最强大的工具之一，能快速对数据进行多维度汇总分析。

pivot_table参数说明：
- index：行索引（分组维度）
- columns：列索引（分组维度）
- values：要聚合的数值列
- aggfunc：聚合函数（默认是mean）
- fill_value：缺失值填充
- margins：是否显示合计行/列

crosstab用于计算两个（或多个）分类变量的交叉表。

透视表 vs 交叉表：
- pivot_table：更灵活，可自定义聚合函数
- crosstab：专门用于计算频次交叉表""",
            "codeExample": {
                "language": "python",
                "code": """import pandas as pd
import numpy as np

# 创建销售数据
data = {
    '地区': ['华北', '华东', '华南', '华北', '华东', '华南'],
    '产品': ['手机', '电脑', '手机', '电脑', '手机', '电脑'],
    '季度': ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2'],
    '销售额': [100, 150, 120, 110, 160, 130]
}
df = pd.DataFrame(data)

# 创建透视表：按地区和产品汇总销售额
pivot = pd.pivot_table(df, values='销售额',
                       index='地区', columns='产品',
                       aggfunc='sum')
print(pivot)

# 添加合计行
pivot_with_margins = pd.pivot_table(df, values='销售额',
                                    index='地区', columns='产品',
                                    aggfunc='sum', margins=True)
print(pivot_with_margins)

# 交叉表：统计频次
crosstab = pd.crosstab(df['地区'], df['产品'])
print(crosstab)"""
            }
        },
        "quiz": [
            {
                "id": "pt-q1",
                "type": "choice",
                "question": "pivot_table中，哪个参数指定要聚合的数值列？",
                "options": ["values", "index", "columns", "aggfunc"],
                "correctAnswer": "values",
                "explanation": "values参数指定要聚合的数值列，index指定行维度，columns指定列维度，aggfunc指定聚合函数。"
            },
            {
                "id": "pt-q2",
                "type": "code",
                "question": "按'城市'和'产品'创建透视表？",
                "correctAnswer": "pivot_table",
                "explanation": "pd.pivot_table()创建透视表，需要指定数据源、聚合列、行维度和列维度。",
                "codeSnippet": "pd._____",
                "codeOptions": ["pivot_table", "pivot", "cross_table", "group_table"]
            },
            {
                "id": "pt-q3",
                "type": "choice",
                "question": "如何显示透视表的合计行和合计列？",
                "options": ["margins=True", "total=True", "sum=True", "aggregate=True"],
                "correctAnswer": "margins=True",
                "explanation": "margins=True在透视表边缘添加合计行/列，显示各维度及总体的汇总值。"
            },
            {
                "id": "pt-q4",
                "type": "code",
                "question": "使用交叉表分析'地区'和'产品'的关系？",
                "correctAnswer": "pd.crosstab(df['地区'], df['产品'])",
                "explanation": "crosstab计算两个分类变量的频次交叉表，行维度第一个参数，列维度第二个参数。",
                "codeSnippet": "pd._____(df['地区'], df['产品'])",
                "codeOptions": ["crosstab", "pivot_table", "cross", "tabulation"]
            },
            {
                "id": "pt-q5",
                "type": "choice",
                "question": "pivot_table的默认聚合函数是什么？",
                "options": ["mean", "sum", "count", "median"],
                "correctAnswer": "mean",
                "explanation": "aggfunc默认是'mean'（均值），可以改为'sum'、'count'、'max'等其他聚合函数。"
            },
            {
                "id": "pt-q6",
                "type": "code",
                "question": "设置聚合函数为求和？",
                "correctAnswer": "aggfunc='sum'",
                "explanation": "aggfunc参数指定聚合函数，可以是字符串('sum', 'mean'等)或自定义函数。",
                "codeSnippet": "aggfunc=_____",
                "codeOptions": ["'sum'", "'mean'", "'count'", "'max'"]
            },
            {
                "id": "pt-q7",
                "type": "choice",
                "question": "crosstab和pivot_table的主要区别是什么？",
                "options": ["crosstab专门用于频次分析", "pivot_table不能汇总", "crosstab不能设置聚合函数", "两者完全相同"],
                "correctAnswer": "crosstab专门用于频次分析",
                "explanation": "crosstab主要用于计算两个分类变量的频次交叉表，pivot_table功能更广泛，可自定义聚合函数。"
            },
            {
                "id": "pt-q8",
                "type": "code",
                "question": "缺失值用0填充怎么写？",
                "correctAnswer": "fill_value=0",
                "explanation": "fill_value参数指定缺失值的填充值，使透视表更整洁。",
                "codeSnippet": "fill_value=_____",
                "codeOptions": ["0", "None", "'0'", "False"]
            },
            {
                "id": "pt-q9",
                "type": "choice",
                "question": "透视表的'index'参数作用是什么？",
                "options": ["指定行索引维度", "指定列索引维度", "指定要聚合的列", "指定聚合函数"],
                "correctAnswer": "指定行索引维度",
                "explanation": "index参数指定作为透视表行索引的列，即第一个分组维度。columns指定列维度。"
            },
            {
                "id": "pt-q10",
                "type": "code",
                "question": "对透视表计算后的值应用多个聚合函数？",
                "correctAnswer": "aggfunc=['sum', 'mean']",
                "explanation": "aggfunc可以接受函数列表，对同一列同时应用多个聚合函数进行计算。",
                "codeSnippet": "aggfunc=[_____)",
                "codeOptions": ["'sum', 'mean'", "'sum'", "'count', 'mean'", "'max', 'min'"]
            }
        ]
    },
    {
        "id": "correlation-analysis",
        "title": "相关性分析",
        "titleEn": "Correlation Analysis",
        "difficulty": "初级",
        "duration": "2小时",
        "description": "学习计算和分析变量之间的相关性，理解相关矩阵并可视化相关关系。",
        "objectives": [
            "掌握相关系数的计算方法",
            "理解不同相关系数的适用场景",
            "能够解读相关矩阵"
        ],
        "prerequisites": ["Pandas基础", "统计基础"],
        "techStack": ["Pandas", "Seaborn"],
        "content": {
            "theory": """相关性分析用于衡量两个变量之间关系的强弱和方向。

一、相关系数类型：
1. Pearson相关系数：衡量线性关系，默认方法
   - 取值范围：[-1, 1]
   - 0表示无线性关系
   - >0表示正相关，<0表示负相关

2. Spearman相关系数：衡量单调关系，适用于非正态分布
3. Kendall相关系数：基于秩次的相关系数

二、相关系数解读：
- |r| < 0.3：弱相关
- 0.3 ≤ |r| < 0.5：中等相关
- 0.5 ≤ |r| < 0.7：较强相关
- |r| ≥ 0.7：强相关

三、注意事项：
- 相关不等于因果
- 异常值会显著影响Pearson相关系数
- 非线性关系可能显示低相关性""",
            "codeExample": {
                "language": "python",
                "code": """import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
data = pd.DataFrame({
    '身高': [170, 165, 180, 175, 160],
    '体重': [65, 55, 80, 72, 50],
    '年龄': [25, 30, 35, 28, 22],
    '工资': [8000, 6000, 15000, 10000, 5000]
})
df = pd.DataFrame(data)

# 计算相关矩阵（Pearson）
corr_matrix = df.corr()
print(corr_matrix)

# 计算Spearman相关系数
spearman_corr = df.corr(method='spearman')
print(spearman_corr)

# 可视化相关矩阵
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm',
            center=0, fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# 散点图矩阵
sns.pairplot(df)
plt.show()"""
            }
        },
        "quiz": [
            {
                "id": "ca-q1",
                "type": "choice",
                "question": "Pearson相关系数的取值范围是多少？",
                "options": ["[-1, 1]", "[0, 1]", "[-∞, ∞]", "[0, 100]"],
                "correctAnswer": "[-1, 1]",
                "explanation": "Pearson相关系数r的取值范围是[-1, 1]，r=1表示完全正相关，r=-1表示完全负相关，r=0表示无相关。"
            },
            {
                "id": "ca-q2",
                "type": "code",
                "question": "计算DataFrame的相关矩阵？",
                "correctAnswer": "df.corr()",
                "explanation": "corr()计算DataFrame中所有数值列两两之间的Pearson相关系数矩阵。",
                "codeSnippet": "df._____()",
                "codeOptions": ["corr", "correlation", "relate", "connect"]
            },
            {
                "id": "ca-q3",
                "type": "choice",
                "question": "r=0.85表示什么程度的相关？",
                "options": ["强正相关", "弱正相关", "中等相关", "负相关"],
                "correctAnswer": "强正相关",
                "explanation": "|r|≥0.7为强相关，r=0.85>0，符号为正，所以是强正相关，表示两个变量有很强的线性正相关关系。"
            },
            {
                "id": "ca-q4",
                "type": "code",
                "question": "计算Spearman相关系数？",
                "correctAnswer": "method='spearman'",
                "explanation": "corr(method='spearman')使用Spearman方法，适用于非正态分布或等级数据。",
                "codeSnippet": "df.corr(_____='spearman')",
                "codeOptions": ["method", "type", "mode", "kind"]
            },
            {
                "id": "ca-q5",
                "type": "choice",
                "question": "相关系数r=-0.6表示什么？",
                "options": ["中等负相关", "中等正相关", "强负相关", "弱负相关"],
                "correctAnswer": "中等负相关",
                "explanation": "0.5≤|r|<0.7为中等相关，r=-0.6为负值，所以是中等负相关，表示一个变量增加时另一个变量倾向于减少。"
            },
            {
                "id": "ca-q6",
                "type": "code",
                "question": "可视化相关矩阵用什么图表最合适？",
                "correctAnswer": "热力图heatmap()",
                "explanation": "热力图适合展示相关矩阵，用颜色深浅表示相关系数大小，annot=True显示数值。",
                "codeSnippet": "sns._____",
                "codeOptions": ["heatmap", "barplot", "scatter", "pairplot"]
            },
            {
                "id": "ca-q7",
                "type": "choice",
                "question": "Pearson相关系数衡量的是什么关系？",
                "options": ["线性关系", "指数关系", "对数关系", "单调关系"],
                "correctAnswer": "线性关系",
                "explanation": "Pearson相关系数衡量两个变量之间的线性关系强度和方向，不适合非线性关系。"
            },
            {
                "id": "ca-q8",
                "type": "code",
                "question": "相关矩阵中显示数值用什么参数？",
                "correctAnswer": "annot=True",
                "explanation": "annot=True在热力图的每个格子中显示相关系数的数值，便于精确查看。",
                "codeSnippet": "heatmap(____=True)",
                "codeOptions": ["annot", "show_values", "label", "text"]
            },
            {
                "id": "ca-q9",
                "type": "choice",
                "question": "为什么说'相关不等于因果'？",
                "options": ["两个变量相关可能有第三个变量影响", "相关系数计算错误", "样本量太小", "数据有缺失值"],
                "correctAnswer": "两个变量相关可能有第三个变量影响",
                "explanation": "两个变量相关可能只是因为共同受到第三个变量的影响，要证明因果关系需要更多证据。"
            },
            {
                "id": "ca-q10",
                "type": "code",
                "question": "绘制散点图矩阵的函数是？",
                "correctAnswer": "pairplot()",
                "explanation": "pairplot()一次性展示所有数值变量两两之间的散点图，快速了解多变量关系。",
                "codeSnippet": "sns._____",
                "codeOptions": ["pairplot", "scatter_matrix", "plot_matrix", "grid_plot"]
            }
        ]
    },
    {
        "id": "data-types-conversion",
        "title": "数据类型转换",
        "titleEn": "Data Type Conversion",
        "difficulty": "初级",
        "duration": "2小时",
        "description": "学习Pandas中各种数据类型的识别和转换方法，确保数据格式正确。",
        "objectives": [
            "掌握数据类型识别方法",
            "学会字符串和数值的相互转换",
            "理解日期时间类型的处理"
        ],
        "prerequisites": ["Pandas基础"],
        "techStack": ["Pandas"],
        "content": {
            "theory": """数据类型是数据分析的基础，错误的数据类型会导致计算错误或功能失效。

常见数据类型：
1. int64：整数类型
2. float64：浮点数类型
3. object：字符串或混合类型
4. datetime64：日期时间类型
5. bool：布尔类型
6. category：分类类型（节省内存）

类型转换注意事项：
- astype()：直接转换，可能丢失信息
- to_numeric()：转换为数值类型，带错误处理
- to_datetime()：转换为日期时间
- pd.to_numeric(..., errors='coerce')：转换失败时设为NaN""",
            "codeExample": {
                "language": "python",
                "code": """import pandas as pd

# 创建混合类型数据
data = {
    '编号': ['001', '002', '003', '004'],
    '年龄': ['25', '30', '35', '28'],
    '工资': ['8000', '6000', '15000', '10000'],
    '入职日期': ['2020-01-15', '2019-05-20', '2021-03-10', '2018-11-05']
}
df = pd.DataFrame(data)

# 查看数据类型
print(df.dtypes)

# 字符串转数值
df['年龄'] = pd.to_numeric(df['年龄'])
df['工资'] = pd.to_numeric(df['工资'], errors='coerce')

# 字符串转日期
df['入职日期'] = pd.to_datetime(df['入职日期'])

# 数值转字符串
df['编号'] = df['编号'].astype(str)

# 提取日期特征
df['入职年份'] = df['入职日期'].dt.year
df['入职月份'] = df['入职日期'].dt.month

print(df.dtypes)
print(df)"""
            }
        },
        "quiz": [
            {
                "id": "dt-q1",
                "type": "choice",
                "question": "如何查看DataFrame的列数据类型？",
                "options": ["df.dtypes", "df.types", "df.type", "df.dataType"],
                "correctAnswer": "df.dtypes",
                "explanation": "dtypes属性返回每列的数据类型，是一个Series，索引是列名，值是数据类型。"
            },
            {
                "id": "dt-q2",
                "type": "code",
                "question": "将'年龄'列转换为整数类型？",
                "correctAnswer": "astype('int')",
                "explanation": "astype()方法用于类型转换，'int'或'int64'转换为整数类型。",
                "codeSnippet": "df['年龄']._____('int')",
                "codeOptions": ["astype", "convert", "to_int", "change"]
            },
            {
                "id": "dt-q3",
                "type": "choice",
                "question": "将字符串转换为日期时间应该用什么函数？",
                "options": ["to_datetime()", "to_date()", "to_time()", "parse_date()"],
                "correctAnswer": "to_datetime()",
                "explanation": "pd.to_datetime()将字符串转换为datetime64类型，是处理日期数据的标准方法。"
            },
            {
                "id": "dt-q4",
                "type": "code",
                "question": "转换失败时不报错而是设为NaN？",
                "correctAnswer": "errors='coerce'",
                "explanation": "errors='coerce'参数在转换失败时将值设为NaN而不是抛出异常，保证程序继续运行。",
                "codeSnippet": "pd.to_numeric(____='coerce')",
                "codeOptions": ["errors", "handle", "on_error", "mode"]
            },
            {
                "id": "dt-q5",
                "type": "choice",
                "question": "object类型在Pandas中通常表示什么？",
                "options": ["字符串或混合类型", "只能是对象", "数值类型", "日期类型"],
                "correctAnswer": "字符串或混合类型",
                "explanation": "object类型是Pandas的万能类型，通常表示字符串，但也可能包含混合数据类型。"
            },
            {
                "id": "dt-q6",
                "type": "code",
                "question": "从日期列提取年份用什么属性？",
                "correctAnswer": "dt.year",
                "explanation": "datetime列使用.dt访问器，.year提取年份，.month提取月份，.day提取日期。",
                "codeSnippet": "df['日期']._____.year",
                "codeOptions": ["dt", "date", "time", "datetime"]
            },
            {
                "id": "dt-q7",
                "type": "choice",
                "question": "category类型的主要优点是什么？",
                "options": ["节省内存", "计算更快", "显示更美观", "便于排序"],
                "correctAnswer": "节省内存",
                "explanation": "category类型将字符串存储为整数代码，大大节省内存，适用于重复值较多的分类数据。"
            },
            {
                "id": "dt-q8",
                "type": "code",
                "question": "将'数值'列转换为字符串类型？",
                "correctAnswer": "astype('str')",
                "explanation": "astype('str')将任何类型转换为字符串类型，方便字符串操作。",
                "codeSnippet": "df['数值']._____('str')",
                "codeOptions": ["astype", "convert", "to_string", "str()"]
            },
            {
                "id": "dt-q9",
                "type": "choice",
                "question": "to_numeric()和astype()的主要区别是什么？",
                "options": ["to_numeric有errors参数", "to_numeric更快", "astype更安全", "没有区别"],
                "correctAnswer": "to_numeric有errors参数",
                "explanation": "to_numeric()支持errors='coerce'参数处理转换失败的情况，astype()转换失败会直接报错。"
            },
            {
                "id": "dt-q10",
                "type": "code",
                "question": "查看DataFrame信息包括数据类型的最快方法是？",
                "correctAnswer": "info()",
                "explanation": "info()方法快速显示DataFrame的索引、数据类型、非空值数量等信息，比dtypes更全面。",
                "codeSnippet": "df._____()",
                "codeOptions": ["info", "describe", "summary", "dtypes"]
            }
        ]
    },
    {
        "id": "csv-file-operation",
        "title": "CSV文件读写操作",
        "titleEn": "CSV File Read and Write Operations",
        "difficulty": "入门",
        "duration": "2小时",
        "description": "学习使用Pandas读写CSV文件，掌握数据导入导出的基本技能。",
        "objectives": [
            "掌握CSV文件的读取方法",
            "学会导出数据到CSV文件",
            "理解常见读取参数的作用"
        ],
        "prerequisites": ["Pandas基础"],
        "techStack": ["Pandas"],
        "content": {
            "theory": """CSV（Comma-Separated Values）是最常见的数据文件格式，Pandas提供了强大的CSV读写功能。

read_csv常用参数：
- filepath_or_buffer：文件路径
- sep/delimiter：分隔符（默认逗号）
- header：表头行号（默认0）
- index_col：作为索引的列
- usecols：只读取指定的列
- dtype：指定列的数据类型
- encoding：文件编码（常用utf-8、gbk）
- nrows：只读取前n行
- na_values：识别为缺失值的字符串

to_csv常用参数：
- path_or_buf：输出文件路径
- sep：分隔符
- index：是否写入索引（默认True）
- encoding：输出编码""",
            "codeExample": {
                "language": "python",
                "code": """import pandas as pd

# 读取CSV文件
df = pd.read_csv('data.csv')
print(df.head())

# 指定编码读取
df_utf8 = pd.read_csv('data.csv', encoding='utf-8')
df_gbk = pd.read_csv('data.csv', encoding='gbk')

# 只读取指定列
df_subset = pd.read_csv('data.csv', usecols=['姓名', '年龄', '工资'])

# 读取时指定数据类型
df = pd.read_csv('data.csv', dtype={'年龄': int, '工资': float})

# 写入CSV文件
df.to_csv('output.csv', index=False, encoding='utf-8')

# 写入时指定分隔符
df.to_csv('output.tsv', sep='\\t', index=False)

print('文件读写完成！')"""
            }
        },
        "quiz": [
            {
                "id": "csv-q1",
                "type": "choice",
                "question": "读取CSV文件的函数是？",
                "options": ["pd.read_csv()", "pd.load_csv()", "pd.open_csv()", "pd.import_csv()"],
                "correctAnswer": "pd.read_csv()",
                "explanation": "pd.read_csv()是Pandas读取CSV文件的标准函数，返回DataFrame。"
            },
            {
                "id": "csv-q2",
                "type": "code",
                "question": "指定读取编码为utf-8？",
                "correctAnswer": "encoding='utf-8'",
                "explanation": "encoding参数指定文件编码，中文文件常用'utf-8'或'gbk'。",
                "codeSnippet": "read_csv('data.csv', _____='utf-8')",
                "codeOptions": ["encoding", "charset", "code", "format"]
            },
            {
                "id": "csv-q3",
                "type": "choice",
                "question": "只读取'姓名'和'年龄'两列应该用什么参数？",
                "options": ["usecols", "columns", "select", "include"],
                "correctAnswer": "usecols",
                "explanation": "usecols参数指定要读取的列名列表，可以减少内存占用和读取时间。",
                "code": "read_csv('data.csv', _____=['姓名', '年龄'])"
            },
            {
                "id": "csv-q4",
                "type": "code",
                "question": "不写入行索引到CSV文件？",
                "correctAnswer": "index=False",
                "explanation": "to_csv的index=False参数确保不将DataFrame的索引写入CSV文件，避免产生多余的索引列。",
                "codeSnippet": "to_csv('output.csv', _____=False)",
                "codeOptions": ["index", "row_index", "header", "ignore"]
            },
            {
                "id": "csv-q5",
                "type": "choice",
                "question": "分隔符是Tab的文件应该用什么函数读取？",
                "options": ["read_csv(sep='\\t')", "read_tsv()", "read_table()", "read_fwf()"],
                "correctAnswer": "read_csv(sep='\\t')",
                "explanation": "read_csv()的sep参数可以指定任何分隔符，'\\t'表示Tab分隔，read_csv默认读取逗号分隔。",
                "explanation": "sep='\\t'"
            },
            {
                "id": "csv-q6",
                "type": "code",
                "question": "指定'年龄'列为整数类型读取？",
                "correctAnswer": "dtype={'年龄': int}",
                "explanation": "dtype参数接受字典，键是列名，值是指定的数据类型，可以加快读取速度。",
                "codeSnippet": "read_csv('data.csv', _____{'年龄': int})",
                "codeOptions": ["dtype", "type", "dtypes", "convert"]
            },
            {
                "id": "csv-q7",
                "type": "choice",
                "question": "处理中文CSV文件最常用的两种编码是？",
                "options": ["utf-8和gbk", "ascii和unicode", "utf-16和gb2312", "iso和windows"],
                "correctAnswer": "utf-8和gbk",
                "explanation": "中文CSV文件常用UTF-8或GBK编码，读取前需要确认文件编码格式，否则会乱码。"
            },
            {
                "id": "csv-q8",
                "type": "code",
                "question": "只读取前100行数据？",
                "correctAnswer": "nrows=100",
                "explanation": "nrows参数指定只读取前n行数据，适合大文件预览，可以节省时间和内存。",
                "codeSnippet": "read_csv('data.csv', _____=100)",
                "codeOptions": ["nrows", "rows", "limit", "head"]
            },
            {
                "id": "csv-q9",
                "type": "choice",
                "question": "将某列作为行索引读取，应该用哪个参数？",
                "options": ["index_col", "index", "set_index", "header"],
                "correctAnswer": "index_col",
                "explanation": "index_col参数指定某列作为DataFrame的行索引，值可以是列名或列序号。",
                "explanation": "index_col='姓名'"
            },
            {
                "id": "csv-q10",
                "type": "code",
                "question": "将数据导出为Tab分隔的TSV文件？",
                "correctAnswer": "sep='\\t'",
                "explanation": "to_csv的sep参数设置分隔符，'\\t'表示Tab分隔，生成TSV格式文件。",
                "codeSnippet": "to_csv('output.tsv', _____='\\t')",
                "codeOptions": ["sep", "delimiter", "tab", "split"]
            }
        ]
    }
]

# 生成TypeScript文件
lines = []
lines.append("export interface Project {")
lines.append("  id: string;")
lines.append("  title: string;")
lines.append("  titleEn: string;")
lines.append("  difficulty: '入门' | '初级' | '中级' | '高级';")
lines.append("  duration: string;")
lines.append("  description: string;")
lines.append("  objectives: string[];")
lines.append("  prerequisites: string[];")
lines.append("  techStack: string[];")
lines.append("  content: {")
lines.append("    theory: string;")
lines.append("    codeExample: {")
lines.append("      language: string;")
lines.append("      code: string;")
lines.append("    };")
lines.append("  };")
lines.append("  quiz: QuizQuestion[];")
lines.append("}")
lines.append("")
lines.append("export interface QuizQuestion {")
lines.append("  id: string;")
lines.append("  type: 'choice' | 'code';")
lines.append("  question: string;")
lines.append("  options?: string[];")
lines.append("  correctAnswer: string;")
lines.append("  explanation: string;")
lines.append("  codeSnippet?: string;")
lines.append("  codeOptions?: string[];")
lines.append("}")
lines.append("")
lines.append("export interface ChatMessage {")
lines.append("  id: string;")
lines.append("  role: 'user' | 'ai';")
lines.append("  content: string;")
lines.append("  timestamp: Date;")
lines.append("}")
lines.append("")
lines.append("export const projects: Project[] = [")

for i, project in enumerate(projects_data):
    lines.append("  {")
    lines.append(f"    id: '{project['id']}',")
    lines.append(f"    title: '{escape_string(project['title'])}',")
    lines.append(f"    titleEn: '{escape_string(project['titleEn'])}',")
    lines.append(f"    difficulty: '{project['difficulty']}',")
    lines.append(f"    duration: '{project['duration']}',")
    lines.append(f"    description: '{escape_string(project['description'])}',")
    
    lines.append("    objectives: [")
    for obj in project['objectives']:
        lines.append(f"      '{escape_string(obj)}',")
    lines.append("    ],")
    
    lines.append("    prerequisites: [")
    for prereq in project['prerequisites']:
        lines.append(f"      '{escape_string(prereq)}',")
    lines.append("    ],")
    
    lines.append("    techStack: [")
    for tech in project['techStack']:
        lines.append(f"      '{tech}',")
    lines.append("    ],")
    
    lines.append("    content: {")
    theory = project['content']['theory'].replace('`', '\\`').replace('${', '\\${')
    lines.append(f"      theory: `{theory}`,")
    code = project['content']['codeExample']['code'].replace('`', '\\`').replace('${', '\\${')
    lines.append("      codeExample: {")
    lines.append(f"        language: '{project['content']['codeExample']['language']}',")
    lines.append(f"        code: `{code}`,")
    lines.append("      },")
    lines.append("    },")
    
    lines.append("    quiz: [")
    for q in project['quiz']:
        lines.append("      {")
        lines.append(f"        id: '{q['id']}',")
        lines.append(f"        type: '{q['type']}',")
        lines.append(f"        question: '{escape_string(q['question'])}',")
        if q.get('options'):
            lines.append("        options: [")
            for opt in q['options']:
                lines.append(f"          '{escape_string(opt)}',")
            lines.append("        ],")
        lines.append(f"        correctAnswer: '{escape_string(q['correctAnswer'])}',")
        lines.append(f"        explanation: '{escape_string(q['explanation'])}',")
        if q.get('codeSnippet'):
            codeSnippet = q['codeSnippet'].replace('`', '\\`').replace('${', '\\${')
            lines.append(f"        codeSnippet: `{codeSnippet}`,")
        if q.get('codeOptions'):
            lines.append("        codeOptions: [")
            for opt in q['codeOptions']:
                lines.append(f"          '{escape_string(opt)}',")
            lines.append("        ],")
        lines.append("      },")
    lines.append("    ],")
    lines.append("  }" + ("" if i == len(projects_data) - 1 else ","))

lines.append("];")
lines.append("")
lines.append("export const difficultyColors: Record<string, string> = {")
lines.append("  '入门': 'bg-neon-green/20 text-neon-green border-neon-green/50',")
lines.append("  '初级': 'bg-neon-blue/20 text-neon-blue border-neon-blue/50',")
lines.append("  '中级': 'bg-neon-orange/20 text-neon-orange border-neon-orange/50',")
lines.append("  '高级': 'bg-neon-purple/20 text-neon-purple border-neon-purple/50',")
lines.append("};")
lines.append("")
lines.append("export const allTechStack = Array.from(")
lines.append("  new Set(projects.flatMap(p => p.techStack))")
lines.append(").sort();")

with open('/workspace/src/data/projects.ts', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("File generated successfully!")
