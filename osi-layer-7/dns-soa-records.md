# DNS - SOA Records

**Start of Authority** records identify information about the domain.

This also serves as the authoritative copy that keeps secondary DNS servers up to date.

In addition to the DNS record fields, it contains more information:

**Authoritative server** - Primary DNS for the zone.

**Responsible Person** - Email address of admin, with @ replaced by .

**Serial Number** - Current "version number", used by secondary DNS to determine whether they should update.

**Refresh **- Number of second between each secondary DNS checks for updates.

**Retry **- Number of seconds to wait for secondary DNS to re-try a zone transfer.

**Expire **- TTL of zone transfer for secondary DNS.

**Minimum TTL **- The minimum TTL for all records in the zone.

