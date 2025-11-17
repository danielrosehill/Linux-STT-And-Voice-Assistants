---
description: Update repository statistics and badges
tags: [maintenance, stats]
---

# Update Repository Statistics

Update all dynamic statistics and badges in the README.md:

1. **Update header badges**:
   - Last Updated date (set to today's date)
   - Resources count (count total projects in README)
   - Verify license badge is current

2. **Update "Largest Projects" section**:
   - Fetch current star counts for all projects
   - Re-sort by star count
   - Update the table with current stars
   - Add any new projects that have crossed 1000+ stars

3. **Verify badge URLs** are working:
   - Star count badges
   - Last commit badges
   - Any custom badges

4. **Update star counts** for projects in tables (optional, can be selective):
   - Focus on high-visibility sections
   - Update projects that may have changed significantly

Use the Hugging Face MCP or direct GitHub API calls to fetch accurate, current data.

Output a summary of changes made.
