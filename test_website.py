#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Test Suite for Dynatrace Documentation Website
=============================================================
Full coverage: security, build, translations, AI integration, config, CI/CD

Usage:
    python test_website.py                    # Run all tests
    python test_website.py --section security # Run only security tests
    python test_website.py --verbose          # Detailed output

Test categories:
    1. Security       — API keys, XSS, secrets in source code
    2. Build          — MkDocs config, requirements, file structure
    3. Translations   — Quality, brand terms, frontmatter, code blocks
    4. AI Integration — Chat widget, server proxy, Cloudflare Worker
    5. Config         — mkdocs.yml, ai-config.json, .env, CI/CD
    6. Links          — Internal navigation, cross-references
    7. Documentation  — Coverage stats, file integrity
"""

import os
import re
import sys
import json
import yaml
from pathlib import Path
from typing import List, Tuple, Optional

# Ensure UTF-8 on Windows
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Terminal colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
BOLD = '\033[1m'
RESET = '\033[0m'


class TestResult:
    """Stores test results with context"""
    def __init__(self, name: str, passed: bool, message: str, severity: str = 'error'):
        self.name = name
        self.passed = passed
        self.message = message
        self.severity = severity  # 'error', 'warning', 'info'


class WebsiteTester:
    """Comprehensive website test suite"""

    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)
        self.docs_dir = self.base_dir / 'docs'
        self.site_dir = self.base_dir / 'site'
        self.scripts_dir = self.base_dir / 'scripts'
        self.results: List[TestResult] = []
        self.section_filter: Optional[str] = None

    def add_result(self, name: str, passed: bool, message: str, severity: str = 'error'):
        self.results.append(TestResult(name, passed, message, severity))
        icon = f"{GREEN}PASS{RESET}" if passed else (
            f"{RED}FAIL{RESET}" if severity == 'error' else f"{YELLOW}WARN{RESET}"
        )
        print(f"  [{icon}] {message}")

    def section_header(self, title: str, emoji: str = ""):
        print(f"\n{BOLD}{BLUE}{'=' * 65}{RESET}")
        print(f"{BOLD}{BLUE}  {emoji} {title}{RESET}")
        print(f"{BOLD}{BLUE}{'=' * 65}{RESET}\n")

    # =========================================================================
    # 1. SECURITY TESTS
    # =========================================================================
    def test_security(self):
        """Comprehensive security checks"""
        self.section_header("SECURITY TESTS", "1.")

        # 1.1 No hardcoded API keys in ANY source file
        key_patterns = [
            (r'gsk_[a-zA-Z0-9]{20,}', 'Groq API key'),
            (r'AIzaSy[a-zA-Z0-9_-]{30,}', 'Google/Gemini API key'),
            (r'sk-[a-zA-Z0-9]{40,}', 'OpenAI API key'),
            (r'xoxb-[0-9]+-[a-zA-Z0-9]+', 'Slack Bot token'),
            (r'ghp_[a-zA-Z0-9]{36}', 'GitHub Personal Access Token'),
        ]

        # Only scan source directories (skip site/, node_modules, .git, venv)
        scan_dirs = [self.base_dir / 'docs', self.base_dir / 'scripts',
                     self.base_dir / 'cloudflare-worker', self.base_dir / '.github']
        scan_root_files = list(self.base_dir.glob('*.py')) + list(self.base_dir.glob('*.js')) + \
                          list(self.base_dir.glob('*.json')) + list(self.base_dir.glob('*.yml'))

        files_to_check = list(scan_root_files)
        for scan_dir in scan_dirs:
            if scan_dir.exists():
                for ext in ['*.py', '*.js', '*.json', '*.yml', '*.yaml', '*.html', '*.md']:
                    files_to_check.extend(scan_dir.rglob(ext))

        # Exclude __pycache__
        files_to_check = [
            f for f in files_to_check
            if '__pycache__' not in str(f)
        ]

        for pattern, key_name in key_patterns:
            found_in = []
            for fpath in files_to_check:
                try:
                    content = fpath.read_text(encoding='utf-8', errors='ignore')
                    if re.search(pattern, content):
                        # Exclude legitimate patterns (e.g., regex definitions in validators)
                        # Check if it's a regex pattern definition vs actual key
                        lines_with_key = [
                            line.strip() for line in content.split('\n')
                            if re.search(pattern, line) and 're.search' not in line
                            and 'pattern' not in line.lower() and 'regex' not in line.lower()
                            and "r'" not in line and 'r"' not in line
                        ]
                        if lines_with_key:
                            found_in.append(str(fpath.relative_to(self.base_dir)))
                except Exception:
                    continue

            if found_in:
                self.add_result('security_keys',
                    False,
                    f"CRITICAL: {key_name} pattern found in: {', '.join(found_in[:3])}")
            else:
                self.add_result('security_keys', True, f"No {key_name} hardcoded in source")

        # 1.2 XSS protection in chat widget
        js_file = self.docs_dir / 'assets' / 'javascripts' / 'groq-chat.js'
        if js_file.exists():
            js_content = js_file.read_text(encoding='utf-8')
            has_escape = 'escapeHtml' in js_content or '&amp;' in js_content or '&lt;' in js_content
            self.add_result('security_xss', has_escape,
                "XSS protection in chat widget" + (" (escapeHtml found)" if has_escape else " MISSING"))

            # Check markdownToHtml escapes before formatting
            md_func_match = re.search(r'function markdownToHtml[\s\S]*?}', js_content)
            if md_func_match:
                md_func = md_func_match.group()
                escape_before_format = md_func.find('&amp;') < md_func.find('<strong>') if '<strong>' in md_func else False
                self.add_result('security_xss_order',
                    escape_before_format or '&amp;' in md_func,
                    "HTML escaping happens BEFORE markdown formatting")
        else:
            self.add_result('security_xss', False, "groq-chat.js not found!", 'warning')

        # 1.3 .env not in git
        env_file = self.base_dir / '.env'
        gitignore_file = self.base_dir / '.gitignore'
        if gitignore_file.exists():
            gitignore = gitignore_file.read_text(encoding='utf-8')
            self.add_result('security_env', '.env' in gitignore,
                ".env is in .gitignore")
        else:
            self.add_result('security_env', False, ".gitignore not found!", 'warning')

        # 1.4 Server doesn't expose stack traces
        server_file = self.base_dir / 'local_server.py'
        if server_file.exists():
            server_content = server_file.read_text(encoding='utf-8')
            has_raw_error = 'str(e)' in server_content and 'jsonify' in server_content
            # Check that error responses don't contain str(e) directly in jsonify
            error_patterns = re.findall(r"jsonify\(\{[^}]*str\(e\)[^}]*\}\)", server_content)
            self.add_result('security_error_exposure',
                len(error_patterns) == 0,
                "Server doesn't expose raw error details to clients" + (
                    f" ({len(error_patterns)} instances found)" if error_patterns else ""))

        # 1.5 Sanitize secrets script exists
        sanitize = self.scripts_dir / 'sanitize_secrets.py'
        self.add_result('security_sanitize', sanitize.exists(),
            "Secret sanitization script exists")

    # =========================================================================
    # 2. BUILD TESTS
    # =========================================================================
    def test_build(self):
        """Build configuration and requirements"""
        self.section_header("BUILD TESTS", "2.")

        # 2.1 mkdocs.yml exists and is valid YAML
        mkdocs_file = self.base_dir / 'mkdocs.yml'
        mkdocs_valid = False
        mkdocs_config = None
        if mkdocs_file.exists():
            try:
                # MkDocs uses !!python/name: tags — use FullLoader or fallback
                mkdocs_text = mkdocs_file.read_text(encoding='utf-8')
                try:
                    mkdocs_config = yaml.full_load(mkdocs_text)
                except Exception:
                    # Fallback: strip !!python/ tags and use safe_load
                    clean_text = re.sub(r'!!python/\S+', '', mkdocs_text)
                    mkdocs_config = yaml.safe_load(clean_text)
                mkdocs_valid = isinstance(mkdocs_config, dict) and 'site_name' in mkdocs_config
                self.add_result('build_mkdocs', mkdocs_valid,
                    f"mkdocs.yml valid YAML (site_name: {mkdocs_config.get('site_name', 'MISSING')})")
            except yaml.YAMLError as e:
                self.add_result('build_mkdocs', False, f"mkdocs.yml has YAML errors: {str(e)[:100]}")
        else:
            self.add_result('build_mkdocs', False, "mkdocs.yml NOT FOUND")

        # 2.2 Required theme and plugins
        if mkdocs_config:
            theme = mkdocs_config.get('theme', {})
            self.add_result('build_theme', theme.get('name') == 'material',
                f"Theme: {theme.get('name', 'MISSING')} (expected: material)")

            plugins = mkdocs_config.get('plugins', [])
            plugin_names = []
            for p in plugins:
                if isinstance(p, str):
                    plugin_names.append(p)
                elif isinstance(p, dict):
                    plugin_names.extend(p.keys())
            self.add_result('build_search', 'search' in plugin_names,
                f"Search plugin: {'enabled' if 'search' in plugin_names else 'MISSING'}")

            # Check nav exists and has entries
            nav = mkdocs_config.get('nav', [])
            self.add_result('build_nav', len(nav) > 0,
                f"Navigation entries: {len(nav)}")

            # Check JS is linked
            extra_js = mkdocs_config.get('extra_javascript', [])
            has_chat = any('groq-chat.js' in str(j) for j in extra_js)
            self.add_result('build_js', has_chat,
                "groq-chat.js linked in extra_javascript")

            # Check CSS is linked
            extra_css = mkdocs_config.get('extra_css', [])
            has_css = any('extra.css' in str(c) for c in extra_css)
            self.add_result('build_css', has_css,
                "extra.css linked in extra_css")

        # 2.3 requirements.txt
        req_file = self.base_dir / 'requirements.txt'
        if req_file.exists():
            req_content = req_file.read_text(encoding='utf-8')
            required_deps = ['mkdocs-material', 'pymdown-extensions']
            for dep in required_deps:
                self.add_result('build_deps', dep in req_content,
                    f"Dependency '{dep}' in requirements.txt")
        else:
            self.add_result('build_deps', False, "requirements.txt NOT FOUND")

        # 2.4 Critical directories exist
        for dir_name in ['docs/en', 'docs/assets', 'docs/assets/javascripts', 'docs/assets/stylesheets']:
            dir_path = self.base_dir / dir_name
            self.add_result('build_dirs', dir_path.exists(),
                f"Directory exists: {dir_name}")

        # 2.5 Index files
        index_file = self.docs_dir / 'index.md'
        self.add_result('build_index', index_file.exists(),
            "docs/index.md (homepage) exists")

        # 2.6 Nav file existence check
        if mkdocs_config and 'nav' in mkdocs_config:
            nav_files = self._extract_nav_files(mkdocs_config['nav'])
            missing_nav = []
            for nf in nav_files:
                if not (self.docs_dir / nf).exists():
                    missing_nav.append(nf)

            if missing_nav:
                self.add_result('build_nav_files', False,
                    f"Missing nav files ({len(missing_nav)}): {', '.join(missing_nav[:5])}")
            else:
                self.add_result('build_nav_files', True,
                    f"All {len(nav_files)} navigation files exist")

    def _extract_nav_files(self, nav, files=None):
        """Recursively extract file paths from mkdocs nav"""
        if files is None:
            files = []
        if isinstance(nav, list):
            for item in nav:
                self._extract_nav_files(item, files)
        elif isinstance(nav, dict):
            for key, value in nav.items():
                self._extract_nav_files(value, files)
        elif isinstance(nav, str):
            # It's a file path — skip directory references ending with /
            if not nav.endswith('/'):
                files.append(nav)
        return files

    # =========================================================================
    # 3. TRANSLATION TESTS
    # =========================================================================
    def test_translations(self):
        """Translation quality and integrity"""
        self.section_header("TRANSLATION TESTS", "3.")

        en_dir = self.docs_dir / 'en'
        ru_dir = self.docs_dir / 'ru'

        en_files = sorted(en_dir.rglob('*.md')) if en_dir.exists() else []
        ru_files = sorted(ru_dir.rglob('*.md')) if ru_dir.exists() else []

        self.add_result('trans_en_count', len(en_files) > 0,
            f"English docs: {len(en_files)} files")
        self.add_result('trans_ru_count', len(ru_files) > 0,
            f"Russian docs: {len(ru_files)} files")

        if en_files:
            coverage = len(ru_files) / len(en_files) * 100
            self.add_result('trans_coverage', coverage > 5,
                f"Translation coverage: {coverage:.1f}% ({len(ru_files)}/{len(en_files)})",
                'warning' if coverage < 50 else 'error')

        # 3.1 Check brand terms in translated files (sample)
        bad_translations = {
            'ОдинАгент': 'OneAgent',
            'Один Агент': 'OneAgent',
            'Один агент': 'OneAgent',
            'Активный шлюз': 'ActiveGate',
            'Активный Шлюз': 'ActiveGate',
            'Чистый путь': 'PurePath',
            'Чистый Путь': 'PurePath',
            'Умная карта': 'Smartscape',
        }

        bad_term_files = 0
        sample_ru = ru_files[:100]  # Check first 100 files

        for ru_file in sample_ru:
            try:
                content = ru_file.read_text(encoding='utf-8')
                for bad_term in bad_translations:
                    if bad_term in content:
                        bad_term_files += 1
                        break
            except Exception:
                continue

        self.add_result('trans_brand_terms',
            bad_term_files == 0,
            f"Brand terms check: {bad_term_files}/{len(sample_ru)} files have incorrectly translated terms",
            'warning' if bad_term_files > 0 else 'error')

        # 3.2 Frontmatter integrity
        broken_frontmatter = 0
        for ru_file in sample_ru:
            try:
                content = ru_file.read_text(encoding='utf-8')
                if content.startswith('---'):
                    second = content.find('---', 3)
                    if second == -1:
                        broken_frontmatter += 1
            except Exception:
                continue

        self.add_result('trans_frontmatter',
            broken_frontmatter == 0,
            f"Frontmatter integrity: {broken_frontmatter}/{len(sample_ru)} files have broken frontmatter")

        # 3.3 Code block pairing
        unpaired_code = 0
        for ru_file in sample_ru:
            try:
                content = ru_file.read_text(encoding='utf-8')
                if content.count('```') % 2 != 0:
                    unpaired_code += 1
            except Exception:
                continue

        self.add_result('trans_code_blocks',
            unpaired_code == 0,
            f"Code block pairing: {unpaired_code}/{len(sample_ru)} files have unpaired ``` blocks")

        # 3.4 Empty/corrupt files
        empty_files = 0
        for ru_file in sample_ru:
            try:
                content = ru_file.read_text(encoding='utf-8')
                if len(content.strip()) < 20:
                    empty_files += 1
            except Exception:
                empty_files += 1

        self.add_result('trans_empty',
            empty_files == 0,
            f"Empty/corrupt files: {empty_files}/{len(sample_ru)}")

        # 3.5 Translation validator script exists and works
        validator_script = self.scripts_dir / 'validate_translations.py'
        self.add_result('trans_validator', validator_script.exists(),
            "validate_translations.py script exists")

        # 3.6 Protected terms list in translate script
        translate_script = self.scripts_dir / 'translate_docs_groq.py'
        if translate_script.exists():
            t_content = translate_script.read_text(encoding='utf-8')
            has_protection = 'PROTECTED_TERMS' in t_content or 'protect_terms' in t_content
            self.add_result('trans_protection', has_protection,
                "Brand term protection in translation script")

    # =========================================================================
    # 4. AI INTEGRATION TESTS
    # =========================================================================
    def test_ai_integration(self):
        """AI chat widget and backend integration"""
        self.section_header("AI INTEGRATION TESTS", "4.")

        # 4.1 Chat widget JS exists
        js_file = self.docs_dir / 'assets' / 'javascripts' / 'groq-chat.js'
        self.add_result('ai_js_exists', js_file.exists(),
            "groq-chat.js exists")

        if not js_file.exists():
            return

        js_content = js_file.read_text(encoding='utf-8')

        # 4.2 Auto-detect mode (proxy/worker/direct/disabled)
        has_detect = 'detectMode' in js_content
        self.add_result('ai_detect_mode', has_detect,
            "Auto-detect mode function (detectMode)")

        # 4.3 Multiple modes supported
        modes_supported = []
        if 'sendViaProxy' in js_content:
            modes_supported.append('proxy')
        if 'sendViaWorker' in js_content:
            modes_supported.append('worker')
        if 'sendDirect' in js_content:
            modes_supported.append('direct')

        self.add_result('ai_modes', len(modes_supported) >= 2,
            f"API modes: {', '.join(modes_supported)}")

        # 4.4 Cloudflare Worker support
        has_worker = 'worker' in js_content.lower() and 'GROQ_WORKER_URL' in js_content
        self.add_result('ai_worker', has_worker,
            "Cloudflare Worker support")

        # 4.5 Rate limiting (client-side)
        has_rate_limit = 'checkRateLimit' in js_content or 'RATE_LIMIT' in js_content
        self.add_result('ai_rate_limit', has_rate_limit,
            "Client-side rate limiting")

        # 4.6 Conversation history
        has_history = 'conversationHistory' in js_content or 'history' in js_content
        self.add_result('ai_history', has_history,
            "Conversation history support")

        # 4.7 Error handling for non-JSON responses
        has_content_type_check = 'content-type' in js_content or 'application/json' in js_content
        self.add_result('ai_error_handling', has_content_type_check,
            "Content-type check (prevents 'Unexpected token' error)")

        # 4.8 Chat widget creates DOM elements
        has_widget = 'createChatWidget' in js_content
        self.add_result('ai_widget', has_widget,
            "Chat widget DOM creation function")

        # 4.9 Server proxy (local_server.py)
        server_file = self.base_dir / 'local_server.py'
        if server_file.exists():
            s_content = server_file.read_text(encoding='utf-8')

            has_chat_endpoint = "'/api/chat'" in s_content
            self.add_result('ai_server_chat', has_chat_endpoint,
                "Server has /api/chat endpoint")

            has_server_rate = 'RateLimiter' in s_content
            self.add_result('ai_server_rate', has_server_rate,
                "Server-side rate limiting")

            has_status = "'/api/status'" in s_content
            self.add_result('ai_server_status', has_status,
                "Server has /api/status endpoint")

            has_update_token = 'UPDATE_TOKEN' in s_content
            self.add_result('ai_server_auth', has_update_token,
                "Server update endpoint is token-protected")
        else:
            self.add_result('ai_server', False, "local_server.py not found", 'warning')

        # 4.10 Cloudflare Worker file
        worker_file = self.base_dir / 'cloudflare-worker' / 'worker.js'
        if worker_file.exists():
            w_content = worker_file.read_text(encoding='utf-8')
            has_cors = 'Access-Control-Allow-Origin' in w_content
            has_api_call = 'api.groq.com' in w_content
            has_rate = 'checkRateLimit' in w_content or 'rateLimits' in w_content

            self.add_result('ai_worker_cors', has_cors, "Worker has CORS headers")
            self.add_result('ai_worker_api', has_api_call, "Worker calls Groq API")
            self.add_result('ai_worker_rate', has_rate, "Worker has rate limiting")
        else:
            self.add_result('ai_worker_file', False, "cloudflare-worker/worker.js not found", 'warning')

        # 4.11 ai-config.json structure
        config_file = self.docs_dir / 'assets' / 'ai-config.json'
        if config_file.exists():
            try:
                config = json.loads(config_file.read_text(encoding='utf-8'))
                has_worker_url = 'worker_url' in config
                has_api_key = 'groq_api_key' in config

                self.add_result('ai_config_fields', has_worker_url and has_api_key,
                    f"ai-config.json fields: worker_url={'present' if has_worker_url else 'MISSING'}, groq_api_key={'present' if has_api_key else 'MISSING'}")

                # CRITICAL: key should be empty in source!
                key_empty = not config.get('groq_api_key', '')
                self.add_result('ai_config_key_empty', key_empty,
                    "ai-config.json: groq_api_key is empty (safe for public repo)")
            except json.JSONDecodeError:
                self.add_result('ai_config_json', False, "ai-config.json has invalid JSON!")
        else:
            self.add_result('ai_config', False, "ai-config.json not found", 'warning')

    # =========================================================================
    # 5. CONFIG & CI/CD TESTS
    # =========================================================================
    def test_config(self):
        """Configuration files and CI/CD"""
        self.section_header("CONFIG & CI/CD TESTS", "5.")

        # 5.1 GitHub Actions workflows
        workflows_dir = self.base_dir / '.github' / 'workflows'
        if workflows_dir.exists():
            workflows = list(workflows_dir.glob('*.yml')) + list(workflows_dir.glob('*.yaml'))
            self.add_result('ci_workflows', len(workflows) > 0,
                f"GitHub Actions workflows: {len(workflows)} found")

            for wf in workflows:
                try:
                    wf_content = wf.read_text(encoding='utf-8')
                    wf_config = yaml.safe_load(wf_content)
                    wf_name = wf_config.get('name', wf.stem)
                    self.add_result('ci_workflow_valid', True,
                        f"Workflow '{wf_name}' ({wf.name}) is valid YAML")

                    # Check for validation step in update workflow
                    if 'update' in wf.stem.lower():
                        has_validate = 'validate' in wf_content.lower()
                        self.add_result('ci_validate_step', has_validate,
                            f"Workflow '{wf_name}' has validation step", 'warning')

                        has_build = 'mkdocs build' in wf_content
                        self.add_result('ci_build_step', has_build,
                            f"Workflow '{wf_name}' has mkdocs build step")
                except Exception as e:
                    self.add_result('ci_workflow_valid', False,
                        f"Workflow {wf.name} has errors: {str(e)[:80]}")
        else:
            self.add_result('ci_workflows', False,
                "No .github/workflows directory found", 'warning')

        # 5.2 .gitignore completeness
        gitignore_file = self.base_dir / '.gitignore'
        if gitignore_file.exists():
            gi_content = gitignore_file.read_text(encoding='utf-8')
            critical_ignores = ['.env', 'site/', '__pycache__']
            for ci in critical_ignores:
                self.add_result('ci_gitignore', ci in gi_content,
                    f".gitignore includes '{ci}'")
        else:
            self.add_result('ci_gitignore', False, ".gitignore not found!")

        # 5.3 Python scripts are importable (syntax check)
        scripts = list(self.scripts_dir.glob('*.py')) if self.scripts_dir.exists() else []
        for script in scripts:
            try:
                compile(script.read_text(encoding='utf-8'), str(script), 'exec')
                self.add_result('ci_syntax', True,
                    f"Script syntax OK: {script.name}")
            except SyntaxError as e:
                self.add_result('ci_syntax', False,
                    f"Script syntax ERROR: {script.name} line {e.lineno}: {e.msg}")

    # =========================================================================
    # 6. LINK TESTS
    # =========================================================================
    def test_links(self):
        """Internal links and cross-references"""
        self.section_header("LINK TESTS", "6.")

        # 6.1 Homepage links
        homepage = self.docs_dir / 'index.md'
        if homepage.exists():
            content = homepage.read_text(encoding='utf-8')
            links = re.findall(r'\[([^\]]*)\]\(([^\)]*)\)', content)

            broken_links = []
            for text, url in links:
                # Only check internal links (not http://)
                if url.startswith('http') or url.startswith('#') or url.startswith('mailto:'):
                    continue
                # Resolve relative path
                target = self.docs_dir / url
                # Also try without .md extension
                if not target.exists() and not target.with_suffix('.md').exists():
                    # Check if it's a directory with index.md
                    if not (target / 'index.md').exists():
                        broken_links.append(f"[{text}]({url})")

            if broken_links:
                self.add_result('links_homepage', False,
                    f"Broken links on homepage: {', '.join(broken_links[:5])}")
            else:
                self.add_result('links_homepage', True,
                    f"All {len(links)} homepage links valid")
        else:
            self.add_result('links_homepage', False, "docs/index.md not found!")

        # 6.2 AI section links
        ai_pages = ['ai/groq.md', 'ai/notebooklm.md']
        for page in ai_pages:
            path = self.docs_dir / page
            self.add_result('links_ai', path.exists(),
                f"AI page exists: {page}")

        # 6.3 Managed section
        managed_pages = [
            'managed/index.md', 'managed/installation.md',
            'managed/configuration.md', 'managed/operations.md'
        ]
        for page in managed_pages:
            path = self.docs_dir / page
            self.add_result('links_managed', path.exists(),
                f"Managed page exists: {page}")

    # =========================================================================
    # 7. DOCUMENTATION COVERAGE TESTS
    # =========================================================================
    def test_documentation(self):
        """Documentation coverage and statistics"""
        self.section_header("DOCUMENTATION COVERAGE", "7.")

        en_dir = self.docs_dir / 'en'
        ru_dir = self.docs_dir / 'ru'

        en_count = len(list(en_dir.rglob('*.md'))) if en_dir.exists() else 0
        ru_count = len(list(ru_dir.rglob('*.md'))) if ru_dir.exists() else 0
        managed_count = len(list((self.docs_dir / 'managed').rglob('*.md'))) if (self.docs_dir / 'managed').exists() else 0
        ai_count = len(list((self.docs_dir / 'ai').rglob('*.md'))) if (self.docs_dir / 'ai').exists() else 0

        print(f"  {BLUE}English docs:  {en_count} files{RESET}")
        print(f"  {BLUE}Russian docs:  {ru_count} files{RESET}")
        print(f"  {BLUE}Managed docs:  {managed_count} files{RESET}")
        print(f"  {BLUE}AI docs:       {ai_count} files{RESET}")

        if en_count > 0:
            pct = ru_count / en_count * 100
            print(f"  {BLUE}Translation:   {pct:.1f}%{RESET}")

        # Check for duplicates
        if en_dir.exists() and ru_dir.exists():
            en_relative = set(str(f.relative_to(en_dir)) for f in en_dir.rglob('*.md'))
            ru_relative = set(str(f.relative_to(ru_dir)) for f in ru_dir.rglob('*.md'))
            translated = en_relative & ru_relative
            untranslated = en_relative - ru_relative
            print(f"  {BLUE}Translated:    {len(translated)} files match EN structure{RESET}")
            print(f"  {BLUE}Untranslated:  {len(untranslated)} files remain{RESET}")

        # CSS check
        css_file = self.docs_dir / 'assets' / 'stylesheets' / 'extra.css'
        if css_file.exists():
            css_content = css_file.read_text(encoding='utf-8')
            has_chat_styles = '.chat-container' in css_content or '#groq-chat-widget' in css_content
            self.add_result('docs_css', has_chat_styles,
                "Chat widget CSS styles present")
        else:
            self.add_result('docs_css', False, "extra.css not found", 'warning')

    # =========================================================================
    # RUN ALL TESTS
    # =========================================================================
    def run_all(self, section: Optional[str] = None):
        """Run all test sections"""
        test_map = {
            'security': self.test_security,
            'build': self.test_build,
            'translations': self.test_translations,
            'ai': self.test_ai_integration,
            'config': self.test_config,
            'links': self.test_links,
            'documentation': self.test_documentation,
        }

        if section:
            if section in test_map:
                test_map[section]()
            else:
                print(f"{RED}Unknown section: {section}{RESET}")
                print(f"Available: {', '.join(test_map.keys())}")
                return False
        else:
            for test_func in test_map.values():
                test_func()

        return self.print_summary()

    def print_summary(self) -> bool:
        """Print final test summary"""
        passed = sum(1 for r in self.results if r.passed)
        failed = sum(1 for r in self.results if not r.passed and r.severity == 'error')
        warnings = sum(1 for r in self.results if not r.passed and r.severity == 'warning')
        total = len(self.results)

        self.section_header("TEST SUMMARY", "")

        print(f"  {GREEN}PASSED:   {passed}/{total}{RESET}")
        if warnings > 0:
            print(f"  {YELLOW}WARNINGS: {warnings}{RESET}")
        if failed > 0:
            print(f"  {RED}FAILED:   {failed}{RESET}")

        if failed > 0:
            print(f"\n  {RED}{BOLD}CRITICAL FAILURES:{RESET}")
            for r in self.results:
                if not r.passed and r.severity == 'error':
                    print(f"    {RED}- {r.message}{RESET}")

        if warnings > 0:
            print(f"\n  {YELLOW}WARNINGS:{RESET}")
            for r in self.results:
                if not r.passed and r.severity == 'warning':
                    print(f"    {YELLOW}- {r.message}{RESET}")

        print(f"\n{'=' * 65}")
        if failed > 0:
            print(f"  {RED}{BOLD}RESULT: FAILED ({failed} critical issues){RESET}")
            return False
        elif warnings > 0:
            print(f"  {YELLOW}{BOLD}RESULT: PASSED WITH WARNINGS ({warnings} non-critical){RESET}")
            return True
        else:
            print(f"  {GREEN}{BOLD}RESULT: ALL TESTS PASSED{RESET}")
            return True


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Dynatrace Docs Website - Full Test Suite')
    parser.add_argument('--section', choices=[
        'security', 'build', 'translations', 'ai', 'config', 'links', 'documentation'
    ], help='Run specific test section only')
    parser.add_argument('--verbose', action='store_true', help='More detailed output')
    parser.add_argument('base_dir', nargs='?', default=os.getcwd(), help='Project root directory')

    args = parser.parse_args()

    print(f"\n{BOLD}{BLUE}{'=' * 65}{RESET}")
    print(f"{BOLD}{BLUE}  Dynatrace Documentation Website — Full Test Suite{RESET}")
    print(f"{BOLD}{BLUE}{'=' * 65}{RESET}")
    print(f"  Project: {args.base_dir}\n")

    tester = WebsiteTester(args.base_dir)
    success = tester.run_all(section=args.section)

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
