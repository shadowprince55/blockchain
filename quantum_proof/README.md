
### The 3 day lockdown, oops hackathon:
Since quantum computing is awesome, magical and super scary at the same time, we tried to build a quantum secure variation of a blockchain for a national hackathon called M#. We made it to the semi finals, from among 300 teams but unfortunately got rejected because we were massively sleep-deprived and completely incoherent during our presentation. Nevertheless, we had a lot of fun, realized that there was a lot of exciting fun stuff to learn and made lots of friends! So yay, to the unicorn ending!

### Note to self: 
Start pulling 2 consecutive all-nighters and then giving a Ted-Talk on friggin day 3. 

### About:
This repo is in a .rar format because my laptop cannot handle the upload of the python-env that we had created. It is a variation of another project in this repository, except that it hashes and verifies in a way that is probably quantum-proof. I say 'probably', because I cannot afford to be a pompous idiot, when speaking about supposedly mystical unhackable systems...
Before I go down another rabbit-hole, here is how we tried to made it quantum-secure:
1. Integrating quantum random number generation along with the data being hashed to get the required nonce.
1. Using BB84 to distribute the public key to ensure that tampering did not take place.
1. Using Falcon(because, thank the heavens, it integrates with python) to verify signatures.


### Gracias muchas:
Thanks to Sujeet, for pulling through it all, and to Utkarsh and Rashi for being awesome juniors!
