# Routing Matrix

Use this as a secondary router reference, not as an instruction to load everything.

| Signal | Primary skills | Often pair with |
|---|---|---|
| `fxmanifest.lua`, dependencies, new resource | fivem-resource-architecture | fivem-compatibility, fivem-release |
| `.lua`, threads, vectors | fivem-cfxlua | fivem-native-expert, fivem-performance |
| native/hash/task/entity call | fivem-native-expert | gameplay specialist, fivem-onesync |
| `TriggerServerEvent`, `RegisterNetEvent` | fivem-events, fivem-server-authority | fivem-security |
| network entity/NetID | fivem-onesync, fivem-entity-lifecycle | fivem-statebags |
| `Entity(...).state`, `GlobalState` | fivem-statebags | fivem-onesync |
| routing bucket/instance | fivem-routing-buckets | fivem-security, fivem-entity-lifecycle |
| NUI / `ui_page` | fivem-nui | fivem-nui-bridge, fivem-ui-design |
| React/Vue/Svelte/Tailwind UI | fivem-frontend-stack, fivem-ui-design | fivem-nui-bridge, fivem-performance |
| DUI/runtime texture | fivem-dui | fivem-entity-lifecycle, fivem-performance |
| SQL/oxmysql | fivem-database | framework skill, fivem-security |
| Qbox/QBCore/ESX | matching framework skill | fivem-framework-adapter |
| ox_lib/target/inventory | fivem-ox-ecosystem | fivem-interactions, fivem-database |
| vehicles | fivem-vehicles | fivem-onesync, fivem-entity-lifecycle |
| convoy/autodrive | fivem-vehicle-ai | fivem-native-expert, fivem-onesync |
| NPCs | fivem-peds-ai | fivem-native-expert, fivem-entity-lifecycle |
| target/zones | fivem-interactions | fivem-zones-raycasts, fivem-security |
| exploit/cheat concern | fivem-security | fivem-server-authority, fivem-events |
| high resmon / lag | fivem-performance | fivem-observability, relevant domain skill |
| error/regression | fivem-fix, fivem-debugging | fivem-testing |
| release-ready review | fivem-audit, fivem-code-review | fivem-testing, fivem-release |
