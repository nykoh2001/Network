def alter(n: int):
  with open("gen_output.txt", "r") as f:
    lines = f.readlines()
  frame, generator = lines 
  frame = list(frame.strip())
  for i in range(len(frame)):
    if frame[i] == "1":
      frame[i] = "0"
      n -= 1 
    if n == 0: break 
  frame = "".join(frame)
  with open("altered_input.txt", "w") as f:
    f.write(frame + "\n")
    f.write(generator)
  return frame

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
  print("n의 값을 입력하세요:", end="")
  n = int(input())
  alter(n)
  with open("altered_input.txt", "r") as f:
    lines = f.readlines()
  frame, generator = lines 

  remainder = divide(frame.rstrip(), generator)
  print("remainder:", remainder)
  with open("altered_output.txt", "w") as f:
    if remainder == "0" * len(generator):
      f.write("CORRECT")
    else: f.write("WRONG")
  
if __name__ == "__main__":
  main()