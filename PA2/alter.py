import sys

def alter(n: int):
  # 왼쪽부터 n개의 1을 0으로 바꿈
  with open("./text/gen_output.txt", "r") as f:
    lines = f.readlines()
  frame, generator = lines 
  frame = list(frame.strip())
  # 1을 0으로 변경
  for i in range(len(frame)):
    if frame[i] == "1":
      frame[i] = "0"
      n -= 1 
    if n == 0: break 
  frame = "".join(frame)
  with open("./text/altered_input.txt", "w") as f:
    f.write(frame + "\n")
    f.write(generator)
  return frame

#generator, verifier와 동일한 XOR, divide
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
  # shell의 입력 파라미터로 전달 받은 n
  n = int(sys.argv[1])
  print("n =", n)

  alter(n)
  with open("./text/altered_input.txt", "r") as f:
    lines = f.readlines()
  frame, generator = lines 

  remainder = divide(frame.rstrip(), generator)
  print("remainder:", remainder)
  with open("./text/altered_output.txt", "w") as f:
    # verifier와 동일하게 나머지가 모두 0이면 맞고, 그렇지 않으면 에러 발생
    if remainder == "0" * len(generator):
      print("CORRECT")
      f.write("CORRECT")
    else: 
      print("WRONG")
      f.write("WRONG")
  
if __name__ == "__main__":
  print("ALTER")
  main()