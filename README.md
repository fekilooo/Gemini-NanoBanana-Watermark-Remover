# Gemini NanoBanana Watermark Remover

這是一個 Chrome 瀏覽器擴充功能，專門用於自動移除 Google Gemini AI 生成圖片中的浮水印。

## 功能特色
- **自動去浮水印**：透過演算法自動識別並移除 Gemini 生成圖片的浮水印。
- **一鍵複製**：滑鼠懸停於圖片上時，左上角會出現「📋 複製無印版」按鈕。
- **無損畫質**：自動抓取原始高解析度圖片進行處理。
- **剪貼簿整合**：處理後的圖片直接寫入剪貼簿，方便貼上使用。

## 安裝方式 (手動安裝)

由於此擴充功能未上架 Chrome 線上應用程式商店，請依照以下步驟手動安裝：

1. **下載程式碼**
   - 點擊本頁面的 `Code` -> `Download ZIP` 並解壓縮，或使用 Git Clone 下載此儲存庫。

2. **開啟 Chrome 擴充功能管理頁面**
   - 在網址列輸入 `chrome://extensions/` 並按下 Enter。

3. **開啟開發人員模式**
   - 在右上角找到「開發人員模式 (Developer mode)」開關並將其**開啟**。

4. **載入已解壓縮的擴充功能**
   - 點擊左上角的「載入未封裝項目 (Load unpacked)」按鈕。
   - 選擇本專案內的 `gemini_extension` 資料夾 (包含 `manifest.json` 的該層資料夾)。

5. **完成**
   - 此時擴充功能應已安裝完成，回到 Gemini 網站重新整理即可使用。

## 使用方法
1. 前往 [Google Gemini](https://gemini.google.com/)。
2. 生成一張圖片。
3. 將滑鼠游標移動到圖片上。
4. 點擊左上角出現的 **「📋 複製無印版」** 按鈕。
5. 等待按鈕顯示「✅ 已複製！」後，即可將去浮水印的圖片貼上至其他程式。

## 隱私聲明
- 本擴充功能所有圖像處理皆在本地端 (瀏覽器內) 完成。
- 不會上傳任何圖片或使用者資料至任何外部伺服器。

## 授權
MIT License
來源自 https://github.com/journey-ad/gemini-watermark-remover