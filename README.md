# DDoS Testing Tool

[🇮🇩 Bahasa Indonesia](#bahasa-indonesia) | [🇺🇸 English](#english)

---

## Bahasa Indonesia

### 📋 Deskripsi
Tool untuk melakukan stress testing dan load testing pada server web. Tool ini dilengkapi dengan dummy server untuk keperluan testing lokal dan fitur visualisasi yang menarik.

### ⚠️ Disclaimer
Tool ini dibuat untuk membantu kalian melakukan ddos ke websites tidak penting seperti judol

### 🎯 Fitur
- ✨ Animasi Matrix dengan logo RizzDevs
- 🎨 Interface terminal yang menarik dengan warna
- 📊 Monitoring real-time status server
- 🌐 IP spoofing otomatis
- 📈 Laporan statistik lengkap
- 🛑 Auto-stop ketika server down
- 🔄 Mode restart otomatis
- 🖥️ Dummy server untuk testing lokal

### 📁 Struktur Proyek
```
ddos/
├── app.py              # Tool DDoS utama
│── app.js          # Server dummy untuk testing
└── README.md           # Dokumentasi ini
```

## 🚀 Instalasi

### 1. Instalasi Termux (Android)
```bash
# Download Termux dari F-Droid
# Buka Termux dan update package
pkg update && pkg upgrade -y
```

### 2. Instalasi Python
```bash
# Install Python
pkg install python -y

# Verifikasi instalasi
python --version
```

### 3. Instalasi Node.js
```bash
# Install Node.js
pkg install nodejs -y

# Verifikasi instalasi
node --version
npm --version
```

### 4. Clone Repository
```bash
# Clone repository
git clone https://github.com/InDsToReE/ddos.git
cd ddos
```

### 5. Install Dependencies Python
```bash
# Install module yang diperlukan
pip install requests colorama psutil
```

### 6. Install Dependencies Node.js
```bash

# Install express
npm init -y
npm install express

# Kembali ke folder utama
cd ..
```

## 🛠️ Cara Penggunaan

### Menjalankan Dummy Server (Testing Lokal)
```bash

# Jalankan server
node app.js

# Server akan berjalan di http://localhost:3000
```

### Menjalankan DDoS Tool
```bash
# Jalankan tool utama
python app.py

# Ikuti instruksi di terminal:
# 1. Masukkan target URL (contoh: http://localhost:3000)
# 2. Masukkan jumlah request per detik (1-1000)
```

### Contoh Penggunaan
1. **Testing Lokal:**
   - Jalankan `node app.js` di terminal pertama
   - Jalankan `python app.py` di terminal kedua
   - Target URL: `http://localhost:3000`

2. **Testing External Server:**
   - Jalankan `python app.py`
   - Target URL: `https://example.com`
   - **Pastikan Anda memiliki izin!**

## 📊 Fitur Tool

### Interface Features
- 🎭 Animasi Matrix startup
- 🖥️ System specs monitoring
- 📱 Real-time status updates
- 📈 Success/failure rate tracking
- 🌍 IP distribution statistics

### Security Features
- 🔒 Rate limiting (1-1000 req/sec)
- 🛡️ Auto-stop protection
- ⏱️ Timeout handling
- 📝 Comprehensive logging

## ⚙️ Konfigurasi

### Parameter yang Dapat Diatur
- **Request Rate**: 1-1000 requests per detik
- **Timeout**: 3 detik per request
- **Auto-stop**: Server down selama 2+ detik
- **IP Spoofing**: Otomatis dengan header palsu

### Environment Variables (Opsional)
```bash
export DDOS_MAX_RATE=1000
export DDOS_TIMEOUT=3
export DDOS_AUTO_STOP=2
```

## 🔧 Troubleshooting

### Error: Module tidak ditemukan
```bash
pip install requests colorama psutil
```

### Error: Permission denied
```bash
chmod +x app.py
```

### Error: Port sudah digunakan
```bash
# Ganti port di app.js dari 3000 ke port lain
const PORT = 3001;
```

### Error: Connection refused
- Pastikan target URL benar dan dapat diakses
- Untuk testing lokal, pastikan dummy server berjalan

## 📋 Requirements

### Minimum Requirements
- **OS**: Android (Termux), Linux, macOS, Windows
- **Python**: 3.6+
- **Node.js**: 12+
- **RAM**: 512MB
- **Storage**: 100MB

### Dependencies
- `requests`: HTTP client library
- `colorama`: Terminal colors
- `psutil`: System information
- `express`: Web framework (Node.js)

## 🤝 Kontribusi
Kontribusi sangat diterima! Silakan:
1. Fork repository
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📄 Lisensi
Project ini menggunakan lisensi MIT. Lihat file `LICENSE` untuk detail.

## 📞 Kontak
- **Author**: Riski Ardiane
- **Email**: riskiardiane@gmail.com
- **GitHub**: [@riskiardiane](https://github.com/InDsToReE)

---

## English

### 📋 Description
A tool for performing stress testing and load testing on web servers. This tool comes with a dummy server for local testing purposes and attractive visualization features.

### ⚠️ Disclaimer
This tool is made to help you perform DDoS to unimportant websites like Judol.

### 🎯 Features
- ✨ Matrix animation with RizzDevs logo
- 🎨 Attractive terminal interface with colors
- 📊 Real-time server status monitoring
- 🌐 Automatic IP spoofing
- 📈 Comprehensive statistics reporting
- 🛑 Auto-stop when server is down
- 🔄 Automatic restart mode
- 🖥️ Dummy server for local testing

### 📁 Project Structure
```
ddos/
├── app.py              # Main DDoS tool
|── app.js          # Dummy server for testing
└── README.md           # This documentation
```

## 🚀 Installation

### 1. Install Termux (Android)
```bash
# Download Termux from F-Droid
# Open Termux and update packages
pkg update && pkg upgrade -y
```

### 2. Install Python
```bash
# Install Python
pkg install python -y

# Verify installation
python --version
```

### 3. Install Node.js
```bash
# Install Node.js
pkg install nodejs -y

# Verify installation
node --version
npm --version
```

### 4. Clone Repository
```bash
# Clone repository
git clone https://github.com/InDsToReE/ddos.git
cd ddos
```

### 5. Install Python Dependencies
```bash
# Install required modules
pip install requests colorama psutil
```

### 6. Install Node.js Dependencies
```bash

# Install express
npm init -y
npm install express

# Return to main folder
cd ..
```

## 🛠️ Usage

### Running Dummy Server (Local Testing)
```bash

# Run server
node app.js

# Server will run at http://localhost:3000
```

### Running DDoS Tool
```bash
# Run main tool
python app.py

# Follow terminal instructions:
# 1. Enter target URL (example: http://localhost:3000)
# 2. Enter requests per second (1-1000)
```

### Usage Examples
1. **Local Testing:**
   - Run `node app.js` in first terminal
   - Run `python app.py` in second terminal
   - Target URL: `http://localhost:3000`

2. **External Server Testing:**
   - Run `python app.py`
   - Target URL: `https://example.com`
   - **Make sure you have permission!**

## 📊 Tool Features

### Interface Features
- 🎭 Matrix startup animation
- 🖥️ System specs monitoring
- 📱 Real-time status updates
- 📈 Success/failure rate tracking
- 🌍 IP distribution statistics

### Security Features
- 🔒 Rate limiting (1-1000 req/sec)
- 🛡️ Auto-stop protection
- ⏱️ Timeout handling
- 📝 Comprehensive logging

## ⚙️ Configuration

### Configurable Parameters
- **Request Rate**: 1-1000 requests per second
- **Timeout**: 3 seconds per request
- **Auto-stop**: Server down for 2+ seconds
- **IP Spoofing**: Automatic with fake headers

### Environment Variables (Optional)
```bash
export DDOS_MAX_RATE=1000
export DDOS_TIMEOUT=3
export DDOS_AUTO_STOP=2
```

## 🔧 Troubleshooting

### Error: Module not found
```bash
pip install requests colorama psutil
```

### Error: Permission denied
```bash
chmod +x app.py
```

### Error: Port already in use
```bash
# Change port in app.js from 3000 to another port
const PORT = 3001;
```

### Error: Connection refused
- Make sure target URL is correct and accessible
- For local testing, ensure dummy server is running

## 📋 Requirements

### Minimum Requirements
- **OS**: Android (Termux), Linux, macOS, Windows
- **Python**: 3.6+
- **Node.js**: 12+
- **RAM**: 512MB
- **Storage**: 100MB

### Dependencies
- `requests`: HTTP client library
- `colorama`: Terminal colors
- `psutil`: System information
- `express`: Web framework (Node.js)

## 🤝 Contributing
Contributions are very welcome! Please:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Create Pull Request

## 📄 License
This project uses MIT license. See `LICENSE` file for details.

## 📞 Contact
- **Author**: Riski Ardiane
- **Email**: riskiardiane@gmail.com
- **GitHub**: [@riskiardiane](https://github.com/InDsToReE)

---

## 🚨 Legal Notice / Pemberitahuan Hukum

**English**: This tool is made to help you perform DDoS to unimportant websites like Judol.

**Indonesia**: Alat ini dibuat untuk membantu Anda melakukan DDoS ke situs web yang tidak penting seperti Judol.

---

## 📸 Screenshots

### Startup Animation
```
 ____  _            ____                  
|  _ \(_)___ ____  |  _ \  _____   _____ 
| |_) | |_  /_  /  | | | |/ _ \ \ / / __|
|  _ <| |/ / / /   | |_| |  __/\ V /\__ \
|_| \_\_/___/___/  |____/ \___| \_/ |___/
```

### Real-time Status
```
[14:23:15] ✓1247 | ✗23 | 🚨 SERVER DOWN ⳿2s | ⚡847.3/1000
```

## ⭐ Star History
If you find this project useful, please give it a star! ⭐

---

## Japan

# DDoS ツール

## 📋 説明

このツールは、Web サーバーに対するストレステストおよびロードテストを行うためのものです。ローカルテスト用のダミーサーバーや、魅力的な可視化機能が備わっています。

## ⚠️ 免責事項

このツールは、重要ではないウェブサイト（例: 賭博サイトなど）に対して DDoS を行うための学習・研究用の補助ツールとして作成されています。

## 🎯 機能

* ✨ RizzDevs ロゴ付きマトリックスアニメーション
* 🎨 カラフルで見やすいターミナルインターフェース
* 📊 サーバーのリアルタイムステータス監視
* 🌐 自動 IP スプーフィング
* 📈 詳細な統計レポート
* 🛑 サーバーダウン時の自動停止
* 🔄 自動リスタートモード
* 🖥️ ローカルテスト用のダミーサーバー

## 📁 プロジェクト構成

```
ddos/
├── app.py              # メインの DDoS ツール
│── app.js              # テスト用のダミーサーバー
└── README.md           # このドキュメント
```

## 🚀 インストール方法

### 1. Termux のインストール (Android)

```bash
# F-Droid から Termux をダウンロード
# Termux を開いてパッケージを更新
pkg update && pkg upgrade -y
```

### 2. Python のインストール

```bash
# Python をインストール
pkg install python -y

# インストール確認
python --version
```

### 3. Node.js のインストール

```bash
# Node.js をインストール
pkg install nodejs -y

# インストール確認
node --version
npm --version
```

### 4. リポジトリのクローン

```bash
# リポジトリをクローン
git clone https://github.com/InDsToReE/ddos.git
cd ddos
```

### 5. Python 依存関係のインストール

```bash
# 必要なモジュールをインストール
pip install requests colorama psutil
```

### 6. Node.js 依存関係のインストール

```bash
# express をインストール
npm init -y
npm install express

# メインフォルダに戻る
cd ..
```

## 🛠️ 使用方法

### ダミーサーバーの実行（ローカルテスト）

```bash
# サーバーを実行
node app.js

# サーバーは http://localhost:3000 で稼働
```

### DDoS ツールの実行

```bash
# メインツールを実行
python app.py

# ターミナルの指示に従ってください:
# 1. ターゲット URL を入力 (例: http://localhost:3000)
# 2. 1〜1000 のリクエスト数/秒を入力
```

### 使用例

1. **ローカルテスト:**

   * 1つ目のターミナルで `node app.js` を実行
   * 2つ目のターミナルで `python app.py` を実行
   * ターゲット URL: `http://localhost:3000`

2. **外部サーバーテスト:**

   * `python app.py` を実行
   * ターゲット URL: `https://example.com`
   * **必ず事前に許可を得てください！**

## 📊 ツール機能

### インターフェース機能

* 🎭 起動時のマトリックスアニメーション
* 🖥️ システムスペック監視
* 📱 リアルタイムのステータス更新
* 📈 成功率 / 失敗率のトラッキング
* 🌍 IP 分布統計

### セキュリティ機能

* 🔒 レート制限 (1〜1000 req/sec)
* 🛡️ 自動停止保護
* ⏱️ タイムアウト処理
* 📝 詳細なログ記録

## ⚙️ 設定

### 調整可能なパラメータ

* **リクエストレート**: 1〜1000 req/sec
* **タイムアウト**: 1リクエストあたり3秒
* **自動停止**: サーバーが2秒以上ダウンした場合
* **IP スプーフィング**: 偽ヘッダーで自動実行

### 環境変数 (オプション)

```bash
export DDOS_MAX_RATE=1000
export DDOS_TIMEOUT=3
export DDOS_AUTO_STOP=2
```

## 🔧 トラブルシューティング

### エラー: モジュールが見つかりません

```bash
pip install requests colorama psutil
```

### エラー: Permission denied

```bash
chmod +x app.py
```

### エラー: ポートが使用中

```bash
# app.js のポートを 3000 から別のポートに変更
const PORT = 3001;
```

### エラー: Connection refused

* ターゲット URL が正しく、アクセス可能であることを確認してください
* ローカルテストの場合、ダミーサーバーが実行されているか確認してください

## 📋 必要環境

### 最低環境

* **OS**: Android (Termux), Linux, macOS, Windows
* **Python**: 3.6+
* **Node.js**: 12+
* **RAM**: 512MB
* **ストレージ**: 100MB

### 依存関係

* `requests`: HTTP クライアントライブラリ
* `colorama`: ターミナルカラー
* `psutil`: システム情報
* `express`: Web フレームワーク (Node.js)

## 🤝 貢献

コントリビューションは大歓迎です！手順:

1. リポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/AmazingFeature`)
3. 変更をコミット (`git commit -m 'Add some AmazingFeature'`)
4. ブランチをプッシュ (`git push origin feature/AmazingFeature`)
5. プルリクエストを作成

## 📄 ライセンス

本プロジェクトは MIT ライセンスを採用しています。詳細は `LICENSE` ファイルをご確認ください。

## 📞 連絡先

* **作者**: Riski Ardiane
* **メール**: [riskiardiane@gmail.com](mailto:riskiardiane@gmail.com)
* **GitHub**: [@riskiardiane](https://github.com/InDsToReE)

---

**❤️ Riski Ardiane によって作成されました**


**Made with ❤️ by Riski Ardiane**
