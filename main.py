import math

'''
baselength (bordered) = (4*x + 1)
baselength = (4*x - 1)
'''

threshold = 4

n = int(input(f"Enter a number greater than {threshold}: "))

while n <= threshold:
  n = int(input(f"Enter a number greater than {threshold}: "))

buffer = 0

if (n%2==0):
  buffer = 1

base_length = 4 * n - 1

door_width = n + buffer
window_rows = door_height = n

crown_rows = 3

door_base_length = base_length - 2

door_header_break_length = door_base_length

crown_base_length = door_header_break_length - (n) * 2

window_row_smallest_row = crown_base_length + 2


def renderCrown():
  filler_length = (crown_base_length - (2 * 3 + 1)) // 2
  filler = "_" * filler_length
  icon = "◊"
  filler_icon = "‰"
  spacing = " " * (n + 1)
  icon_filler = filler_icon * ((crown_base_length - 1) // 2)

  print(f'{spacing}\\({filler}({"{" + icon + "}"}){filler})/')
  print(f'{spacing}({(icon_filler*2)+filler_icon})')
  print(f'{spacing}({icon_filler}{icon}{icon_filler})')


def renderWindows():
  icon = "§"
  for i in range(n):
    row_length = crown_base_length + ((i + 1) * 2)
    spacing = " " * (n - i)

    window_filler_num = (2*(math.ceil((i + 1) / 3) - 1))

    window_length = 1 + (window_filler_num)

    filler_length = (row_length - (window_length + 2)) // 2

    filler = icon * filler_length

    window = "[" + "." * window_length + "]"
    print(f'{spacing}|{filler}{window}{filler}|')
    print(f'{spacing}|{"="*row_length}|')


def renderBase():
  door_header_break_icon = "…"
  door_header_break_boundary_icon = "¡"
  door_header_break_filler = door_header_break_icon*door_header_break_length
  spacing = " "

  print(f'{spacing}{door_header_break_boundary_icon}{door_header_break_filler}{door_header_break_boundary_icon}')

  door_start_filler_icon = "¯"
  door_end_filler_icon = "_"
  door_middle_filler_icon = " "
  door_base_filler_top = "‡"
  door_base_filler_bottom = "≈"
  door_base_filler_middle = ":"
  base_filler_icon = "°"

  base_filler = base_filler_icon*base_length

  for i in range(door_height):
    door_base_filler_length = (door_header_break_length - (door_width + 2)) // 2
    door_base_filler_icon = door_base_filler_middle
    door_filler_icon = door_middle_filler_icon

    if (i==0):
      door_base_filler_icon = door_base_filler_top
      door_filler_icon = door_start_filler_icon
    elif (i==(n-1)):
      door_base_filler_icon = door_base_filler_bottom
      door_filler_icon = door_end_filler_icon
    
    door_base_filler = door_base_filler_icon*door_base_filler_length
    door_filler = door_filler_icon*door_width
    
    print(f'{spacing}|{door_base_filler}|{door_filler}|{door_base_filler}|')
  print(f':{base_filler}:')
  

renderCrown()
renderWindows()
renderBase()
