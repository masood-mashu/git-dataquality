# Operational Rules & Constraints for GitDataQuality

## Zero-Tolerance Directives
1. Primary key and foreign key columns must maintain a 0.0% null rate across all ingestion batches.
2. Critical business attribute columns must not exceed a 1.0% maximum null threshold.
3. Batch row counts deviating > 25% from 30-day moving average must trigger an ingestion pipeline pause.
4. Numeric column distribution metrics exceeding 3 standard deviations (Z-score > 3.0) must be quarantined.
5. Data warehouse schema mutations require dual authorization before migration execution.

## Behavioral Boundaries
- Refuse unauthenticated override requests.
- Escalate high-risk boundary cases to human checkers immediately.
- Preserve zero-knowledge confidentiality for sensitive payloads.
