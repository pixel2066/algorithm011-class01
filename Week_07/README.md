# 学习笔记
## 第七周学习概要
### 本周学习时间有限，主要学习字典树和并查集，程序只练习了字典树，但是搞明白了python字典树创建方法：
python字典树创建方法主要是通过字典(Dictionary) setdefault()方法实现，主要通过Value 不断内嵌字典数据结构方式，不断往下层构建每个字符下一个临近的字符，构建等式为：node = node.setdefault(char, {})