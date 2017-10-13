# Sequence and Acknowledgements

Sequence numbers indicate the most recent piece of data sent.

Acknowledgement numbers indicate the next byte expected.

During the initial handshake:

* Host A randomly generates a sequence number.
* Host B will acknowledge A'sseqnumber, and generate a randomseqno of it's own.
* Host A will acknowledge B'sseqnumber and the connection is established.

With NO DATA transmitted \(e.g. keep alive packet, or a one-sided series of transactions\):

* A sender that is simplyACKingand not sending data of it's own, will re-use the same Sequence Number.
* Sequence Numbers may be re-ackeduntil other side actually sends some data.



During normal data transmission:

* Sequence numbers mark the beginning of most recent data sent. It starts at the random number chosen during the handshake and is cumulative.
* Acknowledgement numbers =seqnumber + datarecv'dsince last ACK + 1.



Errors will result in the Acknowledgement number being set to the last successfully received CONTIGUOUS block of data + 1.

* A sends 10 data, with aseqof 1, but B only receives 1-7, the Ack number will be 8.
* A sends 10 data, with aseqof 1, but B only receives 1 and 4-10, the Ack number will be 2.



