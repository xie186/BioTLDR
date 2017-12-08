# TopHat - A spliced read mapper for RNA-Seq 

  - Create index 
  `bowtie2-build ref.fa ref_bowtie2index`

  - Alignment of RNA-seq reads
  `tophat ref_bowtie2index read_1.fq read2.fq -o tophat_out`
   
