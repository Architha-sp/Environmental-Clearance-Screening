
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from fastapi import Response

# Total screening requests
SCREENING_REQUESTS = Counter(
    "screening_requests_total",
    "Total number of screening requests",
    ["status"]
)

# Screening execution duration
SCREENING_DURATION = Histogram(
    "screening_duration_seconds",
    "Time taken to complete screening"
)

# Agent execution count
AGENT_EXECUTIONS = Counter(
    "agent_executions_total",
    "Total agent executions",
    ["agent_name", "status"]
)

# Agent tool calls
AGENT_TOOL_CALLS = Counter(
    "agent_tool_calls_total",
    "Total agent tool calls",
    ["agent_name", "tool_name"]
)

# Retry tracking
AGENT_RETRIES = Counter(
    "agent_retries_total",
    "Total agent retries",
    ["agent_name"]
)

# Active workers
ACTIVE_WORKERS = Gauge(
    "active_workers",
    "Number of currently active workers"
)

# Application uptime is best handled through process metrics.
def metrics_endpoint():
    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )
