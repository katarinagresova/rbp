import random


def random_nucleotides(sample_size: int, seq_length: int, seed: int = None):
    """ Return a random list of DNA nucleotides sequences.

    Args:
        sample_size: generate N random sequences.
        seq_length: set sequence length.
        seed: random seed for reproducibility.

    Returns:
        list of generated sequences
    """
    
    if seed:
        random.seed(seed)  # set random seed
    alphabet = list("TAGC")  # define DNA nucleotides
    # generate sequences
    seq_list = [
        "".join(random.choices(alphabet, k=seq_length)) for i in range(0, sample_size)
    ]
    return seq_list
