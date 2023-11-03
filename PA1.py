# CDMA 프로그래밍
# chip sequence length = 8
# station 4
# process 
# 1. transmitter process x 4 (t0~t3)
# 2. joiner process
# 3. receiver process x 4 (r0~r3)

import random
import numpy as np 
from itertools import permutations, product
import random

def get_ones_position() -> list:
  return random.sample(range(8), 4)

class Receiver:
  def __init__(self,chip_sequence: list):
    self.standard = None
    self.chip_sequence = chip_sequence
    
  def receive(self, joined: list) -> int:
    print("Receiving ...")
    print("Joned sequence · chip sequence = ", joined,"·", self.chip_sequence)
    result = np.matmul(np.array(joined),np.array(self.chip_sequence))
    print("Inner product:", result // 8 , "\n")
    return result // 8

class Transmitter:
  def __init__(self, chip_sequence: []) -> None:
    self.transmitted = []
    self.chip_sequence = chip_sequence
      
  def transmit(self, stand: int):
    print("Transmitting ...")
    if stand == 1:
      return self.chip_sequence
    return [-1*int(cs) for cs in self.chip_sequence]

class Joiner:
  def __init__(self, _input:list):
    self.input_bits = _input
    self.chip_sequences = []
    for _ in range(4):
      self.make_chip_sequence()
    
    self.transmitters = [Transmitter(chip_sequence=self.chip_sequences[i]) for i in range(4)]
    self.receivers = [Receiver(chip_sequence=self.chip_sequences[i]) for i in range(4)]
    self.joined = [0 for _ in range(8)]
    self.origin_bits = []
    
  def make_chip_sequence(self):
    _permutations = list(set(permutations([1, 1, 1, 1, -1, -1, -1, -1])))
    cnt = 0
    for seq in _permutations:
      is_orthogonal = True
      for existing_seq in self.chip_sequences:
          dot_product = np.dot(seq, existing_seq)
          if dot_product != 0:
              is_orthogonal = False
              break
      if is_orthogonal:
          self.chip_sequences.append(seq)
          cnt += 1
          # print("Chip Sequence:", seq)
      if cnt == 4:
        for s in self.chip_sequences:
          print("Chip Sequence:", s)
        print()
        return
  
  def join(self):
    print("Joining ...")
    for i in range(4):
      current_trans = self.transmitters[i].transmit(self.input_bits[i])
      for j in range(8):
        self.joined[j] = self.joined[j] + current_trans[j]
    print("joined sequence:", self.joined, "\n")
    
    for i in range(4):
      self.origin_bits.append(max(0, self.receivers[i].receive(self.joined)))
    return self.origin_bits

def __main__():
  input_sequence = list(product([1, 0], repeat=4))
  input_sequence = random.choice(input_sequence)
  print("Input Bits:", input_sequence, "\n")
  joiner = Joiner(input_sequence)
  origin_bits = joiner.join()

  for i in range(4):
    print(f"station {i}: {origin_bits[i]}")
  print("=>", ", ".join(map(str, origin_bits)))
  
__main__()