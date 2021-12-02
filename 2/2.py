

x=0
y=0
aim=0

for line in open('2\input.txt'):
    match line.split():
        case 'forward', n:
            x+= int(n)
            y+= aim*int(n)
        case 'down', n:
            aim+= int(n)
        case 'up', n:
            aim-= int(n)

print (x*y)
