#!/usr/bin/env python3
"""
Automated testing script for Dynatrace documentation website
Tests: links, navigation, file existence, AI integration
"""

import os
import sys
from pathlib import Path
import json

# Colors for terminal output
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

class WebsiteTester:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / 'docs'
        self.errors = []
        self.warnings = []
        self.passed = []
        
    def print_status(self, status, message):
        if status == "PASS":
            print(f"{GREEN}✅ PASS{RESET}: {message}")
            self.passed.append(message)
        elif status == "FAIL":
            print(f"{RED}❌ FAIL{RESET}: {message}")
            self.errors.append(message)
        elif status == "WARN":
            print(f"{YELLOW}⚠️  WARN{RESET}: {message}")
            self.warnings.append(message)
        else:
            print(f"{BLUE}ℹ️  INFO{RESET}: {message}")
    
    def test_file_exists(self, filepath, description):
        """Test if a file exists"""
        full_path = self.docs_dir / filepath
        if full_path.exists():
            self.print_status("PASS", f"{description}: {filepath}")
            return True
        else:
            self.print_status("FAIL", f"{description} NOT FOUND: {filepath}")
            return False
    
    def test_homepage_links(self):
        """Test all links on homepage"""
        print(f"\n{BLUE}{'='*60}{RESET}")
        print(f"{BLUE}Testing Homepage Links{RESET}")
        print(f"{BLUE}{'='*60}{RESET}\n")
        
        links_to_test = [
            ("en/getting-started.md", "English Getting Started"),
            ("ru/getting-started.md", "Russian Getting Started"),
            ("en/managed/index.md", "English Managed"),
            ("ru/managed/index.md", "Russian Managed"),
            ("ai/gemini.md", "AI Gemini Chat"),
            ("ai/notebooklm.md", "AI NotebookLM"),
        ]
        
        for filepath, description in links_to_test:
            self.test_file_exists(filepath, description)
    
    def test_navigation_files(self):
        """Test files referenced in mkdocs navigation"""
        print(f"\n{BLUE}{'='*60}{RESET}")
        print(f"{BLUE}Testing Navigation Files{RESET}")
        print(f"{BLUE}{'='*60}{RESET}\n")
        
        nav_files = [
            "en/discover-dynatrace/what-is-dynatrace.md",
            "en/observe/infrastructure-observability.md",
            "en/platform/grail/dynatrace-query-language.md",
            "en/ingest-from/dynatrace-oneagent/installation-and-operation.md",
            "ru/observe/infrastructure-observability.md",
            "ru/platform/oneagent.md",
        ]
        
        for filepath in nav_files:
            self.test_file_exists(filepath, "Nav file")
    
    def test_ai_integration(self):
        """Test AI integration files"""
        print(f"\n{BLUE}{'='*60}{RESET}")
        print(f"{BLUE}Testing AI Integration{RESET}")
        print(f"{BLUE}{'='*60}{RESET}\n")
        
        # Check Gemini JavaScript
        js_file = self.base_dir / 'docs/assets/javascripts/gemini-chat.js'
        if js_file.exists():
            content = js_file.read_text(encoding='utf-8')
            
            # Check API key
            if 'AIzaSyDvAv31Q97V-C5PRqEKf51uUSDIH8s5Vwo' in content:
                self.print_status("PASS", "Gemini API key found in gemini-chat.js")
            else:
                self.print_status("FAIL", "Gemini API key NOT found in gemini-chat.js")
            
            # Check API endpoint
            if 'generativelanguage.googleapis.com' in content:
                self.print_status("PASS", "Gemini API endpoint configured")
            else:
                self.print_status("FAIL", "Gemini API endpoint NOT configured")
            
            # Check widget creation
            if 'createChatWidget' in content:
                self.print_status("PASS", "Chat widget creation function exists")
            else:
                self.print_status("FAIL", "Chat widget creation function MISSING")
        else:
            self.print_status("FAIL", "gemini-chat.js NOT FOUND")
        
        # Check mkdocs.yml includes the JS
        mkdocs_file = self.base_dir / 'mkdocs.yml'
        if mkdocs_file.exists():
            content = mkdocs_file.read_text(encoding='utf-8')
            if 'assets/javascripts/gemini-chat.js' in content:
                self.print_status("PASS", "Gemini JS linked in mkdocs.yml")
            else:
                self.print_status("FAIL", "Gemini JS NOT linked in mkdocs.yml")
    
    def count_documentation(self):
        """Count English and Russian documentation files"""
        print(f"\n{BLUE}{'='*60}{RESET}")
        print(f"{BLUE}Documentation Statistics{RESET}")
        print(f"{BLUE}{'='*60}{RESET}\n")
        
        en_docs = list((self.docs_dir / 'en').rglob('*.md')) if (self.docs_dir / 'en').exists() else []
        ru_docs = list((self.docs_dir / 'ru').rglob('*.md')) if (self.docs_dir / 'ru').exists() else []
        
        print(f"{BLUE}ℹ️  English documentation:{RESET} {len(en_docs)} files")
        print(f"{BLUE}ℹ️  Russian documentation:{RESET} {len(ru_docs)} files")
        
        if len(ru_docs) < len(en_docs) * 0.5:
            self.print_status("WARN", f"Russian translation only {len(ru_docs)}/{len(en_docs)} files ({len(ru_docs)*100//len(en_docs)}%)")
        else:
            self.print_status("PASS", f"Russian translation coverage: {len(ru_docs)*100//len(en_docs)}%")
    
    def test_build_requirements(self):
        """Test if all build requirements are present"""
        print(f"\n{BLUE}{'='*60}{RESET}")
        print(f"{BLUE}Testing Build Requirements{RESET}")
        print(f"{BLUE}{'='*60}{RESET}\n")
        
        req_file = self.base_dir / 'requirements.txt'
        if req_file.exists():
            content = req_file.read_text()
            required = ['mkdocs-material', 'pymdown-extensions']
            
            for req in required:
                if req in content:
                    self.print_status("PASS", f"Requirement '{req}' found")
                else:
                    self.print_status("FAIL", f"Requirement '{req}' MISSING")
        else:
            self.print_status("FAIL", "requirements.txt NOT FOUND")
    
    def print_summary(self):
        """Print test summary"""
        print(f"\n{BLUE}{'='*60}{RESET}")
        print(f"{BLUE}TEST SUMMARY{RESET}")
        print(f"{BLUE}{'='*60}{RESET}\n")
        
        print(f"{GREEN}✅ PASSED:{RESET} {len(self.passed)} tests")
        print(f"{YELLOW}⚠️  WARNINGS:{RESET} {len(self.warnings)} issues")
        print(f"{RED}❌ FAILED:{RESET} {len(self.errors)} tests")
        
        if self.errors:
            print(f"\n{RED}CRITICAL ERRORS:{RESET}")
            for error in self.errors:
                print(f"  - {error}")
        
        if self.warnings:
            print(f"\n{YELLOW}WARNINGS:{RESET}")
            for warning in self.warnings:
                print(f"  - {warning}")
        
        print(f"\n{BLUE}{'='*60}{RESET}\n")
        
        # Overall status
        if self.errors:
            print(f"{RED}❌ TESTS FAILED - SITE HAS ISSUES{RESET}\n")
            return False
        elif self.warnings:
            print(f"{YELLOW}⚠️  TESTS PASSED WITH WARNINGS{RESET}\n")
            return True
        else:
            print(f"{GREEN}✅ ALL TESTS PASSED{RESET}\n")
            return True

def main():
    """Main test runner"""
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}🧪 Dynatrace Documentation Website - Automated Tests{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    # Get base directory
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        base_dir = os.getcwd()
    
    print(f"{BLUE}ℹ️  Testing directory:{RESET} {base_dir}\n")
    
    # Create tester and run tests
    tester = WebsiteTester(base_dir)
    
    tester.test_homepage_links()
    tester.test_navigation_files()
    tester.test_ai_integration()
    tester.count_documentation()
    tester.test_build_requirements()
    
    # Print summary
    success = tester.print_summary()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
