#!/usr/bin/env python3
"""
Script to fetch GitHub star counts and create a static projects-by-stars.md file
with star counts from August 27, 2025
"""

import re
import requests
import time
import os
from typing import List, Dict

def extract_github_repos_from_readme(readme_path: str) -> List[Dict[str, str]]:
    """Extract all GitHub repository URLs from README.md"""
    repos = []
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match GitHub repository links in markdown format
    github_pattern = r'\[([^\]]*)\]\(https://github\.com/([^/]+)/([^)]+)\)'
    matches = re.findall(github_pattern, content)
    
    for match in matches:
        display_name, owner, repo = match
        # Clean up repo name (remove any trailing characters)
        repo = repo.split('?')[0].split('#')[0]
        
        # Skip non-GitHub links
        if 'huggingface.co' in f"{owner}/{repo}":
            continue
            
        repos.append({
            'display_name': display_name.replace('**', ''),  # Remove bold formatting
            'owner': owner,
            'repo': repo,
            'full_name': f"{owner}/{repo}",
            'url': f"https://github.com/{owner}/{repo}"
        })
    
    return repos

def get_repo_info(owner: str, repo: str) -> Dict:
    """Fetch repository information using GitHub CLI"""
    import subprocess
    import json
    
    try:
        # Use gh CLI to fetch repo info
        cmd = ['gh', 'api', f'/repos/{owner}/{repo}']
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            data = json.loads(result.stdout)
            return {
                'stars': data.get('stargazers_count', 0),
                'description': data.get('description', ''),
                'last_updated': data.get('updated_at', ''),
                'language': data.get('language', ''),
                'archived': data.get('archived', False)
            }
        else:
            print(f"Failed to fetch {owner}/{repo}: {result.stderr.strip()}")
            return {'stars': 0, 'description': '', 'last_updated': '', 'language': '', 'archived': False}
    except Exception as e:
        print(f"Error fetching {owner}/{repo}: {e}")
        return {'stars': 0, 'description': '', 'last_updated': '', 'language': '', 'archived': False}

def main():
    readme_path = 'README.md'
    
    print("Extracting GitHub repositories from README...")
    repos = extract_github_repos_from_readme(readme_path)
    
    # Remove duplicates based on full_name
    unique_repos = {}
    for repo in repos:
        if repo['full_name'] not in unique_repos:
            unique_repos[repo['full_name']] = repo
    
    repos = list(unique_repos.values())
    print(f"Found {len(repos)} unique repositories")
    
    # Fetch star counts and info for all repos
    repo_data = []
    for i, repo in enumerate(repos):
        print(f"Fetching data for {repo['full_name']} ({i+1}/{len(repos)})")
        info = get_repo_info(repo['owner'], repo['repo'])
        
        repo_data.append({
            **repo,
            **info
        })
        
        # Small delay to avoid overwhelming the API
        time.sleep(0.2)
    
    # Sort by star count (descending)
    repo_data.sort(key=lambda x: x['stars'], reverse=True)
    
    # Generate static projects-by-stars.md
    generate_static_projects_by_stars(repo_data)
    
    print(f"\nCompleted! Top 10 repositories by stars:")
    for repo in repo_data[:10]:
        print(f"  {repo['full_name']}: {repo['stars']} stars")

def generate_static_projects_by_stars(repo_data: List[Dict]) -> None:
    """Generate static projects-by-stars.md file with star counts from August 27, 2025"""
    content = """# Projects by Stars

All repositories from the Linux STT and Voice Assistants index, sorted by GitHub star count from highest to lowest.

**Star counts as of August 27, 2025** - Static snapshot, not dynamically updated.

| Repository | Stars (Aug 27, 2025) | Description | Language |
|------------|----------------------|-------------|----------|
"""
    
    for repo in repo_data:
        # Handle empty descriptions and languages
        description = repo['description'] if repo['description'] else 'No description available'
        language = repo['language'] if repo['language'] else 'N/A'
        
        # Create repository link with proper name
        repo_name = repo['display_name'] if repo['display_name'] else repo['repo']
        repo_link = f"[**{repo_name}**]({repo['url']})"
        
        # Static star count (not a badge)
        star_count = f"{repo['stars']:,}"  # Format with commas for readability
        
        content += f"| {repo_link} | {star_count} | {description} | {language} |\n"
    
    with open('projects-by-stars.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Generated static projects-by-stars.md")

if __name__ == "__main__":
    main()
