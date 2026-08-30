# Framework adapter template

Define the domain capabilities you actually need, then implement them per framework. Keep framework player objects out of core modules.

Suggested normalized interface:
- `getPlayer(source) -> { id, source, job, groups } | nil`
- `hasPermission(source, capability) -> boolean`
- `getBalance(source, account) -> number`
- `removeMoney(source, account, amount, reason) -> ok, error`
- `addItem(source, item, count, metadata) -> ok, error`
- `notify(source, message, kind)`

Do not force all frameworks into semantics they do not share; expose capability-specific adapters where needed.
