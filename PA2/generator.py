def padding(frame: str, r: int) -> str:
  return frame + r * "0"

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
  print("output frame:", output_frame, ", poly:", gen)
  return output_frame, gen
    

def main():
  with open("Input.txt", "r") as f:
    lines = f.readlines()
  frame, generator = lines 
  padded_frame = frame.rstrip() + "0" * (len(generator) - 1)
  print("padded:",padded_frame)
  E_x, gen = divide(padded_frame, generator)
  with open("gen_output.txt", "w") as f:
    f.write(E_x + "\n")
    f.write(gen)
  
if __name__ == "__main__":
  main()