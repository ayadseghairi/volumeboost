
# 🎵 VolumeBoost - Boost Your Sound on Linux! 🔊

VolumeBoost is a simple GUI application built with **CustomTkinter**, allowing you to increase your system volume up to **200%** easily! 🚀

## 📌 Features
✅ Smooth volume control via **slider**  
✅ Quick **increase/decrease** buttons  
✅ Uses **pactl** to amplify sound beyond 100%  
✅ Modern dark-mode GUI with **CustomTkinter** 🌙  

---

## 📥 Installation & Usage

### 🔽 **1. Install via AUR (`yay`)**:
For Arch Linux users, install it easily with:
```bash
yay -S volumeboost
```

### 🖥️ **2. Run the Application**
1️⃣ **From the application menu** (Look for "Volume Boost")  
2️⃣ **Using the terminal**:  
```bash
volumeboost
```

---

## 🔨 Manual Installation (For Other Linux Distros)

### **1️⃣ Install Dependencies**
Ensure **Python** and required libraries are installed:
```bash
pip install customtkinter
```

### **2️⃣ Run the App**
Clone the repository and execute:
```bash
git clone https://github.com/ayadseghairi/volumeboost.git
cd volumeboost
python main.py
```

---

## 📷 **Screenshots**
![VolumeBoost Screenshot](https://github.com/ayadseghairi/volumeboost/blob/main/Screenshot.png)

---

## ⚙️ **Building an Executable (`.exe` or Linux Binary)**
### **🔧 Create a Standalone Executable on Linux**
```bash
pyinstaller --onefile --noconsole --name volumeboost main.py
```
- The final executable will be in the **`dist/volumeboost`** folder.  
- Make it executable and run:
  ```bash
  chmod +x dist/volumeboost
  ./dist/volumeboost
  ```

---

## 📜 **License**
📝 **This project is licensed under the MIT License** - You are free to use and modify it!  
👤 **Developer:** [Ayad Seghairi](https://github.com/ayadseghairi)

---

## 🚀 **Contributing**
✨ If you’d like to improve the app, feel free to submit a **Pull Request** or report issues in the **Issues** section!

🎯 **GitHub Repo:** [VolumeBoost on GitHub](https://github.com/ayadseghairi/volumeboost)
