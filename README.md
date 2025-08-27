# Linux Speech-to-Text and Voice Assistants

## Point in time snapshot, August 27th, 2028

![Last Updated](https://img.shields.io/badge/Last%20Updated-August%2027%2C%202025-blue?style=flat-square)
![Repository Type](https://img.shields.io/badge/Type-Index-green?style=flat-square)
![Resources](https://img.shields.io/badge/Resources-100%2B-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

Point in time snapshot index of speech-to-text repositories and voice assistant tools for Linux, compiled on August 27, 2025.

## Inclusion Criteria

| Scope | Category | Description |
|-------|----------|-------------|
| ✅ In Scope | STT | Speech-to-text tools and applications |
| ✅ In Scope | Voice Assistants | Voice-controlled assistant applications |
| ✅ In Scope | Voice-to-X | Voice-to-MCP, voice-to-commands, and similar tools |
| ❌ Out of Scope | TTS | Text-to-speech synthesis tools |
| ❌ Out of Scope | TTS Applications | Voice cloning and other TTS applications |

## Largest Projects (1000+ Stars)

The most popular repositories in this collection, sorted by star count:

| Repository | Stars | Description | Language |
|------------|-------|-------------|----------|
| [**nerd-dictation**](https://github.com/ideasman42/nerd-dictation) | ![Stars](https://img.shields.io/github/stars/ideasman42/nerd-dictation?style=flat-square) | Simple, hackable offline speech to text - using the VOSK-API. | Python |
| [**dsnote**](https://github.com/mkiol/dsnote) | ![Stars](https://img.shields.io/github/stars/mkiol/dsnote?style=flat-square) | Speech Note Linux app. Note taking, reading and translating with offline Speech to Text, Text to Speech and Machine translation. | C++ |

---

## Getting Started

**New to Linux STT?** 

Check out [Getting Started Guide](starting-points.md) for step-by-step setup instructions, hardware recommendations, and model selection guidance.

## Table of Contents

- [Inclusion Criteria](#inclusion-criteria)
- [Largest Projects (1000+ Stars)](#largest-projects-1000-stars)
- [Getting Started](#getting-started)
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

## Speech-to-Text - Real Time

### GUIs

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**dsnote**](https://github.com/mkiol/dsnote) | ![Stars](https://img.shields.io/github/stars/mkiol/dsnote?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/mkiol/dsnote?style=flat-square) | Speech Note Linux app. Note taking, reading and translating with offline Speech to Text, Text to Speech and Machine translation. |
| [**whisply**](https://github.com/tsmdt/whisply) | ![Stars](https://img.shields.io/github/stars/tsmdt/whisply?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/tsmdt/whisply?style=flat-square) | A simple GUI for OpenAI Whisper |
| [**whisper-to-input-desktop**](https://github.com/Rosbifbr/whisper-to-input-desktop) | ![Stars](https://img.shields.io/github/stars/Rosbifbr/whisper-to-input-desktop?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Rosbifbr/whisper-to-input-desktop?style=flat-square) | A simple desktop application that uses OpenAI's Whisper to transcribe audio and input it as text |
| [**maVoice-Linux**](https://github.com/lliWcWill/maVoice-Linux) | ![Stars](https://img.shields.io/github/stars/lliWcWill/maVoice-Linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/lliWcWill/maVoice-Linux?style=flat-square) | Voice control for Linux |

### CLIs

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**whispertux**](https://github.com/cjams/whispertux) | ![Stars](https://img.shields.io/github/stars/cjams/whispertux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/cjams/whispertux?style=flat-square) | A simple CLI wrapper for OpenAI's Whisper speech-to-text model |
| [**whispertrigger**](https://github.com/RetroTrigger/whispertrigger) | ![Stars](https://img.shields.io/github/stars/RetroTrigger/whispertrigger?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/RetroTrigger/whispertrigger?style=flat-square) | A simple script to trigger OpenAI Whisper with a hotkey |
| [**BlahST**](https://github.com/QuantiusBenignus/BlahST) | ![Stars](https://img.shields.io/github/stars/QuantiusBenignus/BlahST?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/QuantiusBenignus/BlahST?style=flat-square) | Offline, real-time, streaming speech-to-text transcription using OpenAI Whisper |
| [**whisprd**](https://github.com/AgenticToaster/whisprd) | ![Stars](https://img.shields.io/github/stars/AgenticToaster/whisprd?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/AgenticToaster/whisprd?style=flat-square) | A daemon for OpenAI Whisper |
| [**froshine**](https://github.com/AdrianScott/froshine) | ![Stars](https://img.shields.io/github/stars/AdrianScott/froshine?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/AdrianScott/froshine?style=flat-square) | Voice recognition tool |
| [**whisper-hotkey-linux**](https://github.com/atkvishnu/whisper-hotkey-linux) | ![Stars](https://img.shields.io/github/stars/atkvishnu/whisper-hotkey-linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/atkvishnu/whisper-hotkey-linux?style=flat-square) | Whisper hotkey for Linux |
| [**WhisperHelper**](https://github.com/nacmonad/WhisperHelper) | ![Stars](https://img.shields.io/github/stars/nacmonad/WhisperHelper?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/nacmonad/WhisperHelper?style=flat-square) | A simple GUI for OpenAI Whisper |
| [**voice2chatgpt**](https://github.com/RemiFabre/voice2chatgpt) | ![Stars](https://img.shields.io/github/stars/RemiFabre/voice2chatgpt?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/RemiFabre/voice2chatgpt?style=flat-square) | Voice to ChatGPT |
| [**nerd-dictation**](https://github.com/ideasman42/nerd-dictation) | ![Stars](https://img.shields.io/github/stars/ideasman42/nerd-dictation?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/ideasman42/nerd-dictation?style=flat-square) | Simple, hackable offline speech to text - using the VOSK-API. |

### Unsorted / Unreviewed

Met inclusion criteria but haven't been tested yet:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**Linux-Dictation-Project**](https://github.com/wheeler01/Linux-Dictation-Project) | ![Stars](https://img.shields.io/github/stars/wheeler01/Linux-Dictation-Project?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/wheeler01/Linux-Dictation-Project?style=flat-square) | Linux dictation project |
| [**voice-typing-linux**](https://github.com/GitJuhb/voice-typing-linux) | ![Stars](https://img.shields.io/github/stars/GitJuhb/voice-typing-linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/GitJuhb/voice-typing-linux?style=flat-square) | Voice typing for Linux |
| [**LinuxWhisper**](https://github.com/vitali87/LinuxWhisper) | ![Stars](https://img.shields.io/github/stars/vitali87/LinuxWhisper?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/vitali87/LinuxWhisper?style=flat-square) | Whisper for Linux |
| [**WhisperNow**](https://github.com/shinglyu/WhisperNow) | ![Stars](https://img.shields.io/github/stars/shinglyu/WhisperNow?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/shinglyu/WhisperNow?style=flat-square) | Real-time Whisper transcription |
| [**whisper-ui**](https://github.com/schnoddelbotz/whisper-ui) | ![Stars](https://img.shields.io/github/stars/schnoddelbotz/whisper-ui?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/schnoddelbotz/whisper-ui?style=flat-square) | Whisper UI interface |
| [**whisperer**](https://github.com/mike-cr/whisperer) | ![Stars](https://img.shields.io/github/stars/mike-cr/whisperer?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/mike-cr/whisperer?style=flat-square) | Whisper-based tool |
| [**mint-whisper**](https://github.com/codankra/mint-whisper) | ![Stars](https://img.shields.io/github/stars/codankra/mint-whisper?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/codankra/mint-whisper?style=flat-square) | Whisper for Linux Mint |
| [**whisper-toggle**](https://github.com/bradjmsu/whisper-toggle) | ![Stars](https://img.shields.io/github/stars/bradjmsu/whisper-toggle?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/bradjmsu/whisper-toggle?style=flat-square) | Toggle-based Whisper control |
| [**whisper-transcribe**](https://github.com/geraschenko/whisper-transcribe) | ![Stars](https://img.shields.io/github/stars/geraschenko/whisper-transcribe?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/geraschenko/whisper-transcribe?style=flat-square) | Whisper transcription tool |
| [**handsfree**](https://github.com/achyudh/handsfree) | ![Stars](https://img.shields.io/github/stars/achyudh/handsfree?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/achyudh/handsfree?style=flat-square) | Hands-free computing |
| [**dictation-service**](https://github.com/sanastasiou/dictation-service) | ![Stars](https://img.shields.io/github/stars/sanastasiou/dictation-service?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/sanastasiou/dictation-service?style=flat-square) | Dictation service |
| [**transcribeAnywhere**](https://github.com/naren200/transcribeAnywhere) | ![Stars](https://img.shields.io/github/stars/naren200/transcribeAnywhere?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/naren200/transcribeAnywhere?style=flat-square) | Universal transcription tool |
| [**TermlAi**](https://github.com/rohitkr150015/TermlAi) | ![Stars](https://img.shields.io/github/stars/rohitkr150015/TermlAi?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/rohitkr150015/TermlAi?style=flat-square) | Terminal AI assistant |

### STT with Post-processing

Tools that leverage Whisper etc for STT but also add a layer for text cleanup after initial transcription:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**Whisper-Notepad-For-Linux**](https://github.com/danielrosehill/Whisper-Notepad-For-Linux) | ![Stars](https://img.shields.io/github/stars/danielrosehill/Whisper-Notepad-For-Linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/danielrosehill/Whisper-Notepad-For-Linux?style=flat-square) | Whisper notepad with post-processing |
| [**Thought-Pad**](https://github.com/danielrosehill/Thought-Pad) | ![Stars](https://img.shields.io/github/stars/danielrosehill/Thought-Pad?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/danielrosehill/Thought-Pad?style=flat-square) | Thought capture with STT |

### Proof of Concepts

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**whisperai**](https://github.com/jorgecastro05/whisperai) | ![Stars](https://img.shields.io/github/stars/jorgecastro05/whisperai?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/jorgecastro05/whisperai?style=flat-square) | Whisper AI proof of concept |
| [**stt-linux**](https://github.com/samcole8/stt-linux) | ![Stars](https://img.shields.io/github/stars/samcole8/stt-linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/samcole8/stt-linux?style=flat-square) | STT Linux proof of concept |

### General STT Tools

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**linux-stt-input**](https://github.com/fengwk/linux-stt-input) | ![Stars](https://img.shields.io/github/stars/fengwk/linux-stt-input?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/fengwk/linux-stt-input?style=flat-square) | Linux STT input method |
| [**sonori**](https://github.com/0xPD33/sonori) | ![Stars](https://img.shields.io/github/stars/0xPD33/sonori?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/0xPD33/sonori?style=flat-square) | Voice recognition tool |
| [**stt-linux**](https://github.com/afif-malghani/stt-linux) | ![Stars](https://img.shields.io/github/stars/afif-malghani/stt-linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/afif-malghani/stt-linux?style=flat-square) | STT for Linux |
| [**super-stt**](https://github.com/jorge-menjivar/super-stt) | ![Stars](https://img.shields.io/github/stars/jorge-menjivar/super-stt?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/jorge-menjivar/super-stt?style=flat-square) | Enhanced STT tool |
| [**wvcr**](https://github.com/bakeryproducts/wvcr) | ![Stars](https://img.shields.io/github/stars/bakeryproducts/wvcr?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/bakeryproducts/wvcr?style=flat-square) | Wave voice control recorder |

## Vendor Projects

### Deepgram

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**fortuna**](https://github.com/deepgram-devs/fortuna) | ![Stars](https://img.shields.io/github/stars/deepgram-devs/fortuna?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/deepgram-devs/fortuna?style=flat-square) | Deepgram Fortuna project |
| [**voice-keyboard-linux**](https://github.com/deepgram/voice-keyboard-linux) | ![Stars](https://img.shields.io/github/stars/deepgram/voice-keyboard-linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/deepgram/voice-keyboard-linux?style=flat-square) | Deepgram voice keyboard |

### Small Repositories

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**STT-Assistant-linux**](https://github.com/4lext/STT-Assistant-linux) | ![Stars](https://img.shields.io/github/stars/4lext/STT-Assistant-linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/4lext/STT-Assistant-linux?style=flat-square) | STT assistant for Linux |
| [**voicekeyboard**](https://github.com/sam1am/voicekeyboard) | ![Stars](https://img.shields.io/github/stars/sam1am/voicekeyboard?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/sam1am/voicekeyboard?style=flat-square) | Voice keyboard implementation |

---

## Speech-to-Text - Asynchronous

*Section placeholder - repositories to be added*

---

## Voice Assistants

Convert voice into commands on services including terminal directly or into specific formats:

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**Local-Voice**](https://github.com/shashank2122/Local-Voice) | ![Stars](https://img.shields.io/github/stars/shashank2122/Local-Voice?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/shashank2122/Local-Voice?style=flat-square) | Local voice assistant |
| [**home-assistant-assist-desktop**](https://github.com/timmo001/home-assistant-assist-desktop) | ![Stars](https://img.shields.io/github/stars/timmo001/home-assistant-assist-desktop?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/timmo001/home-assistant-assist-desktop?style=flat-square) | Home Assistant desktop client |
| [**vosk-cli-dictation**](https://github.com/RonanDavalan/vosk-cli-dictation) | ![Stars](https://img.shields.io/github/stars/RonanDavalan/vosk-cli-dictation?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/RonanDavalan/vosk-cli-dictation?style=flat-square) | Vosk CLI dictation |
| [**voice2json**](https://github.com/synesthesiam/voice2json) | ![Stars](https://img.shields.io/github/stars/synesthesiam/voice2json?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/synesthesiam/voice2json?style=flat-square) | Voice to JSON converter |

---

## Developer Tools

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**whisper.cpp-cli**](https://github.com/charliermarsh/whisper.cpp-cli) | ![Stars](https://img.shields.io/github/stars/charliermarsh/whisper.cpp-cli?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/charliermarsh/whisper.cpp-cli?style=flat-square) | Whisper.cpp CLI wrapper |

---

## Subtitle Generation

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**whisper-subs**](https://github.com/GhostNaN/whisper-subs) | ![Stars](https://img.shields.io/github/stars/GhostNaN/whisper-subs?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/GhostNaN/whisper-subs?style=flat-square) | Whisper subtitle generation |
| [**auto-subs**](https://github.com/tmoroney/auto-subs) | ![Stars](https://img.shields.io/github/stars/tmoroney/auto-subs?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/tmoroney/auto-subs?style=flat-square) | Automatic subtitle generation |

---

## API Services

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**whisper-fastapi**](https://github.com/heimoshuiyu/whisper-fastapi) | ![Stars](https://img.shields.io/github/stars/heimoshuiyu/whisper-fastapi?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/heimoshuiyu/whisper-fastapi?style=flat-square) | Whisper FastAPI service |

---

## Models

### Whisper

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**Whisper on Hugging Face**](https://huggingface.co/spaces/openai/whisper) | N/A | N/A | OpenAI Whisper on Hugging Face |

---

## General Voice Assistants

| Repository | Stars | Last Updated | Description |
|------------|-------|--------------|-------------|
| [**linux-voice-control**](https://github.com/omegaui/linux-voice-control) | ![Stars](https://img.shields.io/github/stars/omegaui/linux-voice-control?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/omegaui/linux-voice-control?style=flat-square) | Linux voice control system |
| [**LinuxVoiceAssistant**](https://github.com/aydinnyunus/LinuxVoiceAssistant) | ![Stars](https://img.shields.io/github/stars/aydinnyunus/LinuxVoiceAssistant?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/aydinnyunus/LinuxVoiceAssistant?style=flat-square) | Linux voice assistant |
| [**Personal-Voice-Assistent**](https://github.com/Cyborgscode/Personal-Voice-Assistent) | ![Stars](https://img.shields.io/github/stars/Cyborgscode/Personal-Voice-Assistent?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/Cyborgscode/Personal-Voice-Assistent?style=flat-square) | Personal voice assistant |
| [**tempest**](https://github.com/lavafroth/tempest) | ![Stars](https://img.shields.io/github/stars/lavafroth/tempest?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/lavafroth/tempest?style=flat-square) | Voice assistant framework |
| [**jarvis_linux**](https://github.com/morrolinux/jarvis_linux) | ![Stars](https://img.shields.io/github/stars/morrolinux/jarvis_linux?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/morrolinux/jarvis_linux?style=flat-square) | Jarvis for Linux |
