# Makefile untuk Bot Telegram Claim TukTuk
# Simplifies common development tasks

.PHONY: help install run test clean lint format docs

# Default target
help:
	@echo "╔══════════════════════════════════════════════════════════╗"
	@echo "║     BOT TELEGRAM CLAIM TUKTUK - AVAILABLE COMMANDS       ║"
	@echo "╚══════════════════════════════════════════════════════════╝"
	@echo ""
	@echo "  make install     - Install dependencies"
	@echo "  make run         - Run the bot"
	@echo "  make test        - Run unit tests"
	@echo "  make clean       - Clean cache files"
	@echo "  make lint        - Run linter (flake8)"
	@echo "  make format      - Format code (black)"
	@echo "  make setup       - Initial setup"
	@echo "  make update      - Update dependencies"
	@echo "  make docs        - Show documentation"
	@echo "  make check       - Run all checks"
	@echo ""

# Install dependencies
install:
	@echo "📦 Installing dependencies..."
	pip install -r requirements.txt
	@echo "✅ Dependencies installed!"

# Run the bot
run:
	@echo "🚀 Starting bot..."
	python bot.py

# Run with virtual environment
run-venv:
	@echo "🚀 Starting bot with virtual environment..."
	./run.sh

# Run tests
test:
	@echo "🧪 Running tests..."
	python test_bot.py
	@echo "✅ Tests completed!"

# Clean cache files
clean:
	@echo "🧹 Cleaning cache files..."
	rm -rf __pycache__
	rm -rf *.pyc
	rm -rf *.pyo
	rm -rf *.pyd
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	@echo "✅ Cache cleaned!"

# Run linter
lint:
	@echo "🔍 Running linter..."
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	@echo "✅ Linting completed!"

# Format code
format:
	@echo "🎨 Formatting code..."
	black . --line-length 100
	@echo "✅ Code formatted!"

# Initial setup
setup:
	@echo "⚙️  Running initial setup..."
	@echo "1. Creating virtual environment..."
	python3 -m venv venv
	@echo "2. Installing dependencies..."
	. venv/bin/activate && pip install -r requirements.txt
	@echo "3. Creating .env file..."
	cp .env.example .env
	@echo ""
	@echo "✅ Setup completed!"
	@echo "⚠️  Please edit .env file with your configuration"

# Update dependencies
update:
	@echo "🔄 Updating dependencies..."
	pip install --upgrade -r requirements.txt
	@echo "✅ Dependencies updated!"

# Show documentation
docs:
	@echo ""
	@echo "📚 Available documentation:"
	@echo ""
	@echo "  README.md                  - Main documentation"
	@echo "  INSTALL.md                 - Installation guide"
	@echo "  QUICKSTART.md              - Quick start (5 minutes)"
	@echo "  PANDUAN_GOOGLE_SHEETS.md   - Google Sheets setup"
	@echo "  DEPLOY.md                  - Deployment guide"
	@echo "  FAQ.md                     - Frequently asked questions"
	@echo "  CONTRIBUTING.md            - Contribution guide"
	@echo ""

# Run all checks
check:
	@echo "🔍 Running all checks..."
	@echo ""
	@echo "1. Running tests..."
	python test_bot.py
	@echo ""
	@echo "2. Checking config..."
	python config.py
	@echo ""
	@echo "✅ All checks completed!"

# Development mode (with auto-reload)
dev:
	@echo "🚀 Starting bot in development mode..."
	watchmedo auto-restart --directory=. --pattern="*.py" --recursive -- python bot.py

# Create distribution package
dist:
	@echo "📦 Creating distribution package..."
	python setup.py sdist bdist_wheel
	@echo "✅ Package created in dist/"

# Install in development mode
dev-install:
	@echo "⚙️  Installing in development mode..."
	pip install -e .
	@echo "✅ Installed in development mode!"

# Uninstall
uninstall:
	@echo "🗑️  Uninstalling..."
	pip uninstall telegram-bot-tuktuk -y
	@echo "✅ Uninstalled!"
