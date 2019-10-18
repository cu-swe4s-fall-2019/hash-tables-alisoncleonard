python hash_functions.py rand_words.txt ascii | python scatter.py ascii_hash_function_rand.png "Hashed word" "Hashed value"

python hash_functions.py rand_words.txt rolling | python scatter.py rolling_hash_function_rand.png "Hashed word" "Hashed value"

python hash_functions.py rand_words.txt python | python scatter.py python_hash_function_rand.png "Hashed word" "Hashed value"

python hash_functions.py non_rand_words.txt ascii | python scatter.py ascii_hash_function_non_rand.png "Hashed word" "Hashed value"

python hash_functions.py non_rand_words.txt rolling | python scatter.py rolling_hash_function_non_rand.png "Hashed word" "Hashed value"

python hash_functions.py non_rand_words.txt python | python scatter.py python_hash_function_non_rand.png "Hashed word" "Hashed value"

# test ascii linear
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py 10000 ascii linear rand_words.txt $M >  ascii_linear_rand.$M.txt
done

grep add ascii_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py ascii_linear_add_time.png "Load factor" "Add time"

(for M in $( seq  1000 1000 10000 ); do
    load_factor=$(bc -l <<< "$M/10000")
    echo -n "$load_factor "
    grep search ascii_linear_rand.$M.txt | cut -d " " -f2 | python mean.py
done) | python scatter.py ascii_linear_search_time.png "Load factor" "Search time"

# test ascii chain
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py 10000 ascii chain rand_words.txt $M >  ascii_chain_rand.$M.txt
done

grep add ascii_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py ascii_chain_add_time.png "Load factor" "Add time"

(for M in $( seq  1000 1000 10000 ); do
    load_factor=$(bc -l <<< "$M/10000")
    echo -n "$load_factor "
    grep search ascii_chain_rand.$M.txt | cut -d " " -f2 | python mean.py
done) | python scatter.py ascii_chain_search_time.png "Load factor" "Search time"

# test rolling linear
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py 10000 rolling linear rand_words.txt $M >  rolling_linear_rand.$M.txt
done

grep add rolling_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py rolling_linear_add_time.png "Load factor" "Add time"

(for M in $( seq  1000 1000 10000 ); do
    load_factor=$(bc -l <<< "$M/10000")
    echo -n "$load_factor "
    grep search rolling_linear_rand.$M.txt | cut -d " " -f2 | python mean.py
done) | python scatter.py rolling_linear_search_time.png "Load factor" "Search time"

# test rolling chain
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py 10000 rolling chain rand_words.txt $M >  rolling_chain_rand.$M.txt
done

grep add rolling_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py rolling_chain_add_time.png "Load factor" "Add time"

(for M in $( seq  1000 1000 10000 ); do
    load_factor=$(bc -l <<< "$M/10000")
    echo -n "$load_factor "
    grep search rolling_chain_rand.$M.txt | cut -d " " -f2 | python mean.py
done) | python scatter.py rolling_chain_search_time.png "Load factor" "Search time"
