---
description: Add new projects to the repository from for-ai notes
tags: [organization, update]
---

# Add Projects to Repository

Review the projects listed in `/for-ai/test.md` or provided by the user and add them to the main README.md.

For each project:

1. **Check if it already exists** in the README.md to avoid duplicates
2. **Extract metadata** using the Hugging Face MCP or GitHub API:
   - Star count (if GitHub repo)
   - Last commit date
   - Description (use repo description or infer from readme)
   - Primary language
3. **Categorize** based on:
   - Project type (GUI, CLI, Web UI, etc.)
   - Real-time vs async STT
   - Voice assistant vs pure STT
   - Specialized use case
4. **Add to the appropriate section** with proper formatting:
   ```
   | [**repo-name**](https://github.com/user/repo) | ![Stars](https://img.shields.io/github/stars/user/repo?style=flat-square) | ![Last Commit](https://img.shields.io/github/last-commit/user/repo?style=flat-square) | Description |
   ```
5. **Note any special features**:
   - Wayland support (add 🎉 emoji)
   - MCP integration
   - Local vs cloud inference
   - Notable framework (Whisper, VOSK, etc.)

After adding projects, update the "Last Updated" badge and resource count in the header.

Sort entries within each category by star count (highest first) unless there's a compelling reason not to.
