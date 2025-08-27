# Inclusion Criteria

This document outlines the scope and inclusion criteria for the Linux Speech-to-Text and Voice Assistants repository index.

## Project Focus

This repository focuses on **modern ASR (Automatic Speech Recognition)** projects that are:
- Currently being developed or prototyped
- Released within the last few years
- Part of the current wave of AI-accelerated speech technology

## Historical Context

The repository excludes the prior wave of STT tools on Linux that existed before the widespread acceleration in the AI market pioneered by **OpenAI Whisper** and similar breakthrough models. We focus on projects that have integrated modern ASR capabilities, including local Whisper implementations, over traditional and usually inferior STT solutions.

## In Scope

### Speech-to-Text (STT) Tools
- Real-time and asynchronous transcription tools
- GUI and CLI applications for speech recognition
- Local/offline STT implementations
- Cloud STT integrations and interfaces
- STT tools with post-processing capabilities

### STT Assistants
Speech-to-text AI appliances or interfaces that allow for tool execution, including:
- Voice command systems
- Voice-controlled desktop applications
- Terminal voice interfaces
- Voice-to-action automation tools

### Models and Training
- Pre-trained STT models (Whisper, Vosk, etc.)
- Model fine-tuning and training tools
- Model optimization utilities

### Development Tools
- STT APIs and services
- Development frameworks for voice applications
- Audio processing tools specifically for STT workflows

## Out of Scope

### Excluded Technologies
- **TTS (Text-to-Speech) tools** - This repository focuses exclusively on STT
- **Voice cloning tools** - Outside the scope of speech recognition
- **General audio processing** - Only STT-specific audio tools are included

### Project Categories
The repository organizes projects into distinct sections:
1. **STT Tools** - Direct speech-to-text applications
2. **STT Assistants** - Voice command and automation systems
3. **Models** - Pre-trained models and training resources

## Deployment Preferences

### Self-Hosted vs Cloud
Many Linux users prefer **self-hosted models** for privacy and control, using tools for STT inference on-device. However, **cloud STT services** remain viable due to their affordability and performance.

**Both deployment types are included** within the repository scope:
- **Local/On-Device**: Whisper implementations, local model runners
- **Cloud Integration**: CLI/GUI tools that interface with cloud STT APIs

### Hardware Considerations
Projects are evaluated for their compatibility with common Linux hardware configurations, including:
- CPU-only systems
- NVIDIA GPU systems (CUDA)
- AMD GPU systems (ROCm)
- Various memory constraints

## Quality Standards

### Project Maturity
- Active development or recent updates preferred
- Functional implementations over proof-of-concepts (though POCs are included in separate sections)
- Clear documentation and installation instructions

### Linux Compatibility
- Native Linux support required
- Cross-platform tools acceptable if Linux is well-supported
- Distribution-agnostic preferred, but distro-specific tools included if valuable

## Repository Structure

Projects are categorized by:
- **Functionality** (GUI, CLI, API, etc.)
- **Maturity Level** (Production, Beta, Proof-of-Concept)
- **Deployment Type** (Local, Cloud, Hybrid)
- **Use Case** (General STT, Voice Commands, Development)

---

*This document is part of the [Linux STT and Voice Assistants](README.md) repository index.*
