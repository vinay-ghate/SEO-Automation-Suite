1. Full API Schema (Request/Response Models)
1.1 Authentication API
POST /auth/register

Request

{
  "email": "user@example.com",
  "password": "securepass123",
  "name": "John Doe"
}


Response

{
  "user_id": "uuid",
  "email": "user@example.com",
  "role": "manager"
}

POST /auth/login

Request

{
  "email": "user@example.com",
  "password": "securepass123"
}


Response

{
  "access_token": "jwt-token",
  "token_type": "Bearer",
  "expires_in": 3600
}

GET /auth/me

Response

{
  "user_id": "uuid",
  "email": "user@example.com",
  "role": "analyst",
  "created_at": "2024-01-01T10:00:00Z"
}

1.2 Project API
POST /projects

Request

{
  "name": "Client SEO",
  "domain": "example.com"
}


Response

{
  "project_id": "uuid",
  "name": "Client SEO",
  "domain": "example.com",
  "created_at": "2024-01-01T10:00:00Z"
}

1.3 Meta Tag Generator API
POST /meta/generate

Request

{
  "project_id": "uuid",
  "url": "https://example.com/page",
  "content": null
}


Response

{
  "meta_id": "uuid",
  "variants": [
    {
      "title": "Best Product Page 2024 | Example",
      "description": "Explore the best product with features, pricing..."
    },
    {
      "title": "Example Product - Updated Guide",
      "description": "Get complete insights into..."
    }
  ],
  "scores": {
    "variant_1": {"ctr_score": 0.85, "keyword_score": 0.90},
    "variant_2": {"ctr_score": 0.80, "keyword_score": 0.88}
  },
  "created_at": "2024-01-01T10:00:00Z"
}

1.4 Broken Link Finder API
POST /links/scan

Request

{
  "project_id": "uuid",
  "domain": "example.com"
}


Response

{
  "scan_id": "uuid",
  "status": "queued"
}

GET /links/{project_id}

Response

{
  "project_id": "uuid",
  "broken_links": [
    {
      "source_url": "https://example.com/about",
      "broken_url": "https://example.com/old-page",
      "status_code": 404
    }
  ]
}

1.5 Competitor NLP Analyzer API
POST /competitor/analyze

Request

{
  "project_id": "uuid",
  "competitor_urls": [
    "https://competitor.com/page",
    "https://competitor2.com/article"
  ],
  "target_url": "https://example.com/target"
}


Response

{
  "analysis_id": "uuid",
  "similarity_score": 0.73,
  "keyword_gap": ["best tools", "pricing guide", "how to use"],
  "topic_clusters": [
    {
      "cluster_name": "Buying Intent",
      "topics": ["pricing", "product comparison"]
    }
  ]
}

1.6 SERP Comparator API
POST /serp/compare

Request

{
  "project_id": "uuid",
  "keywords": ["best seo tools"],
  "location": "India"
}


Response

{
  "comparison_id": "uuid",
  "results": [
    {
      "keyword": "best seo tools",
      "rankings": [
        {"domain": "example.com", "position": 5},
        {"domain": "competitor.com", "position": 2}
      ]
    }
  ]
}

2. Complete Database Schema
2.1 Table: users
id              UUID PK
email           TEXT UNIQUE
password_hash   TEXT
role            TEXT
created_at      TIMESTAMP

2.2 Table: projects
id          UUID PK
name        TEXT
domain      TEXT
owner_id    UUID FK -> users.id
created_at  TIMESTAMP

2.3 Table: meta_tags
id               UUID PK
project_id       UUID FK -> projects.id
url              TEXT
input_content    TEXT
variants         JSONB
scores           JSONB
created_at       TIMESTAMP

2.4 Table: broken_links
id              UUID PK
project_id      UUID FK -> projects.id
source_url      TEXT
broken_url      TEXT
status_code     INT
first_detected  TIMESTAMP
last_detected   TIMESTAMP

2.5 Table: competitor_analysis
id                 UUID PK
project_id         UUID FK -> projects.id
target_url         TEXT
competitor_urls    JSONB
similarity_score   FLOAT
keyword_gap        JSONB
topic_clusters     JSONB
created_at         TIMESTAMP

2.6 Table: serp_history
id            UUID PK
project_id    UUID FK -> projects.id
keyword       TEXT
domain        TEXT
rank          INT
detected_at   TIMESTAMP

2.7 Table: schedules
id              UUID PK
project_id      UUID FK -> projects.id
task_type       TEXT
cron_expression TEXT
enabled         BOOLEAN
created_at      TIMESTAMP

3. Fully Structured Python Project Architecture

Production-grade structure with modular services

seo-automation-suite/
│
├── app/
│   ├── main.py                         # FastAPI entrypoint
│   ├── config.py
│   ├── dependencies.py
│   ├── routers/
│   │   ├── auth.py
│   │   ├── projects.py
│   │   ├── meta.py
│   │   ├── links.py
│   │   ├── competitor.py
│   │   └── serp.py
│   │
│   ├── services/
│   │   ├── meta_generator.py           # Gemini agent workflows
│   │   ├── broken_link_service.py
│   │   ├── competitor_service.py
│   │   ├── serp_service.py
│   │   └── scheduler.py
│   │
│   ├── workers/
│   │   ├── celery_app.py
│   │   ├── tasks/
│   │   │   ├── meta_tasks.py
│   │   │   ├── link_tasks.py
│   │   │   ├── competitor_tasks.py
│   │   │   └── serp_tasks.py
│   │
│   ├── nlp/
│   │   ├── embeddings.py               # Gemini embedding pipeline
│   │   ├── similarity.py
│   │   └── clustering.py
│   │
│   ├── integrations/
│   │   ├── apify_client.py
│   │   ├── gemini_client.py
│   │   └── email_client.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── meta.py
│   │   ├── competitor.py
│   │   ├── links.py
│   │   └── serp.py
│   │
│   ├── database/
│   │   ├── session.py
│   │   ├── base.py
│   │   └── migrations/
│   │
│   └── utils/
│       ├── scraper_utils.py
│       ├── scoring.py
│       └── validators.py
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── load/
│
├── docker-compose.yml
├── requirements.txt
└── README.md

4. Sequence Diagrams (System-Level)

Below are text-based UML-style diagrams (suitable for documentation).

4.1 Meta Tag Generator Workflow
User → API → Worker → Apify → Worker → Gemini → Worker → API → User

1. User submits URL
2. API stores task and sends to worker
3. Worker triggers Apify scraper
4. Apify returns cleaned content
5. Worker sends content to Gemini (draft → refine → optimize)
6. Worker stores outputs in DB
7. API returns meta tag variants to user

4.2 Broken Link Finder Workflow
User → API → Worker → Apify → Worker → DB → API → User

1. User initiates scan request
2. API queues task
3. Worker launches Apify crawler
4. Worker processes results (HTTP checks)
5. Worker stores broken links in DB
6. User fetches scan report via API

4.3 Competitor NLP Analysis Workflow
User → API → Worker → Apify → Worker → Gemini Embeddings → Vector Store → Worker → API → User

1. User submits competitor URLs
2. API sends analysis job to worker
3. Worker triggers Apify scrapers
4. Worker extracts text + headings
5. Worker generates embeddings using Gemini
6. Worker stores vectors in pgvector/Milvus
7. Worker computes similarity + gaps
8. API returns structured analysis

4.4 SERP Comparator Workflow
User → API → Worker → Apify SERP Actor → Worker → DB → API → User

1. User submits keyword list
2. API queues SERP job
3. Worker calls Apify SERP actor
4. Worker normalizes results
5. Worker stores historical ranks
6. API returns comparison result
