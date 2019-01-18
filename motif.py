from Bio import SeqIO
from Bio.Seq import Seq
#change motlen here to set the minimum motif length
motlen = 14
Scer = SeqIO.read("Scer.fas", "fasta").seq.upper()
Spar = SeqIO.read("Spar.fas", "fasta").seq.upper()
Sbay = SeqIO.read("Sbay.fas", "fasta").seq.upper()
Smik = SeqIO.read("Smik.fas", "fasta").seq.upper()
Skud = SeqIO.read("Skud.fas", "fasta").seq.upper()
Cgla = SeqIO.read("Cgla.fas", "fasta").seq.upper()
print ("For motifs of ", motlen, " nt, in cer, par, mik, kud, bay, Cgla")
for pos in range (len(Scer) - motlen + 1):
    motif = Scer[pos:pos + motlen]
    cons = Scer.count(motif) * Spar.count(motif) * Smik.count(motif) * Skud.count(motif) * Sbay.count(motif)
#    if (cons > 0) & (Cgla.count(motif) == 0) & (Spar.count(motif) > Sbay.count(motif)) & (Scer.count(motif) > Sbay.count(motif)) :
    if (cons > 0) & (Cgla.count(motif) == 0) & (Scer.count(motif) > Sbay.count(motif)) :
        print ("Motif ",motif," at ", pos, Scer.count(motif), Spar.count(motif), Smik.count(motif), Skud.count(motif), Sbay.count(motif), Cgla.count(motif))

