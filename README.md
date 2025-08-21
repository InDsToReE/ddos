# DDoS Testing Tool

[🇮🇩 Bahasa Indonesia](#bahasa-indonesia) | [🇺🇸 English](#english)

---

## Bahasa Indonesia

### 📋 Deskripsi
Tool untuk melakukan stress testing dan load testing pada server web. Tool ini dilengkapi dengan dummy server untuk keperluan testing lokal dan fitur visualisasi yang menarik.

### ⚠️ Disclaimer
Tool ini dibuat untuk tujuan **edukasi dan testing** saja. Penggunaan untuk menyerang server tanpa izin adalah **ilegal**. Pengguna bertanggung jawab penuh atas penggunaan tool ini.

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
├── DummyServer/
│   └── app.js          # Server dummy untuk testing
└── README.md           # Dokumentasi ini
```

## 🚀 Instalasi

### 1. Instalasi Termux (Android)
```bash
# Download Termux dari F-Droid atau Google Play Store
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
git clone https://github.com/yourusername/ddos.git
cd ddos
```

### 5. Install Dependencies Python
```bash
# Install module yang diperlukan
pip install requests colorama psutil
```

### 6. Install Dependencies Node.js
```bash
# Masuk ke folder DummyServer
cd DummyServer

# Install express
npm init -y
npm install express

# Kembali ke folder utama
cd ..
```

## 🛠️ Cara Penggunaan

### Menjalankan Dummy Server (Testing Lokal)
```bash
# Masuk ke folder DummyServer
cd DummyServer

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
   - Jalankan `node DummyServer/app.js` di terminal pertama
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
- **GitHub**: [@riskiardiane](https://github.com/riskiardiane)

---

## English

### 📋 Description
A tool for performing stress testing and load testing on web servers. This tool comes with a dummy server for local testing purposes and attractive visualization features.

### ⚠️ Disclaimer
This tool is created for **educational and testing purposes** only. Using it to attack servers without permission is **illegal**. Users are fully responsible for the use of this tool.

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
├── DummyServer/
│   └── app.js          # Dummy server for testing
└── README.md           # This documentation
```

## 🚀 Installation

### 1. Install Termux (Android)
```bash
# Download Termux from F-Droid or Google Play Store
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
git clone https://github.com/yourusername/ddos.git
cd ddos
```

### 5. Install Python Dependencies
```bash
# Install required modules
pip install requests colorama psutil
```

### 6. Install Node.js Dependencies
```bash
# Enter DummyServer folder
cd DummyServer

# Install express
npm init -y
npm install express

# Return to main folder
cd ..
```

## 🛠️ Usage

### Running Dummy Server (Local Testing)
```bash
# Enter DummyServer folder
cd DummyServer

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
   - Run `node DummyServer/app.js` in first terminal
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
- **GitHub**: [@riskiardiane](https://github.com/riskiardiane)

---

## 🚨 Legal Notice / Pemberitahuan Hukum

**English**: This tool is strictly for educational and authorized testing purposes only. Any misuse of this tool for illegal activities is prohibited and not the responsibility of the author.

**Indonesia**: Tool ini hanya untuk tujuan edukasi dan testing yang diotorisasi. Segala penyalahgunaan tool ini untuk aktivitas ilegal dilarang dan bukan tanggung jawab pembuat.

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

**Made with ❤️ by Riski Ardiane**
