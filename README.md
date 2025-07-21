# shenchen
# GeoGPT 夜间灯光查询服务（MCP）

本项目是一个基于 Google Earth Engine 的地理查询工具，支持通过输入经纬度坐标，获取指定位置在 2022 年 12 月的夜间灯光强度数据（avg_rad 值）。

本项目已适配 ModelScope MCP 平台，支持托管部署和自动服务调用。

---

## 📦 项目结构

```
.
├── main.py              # 主服务执行脚本
├── requirements.txt     # 项目依赖
├── service.json         # MCP 服务配置文件（平台自动识别）
└── README.md            # 项目说明
```

---

## 🚀 快速开始

### ✅ 本地运行

```bash
pip install -r requirements.txt
python main.py --longitude 10.75 --latitude 59.91 --output result.txt
```

运行后将在 `result.txt` 中获得该位置的夜间灯光信息（单位：avg_rad）。

---

## 🤖 MCP 服务配置说明

本项目已包含标准的 `service.json` 文件，支持从 GitHub 快速创建 MCP 服务：

```json
{
  "mpcServers": {
    "nightlight_query": {
      "args": ["--longitude", "10.75", "--latitude", "59.91", "--output", "result.txt"],
      "command": "python3 main.py --longitude 10.75 --latitude 59.91 --output result.txt",
      "env": {}
    }
  }
}
```

---

## 🌍 环境变量建议（可选）

| 变量名          | 说明                      | 示例值          |
|------------------|---------------------------|------------------|
| `EE_PROJECT_ID`  | GEE 项目 ID               | astro-465808     |
| `API_KEY`        | 可选 API 授权密钥         | your-api-key     |
| `MAP_OUTPUT_DIR` | 导出图像/地图的保存路径   | ./output         |

---

## 📋 依赖说明

- `earthengine-api`：Google Earth Engine 官方 API
- `geemap`：地理可视化辅助工具
- `pandas`：数据结构支持（用于结果格式化）

---

## 👤 作者信息

由 Albus 构建。如需合作或反馈建议，欢迎联系。
