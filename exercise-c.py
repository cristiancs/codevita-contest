n_rights = float(input())
n_lefts = float(input())
right_ahead = float(input())
left_ahead = float(input())
distance = float(input())
pit_dist = float(input())
right_pit_time = float(input())
left_pit_time = float(input())
speed = float(input())

ahead = (n_rights * right_ahead) - (n_lefts * left_ahead)

n_pits = distance / pit_dist
if (n_pits == int(n_pits)):
    n_pits -= 1


delay = right_pit_time - left_pit_time
speed_m_s = speed / 3.6

if (delay != 0):
    ahead -= speed_m_s * delay * n_pits

trunc = False
if (ahead != int(ahead)):
    trunc = True

message = ""

if (ahead > 0):
    if trunc:
        ahead = int(ahead) + 1
    message = "Right Hand driver wins race by "+str(int(ahead))+" meters"
elif (ahead < 0):
    if trunc:
        ahead = int(ahead) - 1
    message = "Left Hand driver wins race by " + str(int(-ahead)) + " meters"
else:
    message = "Race Drawn"

print(message)

