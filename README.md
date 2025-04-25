# AI Chat Bot

這是一個使用 Google Gemini AI 模型的智慧問答機器人，提供 Web 介面和 CLI 介面兩種使用方式。

## 功能特點

- Web 介面：提供直觀的聊天界面
  - 即時對話功能
  - 打字動畫效果
  - 錯誤處理和提示
  - 響應式設計
- CLI 介面：方便開發和測試
  - 支援多種命令（help, clear, exit）
  - 錯誤處理
  - 使用者友好的界面
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

CLI 介面支援以下命令：
- `help`: 顯示可用命令
- `clear`: 清除螢幕
- `exit`: 退出程式

## Vercel 部署

專案已經配置好 Vercel 部署設定，包含：
- vercel.json 配置
- 環境變數設定
- 路由配置

### 環境變數設定
在 Vercel 專案設定中需要設定以下環境變數：
- `GEMINI_API_KEY`: 你的 Gemini API key
- `GEMINI_MODEL`: gemini-1.5-flash

## 注意事項

- API Key 已配置在 vercel.json 中
- 使用 Gemini 1.5 Flash 模型
- 所有配置都可以在 vercel.json 中調整
- 建議在生產環境中使用環境變數來儲存敏感資訊

## 錯誤處理

- Web 介面會顯示錯誤訊息
- CLI 介面會顯示錯誤詳情
- 所有錯誤都會被記錄並適當處理 