---
description: Audit all project links for 404s and archive status
tags: [maintenance, quality]
---

# Audit Project Links

Check all GitHub repository links in README.md for availability and status.

**Process:**

1. **Extract all GitHub URLs** from README.md

2. **For each repository, check**:
   - Is it still accessible (not 404)?
   - Is it archived?
   - Has it been renamed/moved?
   - Last commit date (flag if >2 years old)

3. **Categorize findings**:
   - ✅ Active and maintained
   - ⚠️ Stale (no commits in 2+ years)
   - 📦 Archived
   - ❌ Not found (404)
   - 🔄 Moved/renamed

4. **Generate report** with:
   - Summary statistics
   - List of problematic links
   - Suggested actions (remove, update, mark as archived)

5. **Suggest README updates**:
   - Add "archived" notes to relevant entries
   - Remove 404'd projects
   - Update renamed repository URLs

Present findings without making changes - await approval for modifications.
