# SRA Toolkit

  - Prints the first five spots (-X 5) to standard out (-Z)
  `fastq-dump -X 5 -Z SRR390728`

  - Produces two fastq files (--split-files) containing ".1" and ".2" read suffices (-I) for paired-end data. 
  `fastq-dump -I --split-files SRR390728`

  - Produces two (--split-files) fasta files (--fasta) with 60 bases per line ("60" included after --fasta).
    `fastq-dump --split-files --fasta 60 SRR390728`

   - Produces two fastq files (--split-files) that contain only aligned reads (--aligned; Note: only for files submitted as aligned data), with a quality offset of 64 (-Q 64) Please see the documentation on vdb-dump if you wish to produce fasta/qual data.

    `fastq-dump --split-files --aligned -Q 64 SRR390728`
  
