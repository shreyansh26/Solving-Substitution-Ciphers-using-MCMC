# Solving Substitution Ciphers using Markov Chain Monte Carlo (MCMC)

I have written about the explanation of the algorithm and the code in this [blog post](https://shreyansh26.github.io/post/2023-07-22_solving_substitution_cipher_using_mcmc/).

* [prep_freq_counts.py](prep_freq_counts.py) - Bigram frequency/probability calculation  
* [solve_cipher.py](solve_cipher.py) - Solve the substitution cipher given in [ciphertext.txt](ciphertext.txt) using MCMC and compare it with the plaintext given in [plaintext.txt](plaintext.txt).

## To run

```bash
pip install -r requirements.txt
python prep_freq_counts.py
python solve_cipher.py
```

