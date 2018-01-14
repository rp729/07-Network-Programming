# Dig - replacement for nslookup

Dig is a better DNS query tool. It will soon replace nslookup altogether. Comes standard for Linux and Unix.

#### **Syntax:** `dig [@nameserver] domain record-type [+short]`

#### **Normal Lookups:**

#### `dig gov.hackistan AAAA`

#### `dig gov.hackistan ANY`

#### **Ask google's DNS specifically:**

#### `dig @ns1.google.com gov.hackistan`

#### **Reverse lookup:**

#### `dig -x 314.42.13.37`

#### **Dig, but less verbose:**

#### `[user@localhostDesktop]$ dig +short google.com A google.com AAAA 216.58.218.206 2607:f8b0:4000:802::200e`

#### **Dig, commands:**

#### `dig -h`



