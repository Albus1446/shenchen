# shenchen

本项目基于 [Google Earth Engine](https://earthengine.google.com/) 和 [ModelScope MCP](https://modelscope.cn/) 平台，提供对任意经纬度位置的夜间灯光数据查询服务。支持自动部署为 ModelScope MCP 服务。

---

## 📌 功能简介

- 🔍 输入经纬度（例如：`10.75, 59.91`）
- 📅 查询 2022 年 12 月的 NOAA 夜间灯光数据（avg_rad）
- 📤 输出为 JSON 格式结果
- 🌐 支持部署为可托管 MCP 服务

---

## 🗂️ 项目结构

```
.
├── main.py              # MCP 服务入口脚本
├── requirements.txt     # Python依赖声明
└── service.json         # ModelScope MCP 服务配置文件
```

---

## 🚀 使用方法

### ✅ 方式一：本地测试

1. 安装依赖：

```bash
pip install -r requirements.txt
```

2. 运行查询：

```bash
python main.py --longitude 10.75 --latitude 59.91 --output result.txt
```

3. 查看输出结果：

```json
[{'city': 'Test Point', 'avg_rad': 100.23003}]
```

> ✅ 注意：首次使用 Earth Engine API，请运行：
> ```bash
> earthengine authenticate
> ```

---

### ✅ 方式二：部署到 ModelScope MCP

1. 将本项目上传至 GitHub；
2. 登录 [modelscope.cn](https://modelscope.cn)；
3. 选择【MCP广场】→【创建 MCP 服务】→ 选择 GitHub 仓库；
4. 在“服务配置”中填写或上传 `service.json`；
5. 构建并运行即可。

---

## 📦 依赖库

- `earthengine-api`
- `geemap`

---

## 📍 示例说明

```bash
python main.py --longitude 113.30 --latitude 23.13 --output result.txt
```

将在 `result.txt` 中写入该坐标在 2022 年 12 月的夜间灯光强度（单位：avg_rad）。

---

## 🧠 授权说明

本服务使用 Earth Engine 数据，需要提前授权账户。默认项目名为 `astro-465808`，如需替换请在 `main.py` 中修改：

```python
ee.Initialize(project='your_project_name')
```

---

## ✨ 贡献与反馈

如有建议、反馈或合作意向，欢迎联系作者 Albus。
