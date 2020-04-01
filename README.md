# dnaProfile
(Python) Program profiles a DNA sample for a variety of consecutive Short Tandem Repeats (STRs) sequences and matches results against a database to determine identity of an individual.


To run the file, input the name of the file (dna.py) followed by 2 arguments:
- name of the database being used (small.csv or large.csv)
- name of the sequence pattern (ex: sequences/5.txt)

Ex:

> python dna.py databases/large.csv sequences/5.txt


### How it works

"One place where DNA tends to have high genetic diversity is in Short Tandem Repeats (STRs). An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person’s DNA. The number of times any particular STR repeats varies a lot among individuals.

Using multiple STRs, rather than just one, can improve the accuracy of DNA profiling. If the probability that two people have the same number of repeats for a single STR is 5%, and the analyst looks at 10 different STRs, then the probability that two DNA samples match purely by chance is about 1 in 1 quadrillion (assuming all STRs are independent of each other). So if two DNA samples match in the number of repeats for each of the STRs, the analyst can be pretty confident they came from the same person. CODIS, The FBI’s DNA database, uses 20 different STRs as part of its DNA profiling process."


*database imported from Harvard CS50 ProblemSet
