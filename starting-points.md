# Getting Started with Speech-to-Text on Linux

This guide provides recommendations for newcomers to speech-to-text (STT) on Linux. Follow these steps to set up a robust STT environment and find the right tools for your hardware.

## Prerequisites

### 1. Install Conda

Start by installing Conda (Miniconda or Anaconda) for Python environment management:

```bash
# Download Miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Install
bash Miniconda3-latest-Linux-x86_64.sh

# Restart your terminal or source your bashrc
source ~/.bashrc
```

### 2. Verify GPU Setup

Ensure your GPU is properly configured for AI workloads:

**For NVIDIA GPUs (CUDA):**
```bash
nvidia-smi
nvcc --version
```

**For AMD GPUs (ROCm):**
```bash
rocm-smi
hipcc --version
```

If you need to set up CUDA or ROCm support, refer to the official documentation for your distribution.

## Quick Start Recommendation: DSNote

DSNote is a great jumping off point to explore a) whether local STT is viable on your hardware; b) getting a sense for how it compares to cloud STT and c) ... it provides an excellent interface for downloading locally deployable STT (and TTS) models.

[![DSNote](https://img.shields.io/github/stars/mkiol/dsnote?style=flat-square)](https://github.com/mkiol/dsnote)

DSNote offers:
- Easy-to-use graphical interface
- Multiple STT engine support
- Good hardware compatibility
- Active development and community

## Setting Up Your STT Environment

### 1. Create a Dedicated Environment

```bash
# Create a new conda environment for STT work
conda create -n stt-env python=3.10
conda activate stt-env
```

### 2. Install Whisper and Dependencies

```bash
# Install OpenAI Whisper
pip install openai-whisper

# Install additional useful packages
pip install torch torchaudio
pip install faster-whisper  # More efficient implementation
```

### 3. Download and Test Whisper Models

Start by downloading different Whisper model sizes to test on your hardware:

```bash
# Test with different model sizes (from smallest to largest)
whisper --model tiny audio_file.wav
whisper --model base audio_file.wav  
whisper --model small audio_file.wav
whisper --model medium audio_file.wav
whisper --model large audio_file.wav
```

## Model Selection Guidelines

Choose your Whisper model based on your hardware capabilities:

| Model | Size | VRAM Usage | Speed | Accuracy |
|-------|------|------------|-------|----------|
| `tiny` | 39 MB | ~1 GB | Fastest | Basic |
| `base` | 74 MB | ~1 GB | Fast | Good |
| `small` | 244 MB | ~2 GB | Medium | Better |
| `medium` | 769 MB | ~5 GB | Slower | Very Good |
| `large` | 1550 MB | ~10 GB | Slowest | Best |

**Recommendation:** Start with `base` or `small` models, then scale up if your hardware can handle it.

## Hardware Considerations

- **CPU-only systems:** Use `tiny` or `base` models
- **8GB+ GPU:** Can handle `medium` models comfortably  
- **16GB+ GPU:** Can run `large` models efficiently
- **Limited RAM:** Consider `faster-whisper` for better memory efficiency

## Next Steps

1. **Experiment with different models** until you find the right balance of speed/accuracy for your use case
2. **Try GUI applications** like DSNote for daily use
3. **Explore CLI tools** for automation and scripting
4. **Set up hotkeys** for quick voice input using tools from our repository index
5. **Consider post-processing** tools if you need text cleanup after transcription

## Troubleshooting

- **Poor accuracy:** Try a larger model or check your audio quality
- **Slow performance:** Use a smaller model or enable GPU acceleration
- **Memory issues:** Use `faster-whisper` or reduce model size
- **Audio input problems:** Check your microphone settings and permissions

## Additional Resources

- [Main Repository Index](README.md) - Browse all available STT tools
- [Whisper Documentation](https://github.com/openai/whisper) - Official Whisper docs
- [DSNote Documentation](https://github.com/mkiol/dsnote) - GUI application guide


