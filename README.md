# 🧠 PDV Vision - AI视觉导盲助手 | AI Visual Guide for the Visually Impaired

**PDV Vision** 是一款结合 AI 图像识别、语音播报与模式切换的导盲助手应用，专为视障用户设计，助力他们更安全、自主地探索环境。  
**PDV Vision** is an AI-powered assistant that uses image recognition and speech to help visually impaired users navigate their surroundings with greater confidence.

## 🌟 功能特点 | Features

- 📷 **图像识别**  
  使用 YOLOv5 和 GPT-4o 模型识别物体并生成中文或英文描述  
  Object detection and smart image captioning via YOLOv5 + GPT-4o

- 🗣️ **语音播报**  
  自动朗读识别内容，支持中英文语音提示  
  Real-time TTS speech output in Chinese and English

- 📍 **定位支持**  
  根据模式决定是否启用 GPS 定位功能  
  Location-aware feedback depending on selected mode

- 🧭 **三种模式支持**  
  三种使用模式优化语音交互与识别重点：  
  Three operational modes to optimize recognition and feedback:
  - **户外模式 Outdoor Mode**：识别道路、障碍物、红绿灯等  
    Detects streets, obstacles, traffic lights
  - **室内模式 Indoor Mode**：识别洗手间、出入口、门等  
    Detects restrooms, doors, entrances/exits
  - **普通模式 Normal Mode**：常规识别与播报  
    General-purpose recognition and narration

## 🔧 技术栈 | Tech Stack

- **前端客户端 Frontend**：Basic4Android (B4A)  
- **后端服务器 Backend**：Flask + YOLOv5 + OpenAI GPT-4o  
- **部署平台 Hosting**：支持本地与云部署（如 Render）

## 🚀 快速开始 | Getting Started

### 📦 安装后端 | Backend Setup

```bash
git clone https://github.com/pandavio/vision-server.git
cd pdv-vision-server
pip install -r requirements.txt
python app.py
```

### 📱 部署客户端 | Android App Setup

- 使用 B4A 打开 `PDVVision.b4a` 项目
- 修改 `Starter.ServerURL` 为你的服务器地址
- 编译并安装至 Android 手机

## 📂 项目结构 | Project Structure

```bash
PDVVision/
├── B4A/              # Android 客户端代码 / Android app (B4A)
├── server/           # Flask 后端 / Backend server
├── README.md
├── requirements.txt
```

## 📜 开源协议 | License

本项目基于 MIT 协议开源。  
This project is licensed under the MIT License.
