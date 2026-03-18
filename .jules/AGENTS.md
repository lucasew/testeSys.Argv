# Agents Guidelines

## Environment and Tooling
- We use Python 2.x natively. Avoid forcing Python 3 compatibility or syntax changes unless strictly required for external reasons.
- Task runner: `mise` is used for environment setup and commands.
- We use `pytest` for unit testing.

## Error Handling
- The project MUST have a single, centralized error-reporting function (e.g. `reportError`, `captureException`, or equivalent). All code paths that handle unexpected errors MUST funnel through this function. Never call `console.error` or `Sentry.captureException` directly at the call site.
- No silent failures: Every `catch` block, every `.catch()`, every error callback that is not an expected/recoverable condition MUST call the centralized error-reporting function. "Out of scope" is not an excuse to swallow.

## Directory Layout
- `src/` -> Application source code
- `tests/` -> Unit and integration tests
