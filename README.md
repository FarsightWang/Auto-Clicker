# Auto URL Clicker

這是一個自動化訪問網址的工具，可以設定多個網址並自動循環訪問，每個網址停留指定時間。

## 功能特點

- 支援多個網址同時處理
- 可自定義每個網址的點擊次數
- 可設定影片播放等待時間
- 自動追蹤進度並顯示統計資訊
- 錯誤自動處理和重試機制

## 安裝需求

1. Python 3.x
2. Microsoft Edge 瀏覽器
3. 必要的 Python 套件：
```bash
pip3 install selenium webdriver-manager
```

## 使用方法

1. 複製專案：
```bash
git clone [你的專案URL]
cd [專案資料夾名稱]
```

2. 安裝依賴套件：
```bash
pip3 install selenium webdriver-manager
```

3. 執行程式：
```bash
python3 auto_clicker.py
```

4. 依照提示輸入：
   - 要訪問的網址（每行一個，輸入空白行完成）
   - 每個網址的點擊次數（預設 200）
   - 影片播放時間（預設 3 秒）

## 使用範例

```bash
=== 自動點擊程式 ===
請輸入要訪問的短網址（每行一個，輸入空白行完成）：
https://example1.com
https://example2.com
[輸入空白行]

請輸入每個網址要點擊的次數（預設200）：200
請輸入影片播放時間（秒，預設3）：3
```

## 注意事項

1. 確保電腦已安裝 Microsoft Edge 瀏覽器
2. 保持網路連線穩定
3. 程式執行時請勿關閉瀏覽器視窗
4. 如需停止程式，按下 `Ctrl+C`（Windows）或 `Command+C`（Mac）

## 常見問題

Q: 程式無法執行？
A: 請確認：
- Python 已正確安裝
- 已安裝所有依賴套件
- Microsoft Edge 瀏覽器已安裝
- 網路連線正常

Q: 瀏覽器自動關閉？
A: 這是正常現象，程式會在發生錯誤時自動重啟瀏覽器。

## License

MIT License
