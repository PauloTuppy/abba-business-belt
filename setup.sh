#!/bin/bash

echo "🚀 Setting up abbā Business Belt Application..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if running in Gitpod
if [ "$GITPOD_WORKSPACE_ID" ]; then
    echo -e "${BLUE}🌐 Detected Gitpod environment${NC}"
    ENVIRONMENT="gitpod"
else
    echo -e "${BLUE}💻 Detected local environment${NC}"
    ENVIRONMENT="local"
fi

# Install Supabase CLI if not present
if ! command -v supabase &> /dev/null; then
    echo -e "${YELLOW}📦 Installing Supabase CLI...${NC}"
    npm install -g supabase
else
    echo -e "${GREEN}✅ Supabase CLI already installed${NC}"
fi

# Install Python dependencies
echo -e "${YELLOW}🐍 Installing Python dependencies...${NC}"
pip install -r requirements.txt

# Install Node.js dependencies
echo -e "${YELLOW}📦 Installing Node.js dependencies...${NC}"
npm install

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo -e "${YELLOW}📝 Creating .env file from template...${NC}"
    cp .env.example .env
    echo -e "${RED}⚠️  Please update .env file with your API keys${NC}"
else
    echo -e "${GREEN}✅ .env file already exists${NC}"
fi

echo -e "${GREEN}🎉 Setup complete!${NC}"
echo ""
echo -e "${BLUE}📋 Next steps:${NC}"
echo "1. Update your .env file with API keys"
echo "2. Run: supabase login"
echo "3. Run: supabase link --project-ref vfzlbtojeqxkkskldrur"
echo "4. Run: supabase functions deploy business-ai-agent"
echo ""
echo -e "${BLUE}🚀 To start development:${NC}"
echo "Frontend: npm run dev"
echo "Backend: python main.py"
echo ""
echo -e "${GREEN}Happy coding! 🥋${NC}"
