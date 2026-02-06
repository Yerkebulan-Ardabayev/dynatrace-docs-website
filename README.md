# Dynatrace Documentation Website 🚀

Complete bilingual (English/Russian) Dynatrace documentation with AI assistant integration.

## 🌟 Features

- **📚 Complete Documentation** - Full mirror of official Dynatrace docs
- **🌍 Bilingual** - English (original) + Russian (auto-translated)
- **🤖 AI Assistant** - Built-in Gemini AI chat + NotebookLM integration
- **📱 Mobile-Friendly** - Beautiful Material Design theme
- **🔍 Powerful Search** - Search across all documentation
- **🔄 Auto-Updates** - Daily synchronization at 02:00 (UTC+5)
- **📁 Organized Structure** - Managed docs in separate section
- **⚡ Fast & Modern** - Instant loading with MkDocs Material

## 🌐 Live Website

**Coming soon:** `https://YOUR_USERNAME.github.io/dynatrace-docs-website/`

## 📦 What's Inside

```
dynatrace-docs-website/
├── docs/                    # Documentation content
│   ├── index.md            # Homepage
│   ├── en/                 # English docs
│   │   ├── managed/       # Dynatrace Managed (separate)
│   │   ├── observe/
│   │   ├── platform/
│   │   └── ...
│   ├── ru/                 # Russian docs (auto-translated)
│   │   ├── managed/
│   │   └── ...
│   ├── ai/                 # AI assistant guides
│   └── assets/             # CSS, JS, images
│
├── scripts/                # Automation scripts
│   ├── scrape_docs.py     # Download docs from dynatrace.com
│   ├── translate_docs.py  # Translate EN → RU
│   └── organize_docs.py   # Organize Managed separately
│
├── .github/workflows/      # GitHub Actions
│   ├── update-docs.yml    # Daily doc updates
│   └── deploy.yml         # Deploy to GitHub Pages
│
├── mkdocs.yml             # MkDocs configuration
└── requirements.txt       # Python dependencies
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Git

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/dynatrace-docs-website.git
cd dynatrace-docs-website
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download Initial Documentation (Optional)

```bash
cd scripts
python scrape_docs.py --max-pages 50
python organize_docs.py
python translate_docs.py
cd ..
```

###  4. Run Locally

```bash
mkdocs serve
```

Open: http://localhost:8000

### 5. Deploy to GitHub Pages

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

GitHub Actions will automatically:
1. Build the website
2. Deploy to GitHub Pages
3. Available at: `https://YOUR_USERNAME.github.io/dynatrace-docs-website/`

## 🤖 AI Features

### Quick Chat (Gemini)

- Click the AI button (bottom-right corner)
- Ask questions in English or Russian
- Get instant answers based on current page

**Your API Key:** Already configured ✅

### Deep Analysis (NotebookLM)

For complex questions:
1. Visit [NotebookLM](https://notebooklm.google.com/)
2. Upload documentation from `docs/` folder
3. Ask comprehensive questions

## 🔄 Automatic Updates

Documentation updates automatically every day at **02:00 (UTC+5)**:

1. **Scrape** - Download latest docs from dynatrace.com
2. **Organize** - Separate Managed docs
3. **Translate** - Auto-translate to Russian
4. **Deploy** - Push to GitHub Pages

### Manual Update

```bash
# Update docs manually
.github/workflows/update-docs.yml
```

## 📱 Mobile Access

Website is fully responsive:
- Desktop 💻
- Tablets 📱
- Smartphones 📱

## 🎨 Customization

### Change Colors

Edit `mkdocs.yml`:

```yaml
theme:
  palette:
    primary: indigo  # Change to your color
    accent: indigo
```

### Add Custom Pages

1. Create `.md` file in `docs/`
2. Add to `nav` section in `mkdocs.yml`
3. Commit and push

## 📊 Statistics

- **Total Documentation Pages:** Auto-updated daily
- **Languages:** 2 (English, Russian)
- **Update Frequency:** Daily at 02:00
- **Last Update:** Check [GitHub commits](../../commits/main)

## 🛠️ Maintenance

### Clear Translation Cache

```bash
rm .translation_cache.json
```

### Rebuild All Translations

```bash
cd scripts
python translate_docs.py
```

### Force Full Re-scrape

```bash
cd scripts
rm -rf .cache
python scrape_docs.py
```

## 🔒 Security

- API key is used client-side only
- No sensitive data stored
- Open source and transparent

## 📝 License

This is an unofficial documentation mirror. Official documentation: [docs.dynatrace.com](https://docs.dynatrace.com)

## 🙋 Support

- **Questions?** Check the [AI Assistant](ai/gemini.md)
- **Issues?** Open a GitHub issue
- **Contributions?** Pull requests welcome!

## 🎯 Roadmap

- [x] Basic scraper
- [x] Bilingual support
- [x] AI integration (Gemini)
- [x] Auto-updates
- [x] GitHub Pages deployment
- [ ] PDF export
- [ ] Offline mode
- [ ] Search analytics
- [ ] More languages

---

Made with ❤️ using [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)

**Last updated:** Check [commits](../../commits/main)
