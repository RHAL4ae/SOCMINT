# SOCMINT Infrastructure Validation Script (PowerShell)

Write-Host "Starting SOCMINT Docker Compose stack..." -ForegroundColor Cyan
docker-compose up -d

Write-Host "`nChecking container status..." -ForegroundColor Cyan
docker-compose ps

Write-Host "`nInspecting Docker network 'socmint_network'..." -ForegroundColor Cyan
docker network inspect socmint_network

Write-Host "`nTesting service endpoints..." -ForegroundColor Cyan

# Frontend
Write-Host "Frontend (http://localhost):"
Invoke-WebRequest http://localhost | Select-Object -ExpandProperty StatusDescription

# Backend API
Write-Host "`nBackend API (http://localhost:8000/health):"
Invoke-WebRequest http://localhost:8000/health | Select-Object -ExpandProperty StatusDescription

# Elasticsearch
Write-Host "`nElasticsearch (http://localhost:9200/_cat/indices):"
Invoke-WebRequest http://localhost:9200/_cat/indices | Select-Object -ExpandProperty Content

# Neo4j
Write-Host "`nNeo4j (http://localhost:7474):"
Start-Process "http://localhost:7474"

# PostgreSQL
Write-Host "`nPostgreSQL (port 5432):"
Write-Host "Use pgAdmin, DBeaver, or psql to connect and check tables."

# Kafka Topic List
Write-Host "`nListing Kafka topics..."
docker exec -it kafka bash -c "kafka-topics.sh --list --bootstrap-server localhost:9092"

# PostgreSQL Table Checks (if psql is installed)
Write-Host "`nChecking PostgreSQL tables (requires psql)..."
# Replace <user> and <db> with your actual credentials
# psql -h localhost -U <user> -d <db> -c "SELECT * FROM financial_alerts;"
# psql -h localhost -U <user> -d <db> -c "SELECT * FROM incident_reports;"

# Backend API Endpoints
Write-Host "`nTesting backend API endpoints..."
$endpoints = @(
    "collect/twitter",
    "scrape/darkweb",
    "run-analysis",
    "generate-report",
    "verify/1", # Replace 1 with a valid report_id
    "auth/uaepass/login"
)
foreach ($ep in $endpoints) {
    $url = "http://localhost:8000/$ep"
    Write-Host "Testing $url"
    try {
        Invoke-WebRequest $url | Select-Object -ExpandProperty StatusDescription
    } catch {
        Write-Host "Failed: $url" -ForegroundColor Red
    }
}

# TOR Validation (if running on port 9050)
Write-Host "`nTesting TOR connection (if TOR is running on port 9050)..."
try {
    Invoke-WebRequest -Uri "http://check.torproject.org" -Proxy "socks5://localhost:9050" | Select-Object -ExpandProperty Content
} catch {
    Write-Host "TOR test failed or not running." -ForegroundColor Yellow
}

Write-Host "`nTo check logs, run: docker-compose logs <service>"
Write-Host "To check resource usage, run: docker stats"
Write-Host "For database backup, use pgAdmin or pg_dump for PostgreSQL and elasticdump for Elasticsearch."
Write-Host "`nSOCMINT infrastructure validation complete!" -ForegroundColor Green