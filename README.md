# AI Chat Bot

這是一個使用 Google Gemini AI 模型的智慧問答機器人，提供 Web 介面和 CLI 介面兩種使用方式。

## 功能特點

- Web 介面：提供直觀的聊天界面
- CLI 介面：方便開發和測試
- 使用 Google Gemini AI 模型
- 支援 Vercel 部署

## 安裝

1. 安裝依賴套件：
```bash
pip install -r requirements.txt
```

## 使用方式

### Web 介面
1. 啟動 Flask 伺服器：
```bash
python api/app.py
```
2. 在瀏覽器中訪問 `http://localhost:5000`

### CLI 介面
```bash
python api/app.py --cli
```

## Vercel 部署

專案已經配置好 Vercel 部署設定，包含：
- vercel.json 配置
- 環境變數設定
- 路由配置

## 注意事項

- API Key 已配置在 vercel.json 中
- 使用 Gemini 1.5 Flash 模型
- 所有配置都可以在 vercel.json 中調整 