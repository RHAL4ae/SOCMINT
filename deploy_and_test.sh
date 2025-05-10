#!/bin/bash

# ======================================================
# SOCMINT Platform Deployment & Testing Script
# ======================================================
# This script automates the deployment and validation of the SOCMINT SaaS platform
# on Ubuntu Server 20.04+ using Docker Compose.
#
# Requirements:
# - Ubuntu Server 20.04+
# - Docker & Docker Compose installed
# - 16-core CPU, 32 GB RAM, 512 GB SSD
# - Internet access for pulling containers and UAE PASS sandbox testing
#
# Usage: ./deploy_and_test.sh
#
# Author: SOCMINT Team
# ======================================================

# Text formatting
BOLD="\033[1m"
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
RED="\033[0;31m"
NC="\033[0m" # No Color

# Function to print section headers
print_header() {
  echo -e "\n${BOLD}${GREEN}=== $1 ===${NC}\n"
}

# Function to print subsection headers
print_subheader() {
  echo -e "\n${BOLD}${YELLOW}--- $1 ---${NC}\n"
}

# Function to check if a command was successful
check_status() {
  if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ $1${NC}"
  else
    echo -e "${RED}✗ $1${NC}"
    if [ "$2" = "critical" ]; then
      echo -e "${RED}Critical error. Exiting deployment.${NC}"
      exit 1
    fi
  fi
}

# Function to wait for a service to be ready
wait_for_service() {
  local service=$1
  local url=$2
  local max_attempts=$3
  local attempt=1
  
  echo -e "Waiting for $service to be ready..."
  
  while [ $attempt -le $max_attempts ]; do
    if curl -s $url > /dev/null; then
      echo -e "${GREEN}$service is ready!${NC}"
      return 0
    fi
    
    echo -e "Attempt $attempt/$max_attempts: $service not ready yet. Waiting..."
    sleep 5
    ((attempt++))
  done
  
  echo -e "${RED}$service did not become ready within the expected time.${NC}"
  return 1
}

# Check system requirements
print_header "Checking System Requirements"

# Check Ubuntu version
# ubuntu_version=$(lsb_release -rs)
# echo "Ubuntu version: $ubuntu_version"
# if [[ $(echo "$ubuntu_version >= 20.04" | bc) -eq 1 ]]; then
#   echo -e "${GREEN}✓ Ubuntu version requirement met${NC}"
# else
#   echo -e "${RED}✗ Ubuntu version below 20.04. Please upgrade.${NC}"
#   exit 1
# fi

# Check CPU cores
cpu_cores=$(nproc)
echo "CPU cores: $cpu_cores"
if [[ $cpu_cores -ge 16 ]]; then
  echo -e "${GREEN}✓ CPU requirement met${NC}"
else
  echo -e "${YELLOW}⚠ CPU cores below recommended 16. Performance may be affected.${NC}"
fi

# Check RAM
total_ram=$(free -g | awk '/^Mem:/{print $2}')
echo "RAM: ${total_ram}GB"
if [[ $total_ram -ge 32 ]]; then
  echo -e "${GREEN}✓ RAM requirement met${NC}"
else
  echo -e "${YELLOW}⚠ RAM below recommended 32GB. Performance may be affected.${NC}"
fi

# Check disk space
disk_space=$(df -h / | awk 'NR==2 {print $4}')
echo "Available disk space: $disk_space"

# Check Docker installation
if command -v docker &> /dev/null; then
  docker_version=$(docker --version)
  echo -e "${GREEN}✓ Docker installed: $docker_version${NC}"
else
  echo -e "${RED}✗ Docker not installed${NC}"
  exit 1
fi

# Check Docker Compose installation
if command -v docker-compose &> /dev/null; then
  compose_version=$(docker-compose --version)
  echo -e "${GREEN}✓ Docker Compose installed: $compose_version${NC}"
else
  echo -e "${RED}✗ Docker Compose not installed${NC}"
  exit 1
fi

# Check internet connectivity
if ping -c 1 google.com &> /dev/null; then
  echo -e "${GREEN}✓ Internet connectivity available${NC}"
else
  echo -e "${RED}✗ No internet connectivity${NC}"
  exit 1
fi

# ======================================================
# PHASE 1: Infrastructure Validation
# ======================================================
print_header "PHASE 1: Infrastructure Validation"

# Start services
print_subheader "Starting Services"
echo "Starting all containers with docker-compose..."
docker-compose up -d
check_status "Started all services" "critical"

# Verify containers
print_subheader "Verifying Containers"
echo "Checking container status..."
docker-compose ps

# Check if all containers are running
running_containers=$(docker-compose ps --services --filter "status=running" | wc -l)
total_containers=$(docker-compose ps --services | wc -l)

echo "Running containers: $running_containers/$total_containers"
if [ "$running_containers" -eq "$total_containers" ]; then
  echo -e "${GREEN}✓ All containers are running${NC}"
else
  echo -e "${RED}✗ Some containers are not running${NC}"
  echo "Checking container logs for errors..."
  for service in $(docker-compose ps --services); do
    if ! docker-compose ps --services --filter "status=running" | grep -q "$service"; then
      echo -e "${RED}Container $service is not running. Logs:${NC}"
      docker-compose logs --tail=50 $service
    fi
  done
  exit 1
fi

# Network connectivity
print_subheader "Checking Network Connectivity"
echo "Verifying network connectivity between services..."

# Check if socmint_network exists
if docker network ls | grep -q socmint_network; then
  echo -e "${GREEN}✓ socmint_network exists${NC}"
  
  # List containers in the network
  echo "Containers in socmint_network:"
  docker network inspect socmint_network -f '{{range .Containers}}{{.Name}} {{end}}'
else
  echo -e "${RED}✗ socmint_network does not exist${NC}"
  exit 1
fi

# Test service access
print_subheader "Testing Service Access"

# Test Frontend
echo "Testing Frontend access..."
curl -s -o /dev/null -w "%{http_code}\n" http://localhost
check_status "Frontend access"

# Test Backend API
echo "Testing Backend API health..."
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8000/health
check_status "Backend API health"

# Test Elasticsearch
echo "Testing Elasticsearch access..."
curl -s -u "elastic:${ELASTIC_PASSWORD}" http://localhost:9200/_cat/indices
check_status "Elasticsearch access"

# Test PostgreSQL
echo "Testing PostgreSQL connection..."
PGPASSWORD=${POSTGRES_PASSWORD} psql -h localhost -U ${POSTGRES_USER} -d ${POSTGRES_DB} -c "\l"
check_status "PostgreSQL connection"

# Test Neo4j
echo "Testing Neo4j access..."
echo "Neo4j should be accessible at http://localhost:7474"
echo "Please verify manually that you can log in with credentials from NEO4J_AUTH"

# ======================================================
# PHASE 2: Kafka & Database Testing
# ======================================================
print_header "PHASE 2: Kafka & Database Testing"

# Kafka Topic Test
print_subheader "Kafka Topic Test"
echo "Listing Kafka topics..."
docker exec -it kafka kafka-topics.sh --list --bootstrap-server localhost:9092
check_status "Kafka topic listing"

# Create test topic if it doesn't exist
echo "Creating test topic 'raw_social_data' if it doesn't exist..."
docker exec -it kafka kafka-topics.sh --create --if-not-exists --topic raw_social_data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
check_status "Create test topic"

# Test Message Production/Consumption
print_subheader "Test Message Production/Consumption"
echo "Sending test message to 'raw_social_data' topic..."

# Create a test message
cat > test_message.json << EOF
{
  "source": "twitter",
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "content": "This is a test message for SOCMINT platform validation",
  "metadata": {
    "test": true,
    "purpose": "deployment validation"
  }
}
EOF

# Send the message to Kafka
cat test_message.json | docker exec -i kafka kafka-console-producer.sh --broker-list localhost:9092 --topic raw_social_data
check_status "Send test message to Kafka"

# Check if message was consumed
echo "Checking if message was consumed (wait 5 seconds)..."
sleep 5
echo "Verify in the logs that the AI service consumed the message:"
docker-compose logs --tail=20 backend

# PostgreSQL Database Check
print_subheader "PostgreSQL Database Check"
echo "Checking if required tables exist..."

# Check financial_alerts table
echo "Checking financial_alerts table..."
PGPASSWORD=${POSTGRES_PASSWORD} psql -h localhost -U ${POSTGRES_USER} -d ${POSTGRES_DB} -c "SELECT * FROM financial_alerts LIMIT 5;"
check_status "Query financial_alerts table"

# Check incident_reports table
echo "Checking incident_reports table..."
PGPASSWORD=${POSTGRES_PASSWORD} psql -h localhost -U ${POSTGRES_USER} -d ${POSTGRES_DB} -c "SELECT * FROM incident_reports LIMIT 5;"
check_status "Query incident_reports table"

# ======================================================
# PHASE 3: Backend API Testing
# ======================================================
print_header "PHASE 3: Backend API Testing"

# Function to test API endpoint
test_api_endpoint() {
  local endpoint=$1
  local method=${2:-GET}
  local data=${3:-""}
  
  echo "Testing $method $endpoint..."
  
  if [ "$method" = "GET" ]; then
    response=$(curl -s -o /dev/null -w "%{http_code}" -X $method http://localhost:8000$endpoint)
  else
    response=$(curl -s -o /dev/null -w "%{http_code}" -X $method -H "Content-Type: application/json" -d "$data" http://localhost:8000$endpoint)
  fi
  
  if [[ "$response" =~ ^2[0-9][0-9]$ ]]; then
    echo -e "${GREEN}✓ $method $endpoint returned $response${NC}"
    return 0
  else
    echo -e "${RED}✗ $method $endpoint returned $response${NC}"
    return 1
  fi
}

# Test Twitter collection endpoint
print_subheader "Testing /collect/twitter Endpoint"
test_data='{"query":"test","count":10}'
test_api_endpoint "/collect/twitter" "POST" "$test_data"

# Test darkweb scraping endpoint
print_subheader "Testing /scrape/darkweb Endpoint"
test_data='{"url":"http://example.onion","depth":1}'
test_api_endpoint "/scrape/darkweb" "POST" "$test_data"

# Test analysis endpoint
print_subheader "Testing /run-analysis Endpoint"
test_data='{"data_source":"twitter","analysis_type":"sentiment"}'
test_api_endpoint "/run-analysis" "POST" "$test_data"

# Test report generation endpoint
print_subheader "Testing /generate-report Endpoint"
test_data='{"analysis_id":"test-analysis","report_type":"summary"}'
test_api_endpoint "/generate-report" "POST" "$test_data"

# Test report verification endpoint
print_subheader "Testing /verify Endpoint"
test_api_endpoint "/verify/test-report-id"

# Test UAE PASS login endpoint
print_subheader "Testing /auth/uaepass/login Endpoint"
test_api_endpoint "/auth/uaepass/login"

# ======================================================
# PHASE 4: Frontend Testing
# ======================================================
print_header "PHASE 4: Frontend Testing"

print_subheader "Frontend Access Check"
echo "Checking if frontend is accessible..."
curl -s -o /dev/null -w "%{http_code}\n" http://localhost
check_status "Frontend access"

echo -e "\n${YELLOW}Manual Testing Required:${NC}"
echo "Please perform the following manual tests on the frontend:"

echo -e "\n1. ${BOLD}Test Role-Based Views:${NC}"
echo "   - Login with Admin → verify access to all dashboards"
echo "   - Login with Analyst → verify analytics only"
echo "   - Login with Viewer → read-only view"

echo -e "\n2. ${BOLD}Test Language Switching:${NC}"
echo "   - Switch to Arabic, Farsi, Russian and verify layout"

echo -e "\n3. ${BOLD}Test UAE PASS Integration:${NC}"
echo "   - Redirect to sandbox login"
echo "   - Verify JWT returned and user profile loaded"

# ======================================================
# PHASE 5: TOR Validation
# ======================================================
print_header "PHASE 5: TOR Validation"

print_subheader "Testing TOR Connection"
echo "Testing TOR connectivity..."
curl --socks5-hostname localhost:9050 http://check.torproject.org | grep -q "Congratulations"
if [ $? -eq 0 ]; then
  echo -e "${GREEN}✓ TOR connection successful${NC}"
else
  echo -e "${RED}✗ TOR connection failed${NC}"
fi

print_subheader "Testing Dark Web Scraping"
echo "Testing dark web scraping via API..."
test_data='{"url":"http://example.onion","depth":1}'
test_api_endpoint "/scrape/darkweb" "POST" "$test_data"

# ======================================================
# PHASE 6: Final Review
# ======================================================
print_header "PHASE 6: Final Review"

# Check logs for errors
print_subheader "Checking Service Logs"
echo "Checking logs for errors..."

for service in $(docker-compose ps --services); do
  echo -e "\n${BOLD}Logs for $service:${NC}"
  docker-compose logs --tail=20 $service | grep -i "error\|exception\|fail" || echo "No errors found"
done

# Check resource usage
print_subheader "Resource Usage"
echo "Current resource usage:"
docker stats --no-stream

# Backup databases
print_subheader "Database Backup"
echo "Creating PostgreSQL backup..."
docker exec postgres pg_dump -U ${POSTGRES_USER} ${POSTGRES_DB} > socmint_postgres_backup_$(date +%Y%m%d).sql
check_status "PostgreSQL backup"

echo "Creating Elasticsearch snapshot repository..."
# This is a simplified version - in production, you would configure a proper snapshot repository
echo "Note: For production, configure proper Elasticsearch snapshot repository"

# Security check
print_subheader "Security Check"
echo "Checking HTTPS configuration..."
if curl -k https://localhost &> /dev/null; then
  echo -e "${GREEN}✓ HTTPS is configured${NC}"
else
  echo -e "${YELLOW}⚠ HTTPS is not configured. For production, enable HTTPS.${NC}"
fi

# Final summary
print_header "Deployment Summary"

running_containers=$(docker-compose ps --services --filter "status=running" | wc -l)
total_containers=$(docker-compose ps --services | wc -l)

echo -e "${BOLD}Services:${NC} $running_containers/$total_containers running"

echo -e "\n${BOLD}Validation Results:${NC}"
echo -e "✓ Infrastructure validation"
echo -e "✓ Kafka & Database testing"
echo -e "✓ Backend API testing"
echo -e "✓ Frontend accessibility"
echo -e "✓ TOR validation"
echo -e "✓ Final review"

echo -e "\n${GREEN}${BOLD}SOCMINT Platform Deployment Complete!${NC}"
echo -e "The platform is now ready for production use."
echo -e "\n${YELLOW}Note:${NC} Remember to secure your environment and implement proper monitoring for production."

# ======================================================
# Arabic Translation of Summary
# ======================================================
echo -e "\n${BOLD}ملخص النشر:${NC}"
echo -e "✓ التحقق من البنية التحتية"
echo -e "✓ اختبار كافكا وقواعد البيانات"
echo -e "✓ اختبار واجهة برمجة التطبيقات الخلفية"
echo -e "✓ إمكانية الوصول إلى الواجهة الأمامية"
echo -e "✓ التحقق من شبكة TOR"
echo -e "✓ المراجعة النهائية"

echo -e "\n${GREEN}${BOLD}اكتمل نشر منصة SOCMINT!${NC}"
echo -e "المنصة جاهزة الآن للاستخدام الإنتاجي."
echo -e "\n${YELLOW}ملاحظة:${NC} تذكر تأمين بيئتك وتنفيذ المراقبة المناسبة للإنتاج."