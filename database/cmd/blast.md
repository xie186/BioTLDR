# BLAST - Basic Local Alignment Search Tool 

  - Building a BLAST database with local sequences
    `makeblastdb -in mydb.fsa -parse_seqids -dbtype nucl`

  - Align protein sequence again a protein database.
    `blastp -db database_name -query input_file -out output.blast.txt`
