# Linux Speech-to-Text and Voice Assistants

Point in time snapshot index of speech-to-text repositories and voice assistant tools for Linux, compiled on August 27, 2025.

## Getting Started

**New to Linux STT?** 

Check out our [Getting Started Guide](starting-points.md) for step-by-step setup instructions, hardware recommendations, and model selection guidance.

## Table of Contents

- [Getting Started](#getting-started)
- [Inclusion Criteria](#inclusion-criteria)
- [Search Terms](#search-terms)
- [STT Tools](#stt-tools)
  - [GUI Applications](#gui-applications)
  - [CLI Tools](#cli-tools)
  - [STT with Post-processing](#stt-with-post-processing)
- [Voice Assistants](#voice-assistants)
- [Models](#models)
  - [Whisper](#whisper)
- [Developer Tools](#developer-tools)

---

## Inclusion Criteria

This repository focuses on modern ASR projects from the current AI-accelerated era, excluding pre-Whisper legacy STT tools. For detailed scope information, see our [Inclusion Criteria](inclusion-criteria.md) page.

---

## Search Terms

STT and voice tech is fast evolving. These search terms were used to assist in compiling this list:

- STT
- Linux ASR  
- Linux Whisper apps

This index is (highly!) non-exhaustive. 

---

## STT Tools

### GUI Applications

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [![dsnote](https://img.shields.io/github/stars/mkiol/dsnote?style=flat-square)](https://github.com/mkiol/dsnote) | ![Stars](https://img.shields.io/github/stars/mkiol/dsnote?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/mkiol/dsnote?style=flat-square) | Speech note-taking application |
| [![whisply](https://img.shields.io/github/stars/tsmdt/whisply?style=flat-square)](https://github.com/tsmdt/whisply) | ![Stars](https://img.shields.io/github/stars/tsmdt/whisply?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/tsmdt/whisply?style=flat-square) | Whisper-based transcription tool |
| [![whisper-to-input-desktop](https://img.shields.io/github/stars/Rosbifbr/whisper-to-input-desktop?style=flat-square)](https://github.com/Rosbifbr/whisper-to-input-desktop) | ![Stars](https://img.shields.io/github/stars/Rosbifbr/whisper-to-input-desktop?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Rosbifbr/whisper-to-input-desktop?style=flat-square) | Desktop input via Whisper |
| [![maVoice-Linux](https://img.shields.io/github/stars/lliWcWill/maVoice-Linux?style=flat-square)](https://github.com/lliWcWill/maVoice-Linux) | ![Stars](https://img.shields.io/github/stars/lliWcWill/maVoice-Linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/lliWcWill/maVoice-Linux?style=flat-square) | Voice control for Linux |

### CLI Tools

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [![whispertux](https://img.shields.io/github/stars/cjams/whispertux?style=flat-square)](https://github.com/cjams/whispertux) | ![Stars](https://img.shields.io/github/stars/cjams/whispertux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/cjams/whispertux?style=flat-square) | Whisper CLI for Linux |
| [![whispertrigger](https://img.shields.io/github/stars/RetroTrigger/whispertrigger?style=flat-square)](https://github.com/RetroTrigger/whispertrigger) | ![Stars](https://img.shields.io/github/stars/RetroTrigger/whispertrigger?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/RetroTrigger/whispertrigger?style=flat-square) | Trigger-based Whisper tool |
| [![BlahST](https://img.shields.io/github/stars/QuantiusBenignus/BlahST?style=flat-square)](https://github.com/QuantiusBenignus/BlahST) | ![Stars](https://img.shields.io/github/stars/QuantiusBenignus/BlahST?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/QuantiusBenignus/BlahST?style=flat-square) | Speech-to-text CLI tool |
| [![whisprd](https://img.shields.io/github/stars/AgenticToaster/whisprd?style=flat-square)](https://github.com/AgenticToaster/whisprd) | ![Stars](https://img.shields.io/github/stars/AgenticToaster/whisprd?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/AgenticToaster/whisprd?style=flat-square) | Whisper daemon |
| [![froshine](https://img.shields.io/github/stars/AdrianScott/froshine?style=flat-square)](https://github.com/AdrianScott/froshine) | ![Stars](https://img.shields.io/github/stars/AdrianScott/froshine?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/AdrianScott/froshine?style=flat-square) | Voice recognition tool |
| [![whisper-hotkey-linux](https://img.shields.io/github/stars/atkvishnu/whisper-hotkey-linux?style=flat-square)](https://github.com/atkvishnu/whisper-hotkey-linux) | ![Stars](https://img.shields.io/github/stars/atkvishnu/whisper-hotkey-linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/atkvishnu/whisper-hotkey-linux?style=flat-square) | Hotkey-triggered Whisper |
| [![WhisperHelper](https://img.shields.io/github/stars/nacmonad/WhisperHelper?style=flat-square)](https://github.com/nacmonad/WhisperHelper) | ![Stars](https://img.shields.io/github/stars/nacmonad/WhisperHelper?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/nacmonad/WhisperHelper?style=flat-square) | Whisper helper utility |
| [![voice2chatgpt](https://img.shields.io/github/stars/RemiFabre/voice2chatgpt?style=flat-square)](https://github.com/RemiFabre/voice2chatgpt) | ![Stars](https://img.shields.io/github/stars/RemiFabre/voice2chatgpt?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/RemiFabre/voice2chatgpt?style=flat-square) | Voice to ChatGPT interface |
| [![nerd-dictation](https://img.shields.io/github/stars/ideasman42/nerd-dictation?style=flat-square)](https://github.com/ideasman42/nerd-dictation) | ![Stars](https://img.shields.io/github/stars/ideasman42/nerd-dictation?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/ideasman42/nerd-dictation?style=flat-square) | Simple offline speech to text for desktop Linux |

### STT with Post-processing

Tools that leverage Whisper etc for STT but also add a layer for text cleanup after initial transcription:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [![Whisper-Notepad-For-Linux](https://img.shields.io/github/stars/danielrosehill/Whisper-Notepad-For-Linux?style=flat-square)](https://github.com/danielrosehill/Whisper-Notepad-For-Linux) | ![Stars](https://img.shields.io/github/stars/danielrosehill/Whisper-Notepad-For-Linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/danielrosehill/Whisper-Notepad-For-Linux?style=flat-square) | Whisper notepad with post-processing |
| [![Thought-Pad](https://img.shields.io/github/stars/danielrosehill/Thought-Pad?style=flat-square)](https://github.com/danielrosehill/Thought-Pad) | ![Stars](https://img.shields.io/github/stars/danielrosehill/Thought-Pad?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/danielrosehill/Thought-Pad?style=flat-square) | Thought capture with STT |

---

## Voice Assistants

Convert voice into commands on services including terminal directly or into specific formats:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [![Local-Voice](https://img.shields.io/github/stars/shashank2122/Local-Voice?style=flat-square)](https://github.com/shashank2122/Local-Voice) | ![Stars](https://img.shields.io/github/stars/shashank2122/Local-Voice?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/shashank2122/Local-Voice?style=flat-square) | Local voice assistant |
| [![home-assistant-assist-desktop](https://img.shields.io/github/stars/timmo001/home-assistant-assist-desktop?style=flat-square)](https://github.com/timmo001/home-assistant-assist-desktop) | ![Stars](https://img.shields.io/github/stars/timmo001/home-assistant-assist-desktop?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/timmo001/home-assistant-assist-desktop?style=flat-square) | Home Assistant desktop client |
| [![vosk-cli-dictation](https://img.shields.io/github/stars/RonanDavalan/vosk-cli-dictation?style=flat-square)](https://github.com/RonanDavalan/vosk-cli-dictation) | ![Stars](https://img.shields.io/github/stars/RonanDavalan/vosk-cli-dictation?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/RonanDavalan/vosk-cli-dictation?style=flat-square) | Vosk CLI dictation |
| [![voice2json](https://img.shields.io/github/stars/synesthesiam/voice2json?style=flat-square)](https://github.com/synesthesiam/voice2json) | ![Stars](https://img.shields.io/github/stars/synesthesiam/voice2json?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/synesthesiam/voice2json?style=flat-square) | Voice to JSON converter |

---

## Models

### Whisper

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [![Whisper on Hugging Face](https://img.shields.io/badge/Hugging%20Face-Whisper-orange?style=flat-square)](https://huggingface.co/spaces/openai/whisper) | N/A | N/A | OpenAI Whisper on Hugging Face |

---

## Developer Tools

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [![whisper.cpp-cli](https://img.shields.io/github/stars/charliermarsh/whisper.cpp-cli?style=flat-square)](https://github.com/charliermarsh/whisper.cpp-cli) | ![Stars](https://img.shields.io/github/stars/charliermarsh/whisper.cpp-cli?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/charliermarsh/whisper.cpp-cli?style=flat-square) | Whisper.cpp CLI wrapper |

---
