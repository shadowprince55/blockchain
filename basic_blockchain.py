# Just to get a hang of how stuff works

import hashlib

class NeuralCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "A sends 2 NC to M"
t2 = "B sends 4.1 NC to M"
t3 = "M sends 3.2 NC to B"
t4 = "D sends 0.3 NC to A"
t5 = "M sends 1 NC to C"
t6 = "M sends 5.4 NC to D"

initial_block = NeuralCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NeuralCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)

