def padding(frame: str, r: int) -> str:
  # generator 깊이만큼 0 추가
  return frame + r * "0"

def XOR(frame:str, dividor: str) -> str:
  # frame과 dividor에 대해 exclusive or 구하기
  # padding 값에 remainder를 더하는 함수로도 사용될 수 있음 (padding은 전부 0이기 때문)
  frame_len, dividor_len = len(frame), len(dividor)
  frame = list(frame.strip())
  dividor = list(dividor.strip())
  if frame[0] == "0":
    # 현재 나누려는 수가 0으로 시작하는 경우
    # 몫이 0이 되어 나누는 수가 000... 형태가 됨
    dividor = "0" * dividor_len
  # 몫이 1인 경우 dividor 그대로 유지
  else: dividor = dividor
  print("frame:", "".join(frame), ", dividor:", "".join(dividor))
  for i in range(1, dividor_len + 1):
    # 동일 인덱스에 대해 같으면 0, 다르면 1 계산
    frame[frame_len - i] = str(int(dividor[dividor_len - i] != frame[frame_len - i]))
  return "".join(frame)

def divide(frame:str, gen:str) -> str:
  # 한 칸씩 옮겨가면서 나눗셈 진행
  # 나눗셈은 XOR 함수 호출로 구현
  len_frame: int = len(frame)
  len_gen: int = len(gen)
  dividor = frame[:len_gen]
  for i in range(len_gen, len_frame):
    dividor = XOR(dividor, gen)
    dividor = dividor[1:] + frame[i]
  # 최종 frame + remainder
  output_frame = XOR(frame, dividor)
  # padding을 채운 frame에 remainder를 더한 값과 generator 반환
  print("output frame:", output_frame, ", poly:", gen)
  return output_frame, gen
    

def main():
  with open("./text/input.txt", "r") as f:
    lines = f.readlines()
  frame, generator = lines 
  # frame에 padding 채우기
  padded_frame = padding(frame.rstrip(), len(generator) - 1)
  print("padded:",padded_frame)
  E_x, gen = divide(padded_frame, generator)
  with open("./text/gen_output.txt", "w") as f:
    f.write(E_x + "\n")
    f.write(gen)
  
if __name__ == "__main__":
  print("GENERATOR")
  main()
  print()