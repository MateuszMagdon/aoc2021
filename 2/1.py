

x=0
y=0

for line in open('2\input.txt'):
    match line.split():
        case 'forward', n:
            x+= int(n)
        case 'down', n:
            y+= int(n)
        case 'up', n:
            y-= int(n)

print (x*y)
