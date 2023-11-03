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

class Receiver:
  # reveiver process
  def __init__(self,chip_sequence: list):
    # standard: 해석된 원래 비트
    # chip_sequence: 리시버의 칩 시퀀스
    self.standard = None
    self.chip_sequence = chip_sequence
    
  def receive(self, joined: list) -> int:
    print("Receiving ...")
    # 내적하여 원래 비트를 추출
    print("Joned sequence · chip sequence = ", joined,"·", self.chip_sequence)
    result = np.matmul(np.array(joined),np.array(self.chip_sequence))
    print("Inner product:", result // 8 , "\n")
    return result // 8

class Transmitter:
  # Transmit process
  def __init__(self, chip_sequence: []) -> None:
    # transmitted: 여러 개로 쪼개진 하나의 비트
    # chip_sequence: 트랜스미터의 칩 시퀀스
    self.transmitted = []
    self.chip_sequence = chip_sequence
      
  def transmit(self, stand: int):
    # 비트가 1이면 그대로, -1이면 시퀀스를 구성하는 원소들에 -1을 곱한 후 반환
    print("Transmitting ...")
    if stand == 1:
      return self.chip_sequence
    return [-1*int(cs) for cs in self.chip_sequence]

class Joiner:
  # join process
  def __init__(self, _input:list):
    # input_bits: 입력으로 들어온 비트
    # chip_sequences: 4개의 스테이션에 해당하는 칩 시퀀스들
    # transmitters: t0~t3
    # receivers: r0~r3
    # joined: 합쳐진 4개의 시퀀스
    # origin_bits: 리시버로부터 해석되어 반환된 원래 입력 비트
    self.input_bits = _input
    self.chip_sequences = []
    for _ in range(4):
      self.make_chip_sequence()
    
    self.transmitters = [Transmitter(chip_sequence=self.chip_sequences[i]) for i in range(4)]
    self.receivers = [Receiver(chip_sequence=self.chip_sequences[i]) for i in range(4)]
    self.joined = [0 for _ in range(8)]
    self.origin_bits = []
    
  def make_chip_sequence(self):
    # pairwise orthogonal한 비트 시퀀스 생성
    # 1 네개, -1 네개로 구성
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
    # 네 개 시퀀스 합치기
    for i in range(4):
      #트랜스미터로부터 변환 결과 반환 받음
      current_trans = self.transmitters[i].transmit(self.input_bits[i])
      for j in range(8):
        self.joined[j] = self.joined[j] + current_trans[j]
    print("joined sequence:", self.joined, "\n")
    
    # 리시버로부터 받아서 원래 비트 추출
    for i in range(4):
      self.origin_bits.append(max(0, self.receivers[i].receive(self.joined)))
    return self.origin_bits

def __main__():
  # Input Bits 생성
  input_sequence = list(product([1, 0], repeat=4))
  input_sequence = random.choice(input_sequence)
  print("Input Bits:", input_sequence, "\n")
  
  # Joiner 생성 및 실행
  joiner = Joiner(input_sequence)
  origin_bits = joiner.join()

  for i in range(4):
    print(f"station {i}: {origin_bits[i]}")
  print("=>", ", ".join(map(str, origin_bits)))
  
__main__()