# DNS Resource Records

Within a zone file, records are kept. In its simplest form, a record is basically a single mapping between a resource and a name. These can map a domain name to an IP address, define the name servers for the domain, define the mail servers for the domain, etc.

### Resource Record Types

Different types of records contain different types of host information. For example, an Address record provides the name-to-address mapping for a given host, while a Start of Authority \(SOA\) record specifies the start of authority for a given zone.

A DNS zone must contain several types of resource records for DNS to function properly. Other records can be present, but the following are required for standard DNS:

* **Name server \(NS\)**---Binds a domain name with a hostname for a specific name server
  The DNS zone must contain NS records for each primary and secondary name server in the zone. The DNS zone must contain NS records to link the zone to higher- and lower-level zones within the DNS hierarchy.

* **Start of Authority \(SOA\)**---Indicates the start of authority for the zone.
  The name server must contain one SOA record specifying its zone of authority.

* **Canonical name \(CNAME\)**---Specifies the canonical or primary name for the owner. The owner name is an alias.

* **Address \(A\)**---Provides the IP address for the zone.



For example, the name server for a zone must contain the following:

* An SOA record identifying its zone of authority
* An NS record for the primary name server within the zone
* An NS record for each secondary name server within the zone
* An A record that maps each name server specified in the NS records to an IP address

### DNS Record Format

**Owner **- Name of domain

**TTL **- TTL in seconds

**Class **- Protocol family to use, almost always IN

**Type **- Type of record being returned

**RDATA **- Data of the record

