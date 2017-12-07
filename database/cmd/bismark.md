  Bismark - A tool to map bisulfite converted sequence reads and determine cytosine methylation states

  > A functional version of Bowtie or Bowtie2 is required. For BAM output Samtools is also required

  - Convert a specified reference genome into two different bisulfite converted versions and index them for alignments with Bowtie 2 (default), or Bowtie 1. 
    `bismark_genome_preparation ./data/reference/`

   - Alignment of the reads
     `bismark ./data/reference/ -1 read_1.fastq -2 read_2.fastq -o results_dir/`




