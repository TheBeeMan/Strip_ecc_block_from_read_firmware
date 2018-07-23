### Why
It seem common that we would try all kinds of programmer to dump flash/e2rom memory using a physical way, however some weird things occurs, one of them is that we can not extract firmware using binwalk since the way we dump firmware data using a programmer seems to be wrong.

### How
It should be paid attention on that option which imply whether we read ECC data or not when using a programmer, this phenomenor vary with programer, once you read ECC data and embedded it into the whole fimware, you need recompose those data with a tool which function as a hex data stripper.
