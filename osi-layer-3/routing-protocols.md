# Routing Protocols

Routers operate on Layer 3.

They ignore Layer 2 addresses for decision making.

* Multiple Collision Domains
* Multiple Broadcast Domains

Routing protocols allow neighboring routers to collaborate dynamically.

There are two main types: distance-vector and link-state.

Distance-vector protocols attempt to calculate the "distance" between networks. Usually this is the total number of hops, or the sum of all weights on a path.

Link-state protocols are more concerned with speed and current state of the connections. A longer path with a faster travel time will be prioritized over a path with less hops.

Hybrid protocols also exist.

Each routing protocol defines the metric\(s\) used to calculate weights.



Weights are calculated individually on each router for each known network. The weight for the exact same network may be different on different routers.



Static routes may also be set, with arbitrary weights, by a network administrator.



The “best” weight is used by a router to decide where to send the packet. Weights are usually represented as an integer, and the lowest number is considered best.

