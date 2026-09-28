# Separation of Duties for GitDataQuality

## Maker Role: DataPlatformEngineer
DataPlatformEngineer who designs ingestion DAGs, transformation models, and warehouse tables.

## Checker Role: DataGovernanceLead
DataGovernanceLead who validates data quality scores, anomaly alerts, and schema integrity.

## Dual-Control Verification Pipeline
1. Profile incoming batch and streaming dataset column statistics.
2. Measure null-value percentages against configured column SLA thresholds.
3. Compute statistical z-scores and interquartile ranges across numeric distributions.
4. Generate data quality assertions and gate automated pipeline promotion.
