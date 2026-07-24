# Analysis Pipeline

## Purpose

The analysis pipeline transforms a repository into reusable, traceable knowledge and then applies that knowledge to a capability. Each stage has a narrow responsibility and communicates through explicit inputs and outputs.

## Pipeline Flow

Repository Loader → Repository Snapshot → Discovery Engine → Raw Facts → Normalization Engine → Knowledge Graph → Query Engine → Semantic Analysis → Capability Engine

The Repository Snapshot remains the source-of-record boundary for every result. Facts, knowledge, semantic conclusions, and capability output retain provenance to that snapshot.

## Repository Loader

**Purpose:** Obtain repository material for analysis from an authorized source.

**Inputs:** A repository reference and collection request.

**Outputs:** Repository material and collection context for snapshot creation.

**Responsibilities:** Resolve the requested repository state, obtain accessible source material, and report acquisition limitations.

**Must not do:** Interpret source content, classify repository elements, infer relationships, or produce findings.

### Contract Boundary

The Repository Loader contract accepts a Repository Reference and a Repository
Snapshot Request, then returns a Repository Snapshot. The application service
depends on this contract without selecting a repository provider or performing
repository operations. Concrete loading mechanisms belong to future adapters.

The first adapter is local-only. It validates a local repository directory and
records its relative POSIX file and directory paths while pruning `.git`,
`__pycache__`, and `.venv`. It does not read file contents or perform analysis.

## Repository Snapshot

**Purpose:** Establish the stable, point-in-time analysis boundary.

**Inputs:** Repository material and collection context from the Repository Loader.

**Outputs:** A scoped Snapshot containing admitted Source Artifacts, Source Locations, and coverage limitations.

**Responsibilities:** Record repository identity when available, scope, admitted material, exclusions, and unreadable or unsupported material.

**Must not do:** Discover semantic meaning, generate Raw Facts, make recommendations, or mix different repository states.

## Discovery Engine

**Purpose:** Observe repository material and extract direct, analyzer-neutral observations.

**Inputs:** A Repository Snapshot.

**Outputs:** Raw Facts with provenance to Source Artifacts and Source Locations.

**Responsibilities:** Identify observable structures and content characteristics within the snapshot, while preserving the source basis of each observation.

**Must not do:** Resolve competing representations into one canonical form, infer unsupported meaning, generate user-facing conclusions, or access material outside the snapshot.

### Initial Contract

The initial Discovery Service consumes only the path inventory already present
in a Repository Snapshot. It emits `FoundFile` and `FoundDirectory` Raw Facts
in deterministic relative-POSIX-path order. It does not access the filesystem,
call a Repository Loader, detect technologies, or apply rules.

## Raw Facts

**Purpose:** Preserve direct observations before they are reconciled or interpreted.

**Inputs:** Observations from the Discovery Engine and their snapshot provenance.

**Outputs:** Traceable, unnormalized observations for the Normalization Engine.

**Responsibilities:** Retain the observed value, source basis, discovery context, and known limitations without implying higher-level meaning.

**Must not do:** Act as the canonical Knowledge Graph, hide conflicting observations, rank importance, or present recommendations.

## Normalization Engine

**Purpose:** Reconcile Raw Facts into consistent representations suitable for shared knowledge.

**Inputs:** Raw Facts and their provenance.

**Outputs:** Normalized facts and explicit normalization limitations for graph construction.

**Responsibilities:** Apply consistent terminology, identity rules, and relationship representations while retaining traceability to the original facts.

**Must not do:** Discard material ambiguity without recording it, invent missing facts, perform capability-specific reasoning, or generate presentation output.

### Initial Contract

The MVP normalization layer evaluates independent path-based rules over Raw Facts
and emits immutable, source-traceable knowledge entities. It recognizes only the
documented file and directory patterns, reads no file contents, and performs no
provider, README, or repository access.

## Knowledge Graph

**Purpose:** Represent the reusable, connected Repository Knowledge derived from one snapshot.

**Inputs:** Normalized facts, relationships, provenance, and limitations.

**Outputs:** Addressable Knowledge Items, directed Relationships, and evidence links.

**Responsibilities:** Preserve repository facts, classifications, relationships, completeness limits, and evidence references for reuse by multiple consumers.

**Must not do:** Depend on a specific AI provider, contain generated documents, silently combine snapshots, or make audience-specific recommendations.

## Query Engine

**Purpose:** Retrieve relevant, explainable slices of the Knowledge Graph for a stated question or analysis need.

**Inputs:** A query request, Knowledge Graph, and applicable analysis scope.

**Outputs:** Relevant Knowledge Items, Relationships, Evidence references, and retrieval limitations.

**Responsibilities:** Select knowledge according to explicit criteria and preserve the provenance needed to explain the result.

**Must not do:** Change the Knowledge Graph, create unsupported facts, hide retrieval limits, or decide the final capability response.

## Semantic Analysis

**Purpose:** Interpret queried knowledge for a declared analysis purpose.

**Inputs:** Query results, their Evidence, and an analysis purpose.

**Outputs:** Findings with supporting Knowledge Items, Evidence, and stated limitations.

**Responsibilities:** Assess relevance, connect related knowledge, and express bounded conclusions that remain traceable to the snapshot.

**Must not do:** Treat inference as direct observation, replace evidence with narrative, mutate shared knowledge, or render a final user-facing artifact.

## Capability Engine

**Purpose:** Produce a capability-specific result from semantic conclusions and traceable repository knowledge.

**Inputs:** Findings, supporting knowledge and evidence, and a capability request.

**Outputs:** A result appropriate to the requested capability, with available traceability.

**Responsibilities:** Apply the requested capability's presentation or decision policy while respecting scope, provenance, and limitations. README generation is a future example of such a capability.

**Must not do:** Redefine Repository Knowledge, bypass evidence, mutate the Repository Snapshot, or introduce provider-specific assumptions into the shared pipeline.

## Cross-Cutting Constraints

- Every derived result is attributable to one Repository Snapshot.
- Each stage preserves known coverage and uncertainty limits.
- Stages communicate through their declared outputs and do not take over another stage's responsibility.
- The shared stages remain provider-agnostic and reusable by future capabilities.
