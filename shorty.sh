cat linker.csv | parallel --pipe -L 1000 -N1 python amount_guesser_pipe.py
