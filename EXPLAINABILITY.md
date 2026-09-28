# GitDataQuality Explainability Specification

This document provides a transparent, verifiable architectural breakdown of how **GitDataQuality** operates, processes input, makes decisions, and enforces security boundaries.

---

## 1. Input Data and Data Sources Used

GitDataQuality consumes database partition extracts, ETL/ELT pipeline logs, schema metadata catalogs, and column profiling statistics. These data sources include record row counts, column null-value percentages, numeric summary statistics, and partition ingestion timestamps. The agent ingests these inputs in raw JSON, CSV, and parquet metadata format and parses them into standardized data quality profiling metrics for downstream verification. Enterprise data SLA contracts and column constraint definitions are also monitored as sensitive data sources to ensure warehouse data hygiene is strictly maintained.

---

## 2. How It Decides and Reasoning Process

The decision making process follows a deterministic, five-stage analytical pipeline designed to eliminate ambiguity and hallucination. When a new data batch is ingested, the agent first evaluates column completeness using the null-rate-monitor tool to ensure that null proportions adhere to configured SLA thresholds. Next, the reasoning engine invokes the numerical-outlier-detector tool to compute standard deviation z-scores and detect distribution anomalies. Furthermore, partition volume stability is audited using the batch-volume-drift-checker tool against historical moving averages. Finally, the agent correlates all data quality metrics against predefined pipeline policies to issue a conclusive verdict of APPROVED, BLOCKED, or NEEDS_REVIEW alongside an automated quarantine report.

---

## 3. Constraints, Limitations, and Known Issues

GitDataQuality operates under strict operational constraints to prevent false positives and non-deterministic behavior across different agent frameworks. GitDataQuality operates under strict operational constraints to prevent corrupted data ingestion and silent pipeline degradation across analytical warehouses. The agent is deliberately limited to statistical schema profiling and threshold verification and cannot evaluate the subjective semantic truth of unstructured text fields. Another known issue and limitation is that multimodal binary payloads with compressed data may require secondary human review rather than autonomous blocking. Furthermore, the agent enforces a low temperature constraint of 0.1 to maintain strict predictability across all supported export frameworks.
