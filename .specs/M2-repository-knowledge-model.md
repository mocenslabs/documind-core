# M2: Repository Knowledge Model

## Objective

Define a provider-agnostic architecture contract for the Repository Knowledge Model before Domain-layer implementation begins.

## Scope

This milestone defines concepts and relationships only. It does not implement repository collection, analyzers, AI-provider integration, persistence, document generation, or presentation behavior.

## Conceptual Model

A Repository Snapshot is the scoped, point-in-time source of record. It contains Source Artifacts and Source Locations admitted to analysis.

Repository Knowledge is derived from one snapshot. It describes elements, classifications, and relationships. Evidence identifies snapshot material that supports a Knowledge Item or Finding. Findings interpret knowledge for a declared analysis purpose and retain their supporting references.

## Architectural Constraints

- The shared model is provider-agnostic.
- Derived data does not silently combine different snapshots.
- Scope, exclusions, unreadable material, and uncertainty are observable.
- Findings remain distinct from repository facts and source evidence.
- Traceability flows from findings to knowledge, evidence, source locations, and the originating snapshot.
- Multiple analyzers can use the shared model without coupling to each other or to presentation concerns.

## Acceptance Criteria

Future implementation is accepted when it:

1. Identifies the source snapshot for every derived knowledge element.
2. Exposes repository scope, admitted material, and collection limitations.
3. Distinguishes Source Artifacts from Source Locations.
4. Represents facts and directed relationships independently of documents and recommendations.
5. Allows one Knowledge Item to have one or more Evidence references.
6. Allows evidence to identify the Source Artifact and Source Location it references.
7. Distinguishes direct observation, derived support, and known incompleteness.
8. Allows a Finding to identify its purpose, supporting knowledge, evidence, and limitations.
9. Prevents a Finding from becoming the sole record of a repository fact.
10. Supports multiple analyzers without analyzer-specific concepts in the shared model.
11. Does not require a specific AI provider to create, inspect, or consume the model.
12. Can distinguish or invalidate derived results when their snapshot changes.
13. Conforms to the terminology and responsibilities in `docs/architecture`.
