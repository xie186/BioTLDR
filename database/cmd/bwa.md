   # bwa - Burrows-Wheeler Alignment Tool

   > BWA is a software package for mapping low-divergent sequences against a large reference genome, such as the human genome. It consists of three algorithms: BWA-backtrack, BWA-SW and BWA-MEM.

  - Index database sequences in the FASTA format:
    `bwa index ref.fa`

  - Align 70bp-1Mbp query sequences with the BWA-MEM algorithmi (faster and more accurate than BWA-backtrack and BWA-SW). 
     `bwa mem ref.fa reads.fq`

  - Align reads less than 70bp for SE reads.
    `bwa aln ref.fa short_read.fq > aln_sa.sai`
    `bwa samse ref.fa aln_sa.sai short_read.fq > aln-se.sam`

  - Align reads less than 70bp for PE reads.
   `bwa aln ref.fa short_read1.fq > aln_sa1.sai`
   `bwa aln ref.fa short_read2.fq > aln_sa2.sai`
   `bwa sampe ref.fa aln_sa1.sai aln_sa2.sai read1.fq read2.fq > aln-pe.sam`
