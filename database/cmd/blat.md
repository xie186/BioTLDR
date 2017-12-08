# BLAT - The BLAST-Like Alignment Tool

  - Align protein sequences to target protein sequences.
    `blat -t=prot -q=prot target_prot.fa query_prot.fa results_prot2prot.psl`

     -t=type     Database type.  Type is one of:
                 dna - DNA sequence
                 prot - protein sequence
                 dnax - DNA sequence translated in six frames to protein
               The default is dna
     -q=type     Query type.  Type is one of:
                 dna - DNA sequence
                 rna - RNA sequence
                 prot - protein sequence
                 dnax - DNA sequence translated in six frames to protein
                 rnax - DNA sequence translated in three frames to protein
               The default is dna

  - Align DNA sequences to target DNA sequences.
    `blat -t=dna -q=dna target_prot.fa query_prot.fa results_prot2prot.psl`
