---
description: Categorize a specific project and suggest placement
tags: [organization, analysis]
---

# Categorize Project

Given a GitHub repository URL or project name, analyze it and suggest the appropriate category.

**Process:**

1. **Fetch repository information**:
   - Description
   - README content (scan for key features)
   - Language/framework
   - Star count and last commit date

2. **Analyze project characteristics**:
   - Is it GUI, CLI, or Web UI?
   - Real-time or async transcription?
   - Local inference, cloud, or hybrid?
   - Pure STT or voice assistant?
   - Special features (Wayland support, MCP, etc.)

3. **Suggest category placement**:
   - Primary category (e.g., "STT Tools - GUIs")
   - Alternative categories if applicable
   - Whether it fits "Largest Projects" section

4. **Draft the table entry** with:
   - Formatted markdown
   - Badge URLs
   - Accurate description
   - Any special notes (Wayland support, etc.)

5. **Note if the project is already in README** to avoid duplicates

Present findings and await confirmation before adding to README.
