---
description: Check for duplicate projects in the repository
tags: [maintenance, cleanup]
---

# Check for Duplicate Projects

Scan the README.md for duplicate project entries.

**Process:**

1. **Extract all project URLs** from README.md
2. **Identify duplicates**:
   - Same repository URL in multiple sections
   - Similar names that might be the same project
   - Forks vs original repos

3. **For each duplicate found**:
   - List which sections it appears in
   - Note any differences in description or categorization
   - Suggest which entry to keep (usually the more detailed one)

4. **Report findings** with:
   - Total duplicates found
   - Recommended actions
   - Projects that appear intentionally in multiple sections (if applicable)

Do not automatically remove duplicates - present findings for review first.
