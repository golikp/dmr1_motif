from Bio import SeqIO
from Bio.Seq import Seq
motif = "ATAATAATAATAAT"
for seq15S in SeqIO.parse("15S.fas", "fasta"):
	print (seq15S.id, seq15S.seq.count(motif))
