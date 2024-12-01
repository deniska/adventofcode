use 5.10.0;

my $f;
my @nums1;
my @nums2;
my %counts;

open $f, '<', @ARGV[0] || die 'file pls';

while(<$f>) {
    my @vals = split /\s+/, $_;
    push @nums1, @vals[0] + 0;
    push @nums2, @vals[1] + 0;
    $counts{@vals[1] + 0} += 1;
}

close $f;

my @snums1 = sort @nums1;
my @snums2 = sort @nums2;
my $d = 0;
my $s = 0;

for (my $i = 0; $i < @nums1; $i++) {
    $d += abs(@snums1[$i] - @snums2[$i]);
    $s += @nums1[$i] * $counts{@nums1[$i]};
}

say $d;
say $s;
