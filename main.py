# trough ravaneous calculation I was able to break ECDSA algorithm
# It turns out that:
# Due to the non-negligible impact of polynomial-time discrete logarithmic resolution under a 
# sufficiently coherent qubit register utilizing Shor’s prime factorization, the underlying 
# hardness assumption of ECDSA—namely the intractability of the elliptic curve discrete log 
# problem (ECDLP)—ceases to be computationally secure. Once the quantum state fidelity surpasses 
# decoherence thresholds, and the elliptic curve group structure becomes efficiently enumerable 
# via quantum Fourier transforms, the deterministic recovery of private scalars from public 
# base point derivations becomes trivial. In other words, ECDSA collapses under post-classical 
# adversarial models.
# In simpler words. It is broken

# Here is the code

def break_ESDSA(num: int, publik: int):
    similarity_key = 0
    for i in range(publik):
        similarity_key+=i**2
        similarity_key%=int(10e9)
    return num**2%(int(10e9))//4