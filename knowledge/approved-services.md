# Approved External Services

Domains listed here are pre-approved for the PHI/PII transmission guard
(hook S-3 in `hooks/safety-guard.sh`). Outbound HTTP requests to domains
NOT on this list trigger a safety warning — they are not blocked, but the
user is prompted to verify data classification before proceeding.

To add a domain: submit a PR to this file with the service name and
business justification.

## Cloud Infrastructure

*.microsoft.com         # Microsoft 365
*.azure.com             # Azure cloud services
*.windows.net           # Azure storage and services
*.sharepoint.com        # SharePoint Online
*.google.com            # Google Workspace
*.googleapis.com        # Google Cloud APIs
*.gstatic.com           # Google static content

## Developer Tools

*.github.com            # GitHub
*.githubusercontent.com  # GitHub content CDN
*.atlassian.net         # Atlassian (Jira, Confluence)
*.atlassian.com         # Atlassian
*.datadoghq.com         # Datadog monitoring

## Business Applications

*.salesforce.com        # Salesforce CRM
*.hubspot.com           # HubSpot
*.slack.com             # Slack
*.okta.com              # Okta SSO
*.1password.com         # 1Password
*.zoom.us               # Zoom

## AI / API Services

api.anthropic.com       # Anthropic Claude API

## Security and Compliance

api.vanta.com           # Vanta
*.ironcladapp.com       # Ironclad contracts

## Data and Analytics

*.snowflakecomputing.com  # Snowflake

## Communication

*.twilio.com            # Twilio

## Evermore Internal Services

*.azurewebsites.net     # Azure Functions (Evermore services)
*.azurecontainerapps.io # Azure Container Apps (Evermore services)

## Local Development

localhost               # Local development
127.0.0.1               # Loopback
