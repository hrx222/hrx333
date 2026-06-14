interface AIResponse {
  type: 'explanation' | 'code_help' | 'suggestion';
  content: string;
}

const mockResponses: Record<string, AIResponse> = {
  'pandas': {
    type: 'explanation',
    content: `Pandas 是 Python 中最流行的数据处理库，核心数据结构是 DataFrame。

**主要功能：**
1. 数据读取：pd.read_csv(), pd.read_excel()
2. 数据选择：df['column'], df.iloc[], df.loc[]
3. 数据清洗：df.dropna(), df.fillna(), df.replace()
4. 数据聚合：df.groupby(), df.agg()

**学习建议：** 建议先掌握 DataFrame 的基本操作，然后学习 groupby 和 merge 这些高级功能。`,
  },
  'matplotlib': {
    type: 'code_help',
    content: `Matplotlib 是 Python 可视化的基础库。

**基本语法：**
\`\`\`python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='data')
plt.title('Title')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.show()
\`\`\`

**常用图表类型：**
- plt.plot() - 折线图
- plt.scatter() - 散点图
- plt.bar() - 柱状图
- plt.hist() - 直方图
- plt.boxplot() - 箱线图`,
  },
  'scikit-learn': {
    type: 'explanation',
    content: `Scikit-learn 是 Python 机器学习的基础库，提供了统一的 API 设计。

**核心流程：**
1. 数据预处理：StandardScaler, MinMaxScaler
2. 模型选择：train_test_split, cross_val_score
3. 训练模型：model.fit(X, y)
4. 预测：model.predict(X)
5. 评估：accuracy_score, confusion_matrix

**常用算法：**
- 分类：LogisticRegression, RandomForest, SVM
- 回归：LinearRegression, Ridge, Lasso
- 聚类：KMeans, DBSCAN
- 降维：PCA, t-SNE`,
  },
  'groupby': {
    type: 'code_help',
    content: `groupby 是 Pandas 中最强大的功能之一，用于分组聚合。

**基本用法：**
\`\`\`python
# 单列分组
df.groupby('column')['value'].mean()

# 多列分组
df.groupby(['col1', 'col2'])['value'].agg(['mean', 'sum', 'count'])

# 复杂聚合
df.groupby('category').agg({
    'sales': 'sum',
    'customers': 'nunique',
    'products': 'count'
})
\`\`\`

**技巧：** 使用 named aggregation 可以给聚合列起别名，方便后续处理。`,
  },
  '可视化': {
    type: 'code_help',
    content: `数据可视化是数据分析的重要组成部分！

**Seaborn 快捷图表：**
\`\`\`python
import seaborn as sns

# 分布图
sns.histplot(data, x='column', kde=True)

# 关系图
sns.scatterplot(data, x='x', y='y', hue='category')

# 热力图
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
\`\`\`

**选择图表的小技巧：**
- 比较关系 → 柱状图、折线图
- 分布关系 → 直方图、箱线图
- 构成关系 → 饼图、堆叠图
- 相关关系 → 散点图、热力图`,
  },
  'error': {
    type: 'suggestion',
    content: `遇到错误了吗？让我帮你分析：

**常见错误排查步骤：**
1. 仔细阅读错误信息，确定错误类型
2. 检查数据是否存在空值（NaN）
3. 确认数据类型是否匹配
4. 验证索引和切片是否正确

**如果还是解决不了：**
- 把完整的错误信息发给我
- 附上相关的数据样例
- 说明你想要实现的目标

我会帮你一步步排查问题！`,
  },
  'default': {
    type: 'explanation',
    content: `你好！我是 PyData AI 导师，可以帮你解答数据分析相关的问题。

**我可以帮助你：**
1. 解释概念和原理
2. 帮你理解代码逻辑
3. 提供代码示例和建议
4. 调试错误和分析问题

**你可以问我：**
- 某个函数怎么使用？
- 这个错误是什么意思？
- 如何实现某个数据分析流程？
- 推荐一些学习资源？

请告诉我你需要什么帮助！`,
  },
};

export function getAIResponse(userMessage: string): AIResponse {
  const lowerMessage = userMessage.toLowerCase();

  for (const [keyword, response] of Object.entries(mockResponses)) {
    if (lowerMessage.includes(keyword.toLowerCase())) {
      return response;
    }
  }

  return mockResponses['default'];
}

export function simulateTypingEffect(
  text: string,
  onChar: (char: string) => void,
  onComplete: () => void
): () => void {
  let index = 0;
  let timeoutId: ReturnType<typeof setTimeout>;

  const type = () => {
    if (index < text.length) {
      onChar(text[index]);
      index++;
      timeoutId = setTimeout(type, 20);
    } else {
      onComplete();
    }
  };

  timeoutId = setTimeout(type, 500);

  return () => clearTimeout(timeoutId);
}
