#!/usr/bin/env python3
"""
Build script to inject section content into README template.
Usage: python build-readme.py
"""

import os
import re

def inject_sections():
    """Read template and inject section files into placeholders."""
    
    # Read the template
    with open('README.template.md', 'r') as f:
        template = f.read()
    
    # Find all injection placeholders
    pattern = r'\{\{INJECT:([^}]+)\}\}'
    matches = re.findall(pattern, template)
    
    # Replace each placeholder with file content
    for section_file in matches:
        if os.path.exists(section_file):
            with open(section_file, 'r') as f:
                content = f.read().strip()
            
            # Replace the placeholder
            placeholder = f'{{{{INJECT:{section_file}}}}}'
            template = template.replace(placeholder, content)
            print(f"✓ Injected {section_file}")
        else:
            print(f"✗ Warning: {section_file} not found")
    
    # Write the final README
    with open('README.md', 'w') as f:
        f.write(template)
    
    print("✓ README.md generated successfully")

if __name__ == '__main__':
    inject_sections()
