# generator와 동일하게 구현된 XOR, divide
def XOR(frame:str, dividor: str) -> str:
  frame_len, dividor_len = len(frame), len(dividor)
  frame = list(frame.strip())
  dividor = list(dividor.strip())
  if frame[0] == "0":
    dividor = "0" * dividor_len
  else: dividor = dividor
  print("frame:", "".join(frame), ", dividor:", "".join(dividor))
  for i in range(1, dividor_len + 1):
    frame[frame_len - i] = str(int(dividor[dividor_len - i] != frame[frame_len - i]))
  return "".join(frame)

def divide(frame:str, gen:str) -> str:
  len_frame: int = len(frame)
  len_gen: int = len(gen)
  dividor = frame[:len_gen]
  for i in range(len_gen, len_frame):
    dividor = XOR(dividor, gen)
    dividor = dividor[1:] + frame[i]
  output_frame = XOR(frame, dividor)

  return dividor
    

def main():
  with open("./text/gen_output.txt", "r") as f:
    lines = f.readlines()
  frame, generator = lines 

  remainder = divide(frame.rstrip(), generator)
  print("remainder:", remainder)
  with open("./text/veri_output.txt", "w") as f:
    # 나머지 값이 전부 0이면 옳은 프레임, 그렇지 않으면 에러 발생
    if remainder == "0" * len(generator):
      print("CORRECT")
      f.write("CORRECT")
    else: 
      print("WRONG")
      f.write("WRONG")
  
if __name__ == "__main__":
  print("VERIFIER")
  main()
  print()