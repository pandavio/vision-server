# 🧠 PDV Vision - AI Visual Guide for the Visually Impaired

**PDV Vision** is an AI-powered assistant that uses image recognition and speech to help visually impaired users navigate their surroundings with greater confidence.

## 🌟 Features

- 📷 **Object Detection**  
  Object detection and smart image captioning via YOLOv5 + GPT-4o

- 🗣️ **Speech Feedback**  
  Real-time TTS speech output in Chinese and English

- 📍 **Location Awareness**  
  Location-aware feedback depending on selected mode

- 🧭 **Three Operational Modes**  
  Three modes to optimize recognition and interaction:
  - **Outdoor Mode**: Detects streets, obstacles, traffic lights
  - **Indoor Mode**: Detects restrooms, doors, entrances/exits
  - **Normal Mode**: General-purpose recognition and narration

## 🔧 Tech Stack

- **Frontend**: Basic4Android (B4A)  
- **Backend**: Flask + YOLOv5 + OpenAI GPT-4o  
- **Hosting**: Supports local and cloud deployment (e.g., Render)

## 🚀 Getting Started

### 📦 Backend Setup

```bash
git clone https://github.com/pandavio/vision-server.git
cd pdv-vision-server
pip install -r requirements.txt
python app.py
```

### 📱 Android App Setup

- Open `PDVVision.b4a` with B4A
- Update `Starter.ServerURL` with your backend address
- Build and install the APK to your Android phone

## 🔑 Required API Keys

PDV Vision requires the following two API keys to function properly:

- 🧠 **OpenAI API Key**: Used to call the GPT-4o multimodal model for image understanding and natural language generation  
- 🗺️ **Google Maps API Key**: Used to retrieve GPS location and address details for enhanced outdoor navigation (used only in outdoor mode)

Before running the system, please ensure:

- **B4A Client**: Add both API keys in the corresponding sections of your Android client code  
- **Flask Backend**: Set the OpenAI API key as an environment variable or in a configuration file (e.g., `OPENAI_API_KEY`)

## 📂 Project Structure

```bash
PDVVision/
├── B4A/              # Android app (B4A)
├── server/           # Backend server (Flask)
├── README.md
├── requirements.txt
```

## 📜 License

This project is licensed under the MIT License.



# 🧠 PDV Vision - AI视觉导盲助手

**PDV Vision** 是一款结合 AI 图像识别、语音播报与模式切换的导盲助手应用，专为视障用户设计，助力他们更安全、自主地探索环境。

## 🌟 功能特点

- 📷 **图像识别**  
  使用 YOLOv5 和 GPT-4o 模型识别物体并生成中文或英文描述

- 🗣️ **语音播报**  
  自动朗读识别内容，支持中英文语音提示

- 📍 **定位支持**  
  根据模式决定是否启用 GPS 定位功能

- 🧭 **三种模式支持**  
  三种使用模式优化语音交互与识别重点：
  - **户外模式**：识别道路、障碍物、红绿灯等
  - **室内模式**：识别洗手间、出入口、门等
  - **普通模式**：常规识别与播报

## 🔧 技术栈

- **前端客户端**：Basic4Android (B4A)  
- **后端服务器**：Flask + YOLOv5 + OpenAI GPT-4o  
- **部署平台**：支持本地与云部署（如 Render）

## 🚀 快速开始

### 📦 安装后端

```bash
git clone https://github.com/pandavio/vision-server.git
cd pdv-vision-server
pip install -r requirements.txt
python app.py
```

### 📱 部署客户端

- 使用 B4A 打开 `PDVVision.b4a` 项目
- 修改 `Starter.ServerURL` 为你的服务器地址
- 编译并安装至 Android 手机

## 🔑 所需 API 密钥

PDV Vision 的运行依赖以下两个 API 密钥：

- 🧠 **OpenAI API 密钥**：用于调用 GPT-4o 多模态模型，实现图像内容理解与自然语言描述  
- 🗺️ **Google Maps API 密钥**：用于获取用户 GPS 定位与地址信息，提升户外导航体验（仅户外模式使用）

请在部署前完成以下设置：

- **B4A 客户端**：将 OpenAI 和 Google Maps 的 API 密钥配置在代码中相应位置  
- **Flask 后端**：使用环境变量或配置文件导入 OpenAI API 密钥（如 `OPENAI_API_KEY`）

## 📂 项目结构

```bash
PDVVision/
├── B4A/              # Android 客户端代码
├── server/           # Flask 后端服务器
├── README.md
├── requirements.txt
```

## 📜 开源协议

本项目基于 MIT 协议开源。
