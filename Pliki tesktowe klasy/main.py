
import sys

from ChangeFIle import ChangeFile
from WriteFile import WriteFile


message="Za malo parametrow 1 do plik do czytania drugi plik zapisu 3 to pozycja wiersza 4 pozycja kolumny  5 to wartosc"
if len(sys.argv) > 1:
    infile=sys.argv[1]
else:
    sys.exit(message)

if len(sys.argv) > 2:
    outfile=sys.argv[2]
else:
    sys.exit(message)
if len(sys.argv) > 3:
    posX=int(sys.argv[3])
else:
    sys.exit(message)

if len(sys.argv) > 4:
    posY=int(sys.argv[4])
else:
    sys.exit(message)

if len(sys.argv) > 5:
    value=sys.argv[5]
else:
    print(message)
    sys.exit(message)
if len(sys.argv) <1:
    sys.exit(message)

change=ChangeFile(infile,"")
change.changePOS(posX,posY,value)
change.printOut()

writer=WriteFile(outfile,change.lines)


