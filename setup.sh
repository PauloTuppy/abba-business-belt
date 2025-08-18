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

# Create .env file with OpenAI API key
echo -e "${YELLOW}📝 Creating .env file with API keys...${NC}"
cat > .env << EOF
# OpenAI Configuration
OPENAI_API_KEY=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

# Supabase Configuration
SUPABASE_URL=https://vfzlbtojeqxkkskldrur.supabase.co
SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key

# ElevenLabs Configuration (for voice features)
ELEVENLABS_API_KEY=your-elevenlabs-api-key

# Application Settings
DEBUG=true
PORT=8000
HOST=0.0.0.0
EOF

echo -e "${GREEN}✅ .env file created with OpenAI API key${NC}"

echo -e "${GREEN}🎉 Setup complete!${NC}"
echo ""
echo -e "${BLUE}📋 Next steps:${NC}"
echo "1. Run: supabase login"
echo "2. Run: supabase link --project-ref vfzlbtojeqxkkskldrur"
echo "3. Run: supabase functions deploy business-ai-agent"
echo ""
echo -e "${BLUE}🚀 To start development:${NC}"
echo "Frontend: npm run dev"
echo "Backend: python main.py"
echo ""
echo -e "${GREEN}Happy coding! 🥋${NC}"
