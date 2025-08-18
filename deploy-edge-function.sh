#!/bin/bash

echo "🚀 Deploying abbā Business AI Agent Edge Function..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if Supabase CLI is installed
if ! command -v supabase &> /dev/null; then
    echo -e "${RED}❌ Supabase CLI not found. Installing...${NC}"
    npm install -g supabase
fi

# Check if user is logged in
echo -e "${YELLOW}🔐 Checking Supabase authentication...${NC}"
if ! supabase projects list &> /dev/null; then
    echo -e "${YELLOW}🔑 Please login to Supabase...${NC}"
    supabase login
else
    echo -e "${GREEN}✅ Already logged in to Supabase${NC}"
fi

# Link the project
echo -e "${YELLOW}🔗 Linking to Supabase project...${NC}"
supabase link --project-ref vfzlbtojeqxkkskldrur

# Check if link was successful
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Project linked successfully${NC}"
else
    echo -e "${RED}❌ Failed to link project${NC}"
    exit 1
fi

# Deploy the Edge Function
echo -e "${YELLOW}🚀 Deploying business-ai-agent Edge Function...${NC}"
supabase functions deploy business-ai-agent

# Check deployment status
if [ $? -eq 0 ]; then
    echo -e "${GREEN}🎉 Edge Function deployed successfully!${NC}"
    echo ""
    echo -e "${BLUE}📋 Function Details:${NC}"
    echo "Function Name: business-ai-agent"
    echo "Project: vfzlbtojeqxkkskldrur"
    echo "Endpoint: https://vfzlbtojeqxkkskldrur.supabase.co/functions/v1/business-ai-agent"
    echo ""
    echo -e "${BLUE}🧪 To test the function:${NC}"
    echo "curl -i --location --request POST 'https://vfzlbtojeqxkkskldrur.supabase.co/functions/v1/business-ai-agent' \\"
    echo "  --header 'Authorization: Bearer YOUR_SUPABASE_ANON_KEY' \\"
    echo "  --header 'Content-Type: application/json' \\"
    echo "  --data '{\"business_description\":\"Uma startup de tecnologia focada em IA\"}'"
    echo ""
    echo -e "${GREEN}✅ Deployment complete! Your AI business agent is ready! 🤖${NC}"
else
    echo -e "${RED}❌ Failed to deploy Edge Function${NC}"
    echo -e "${YELLOW}💡 Troubleshooting tips:${NC}"
    echo "1. Make sure Docker is running (should be automatic in Gitpod)"
    echo "2. Check if you have the correct permissions"
    echo "3. Verify the project reference is correct"
    exit 1
fi
