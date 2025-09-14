import random

def get_random_int(min_val, max_val):
    return random.randint(min_val, max_val)


def computerMove(n,winningLines,moves):
    boardSize=n*n
#     let move;
    if len(moves)==0:
        move= get_random_int(0,boardSize-1)
        linePicked = winningLines[move]
#     }
#     else {
#         for (const line of winningLines) {
#             if (linePicked.length>0){
#                 const values = linePicked.map(key => moves.get(key));
#                 const unique = new Set(values);
#                 if (!unique.has("o")){
#                     for (let r = 0; r < values.length; r++) {
#                         if (values[r] === undefined)
#                             move=linePicked[r];
#                     }
#                     break;
#                 }
#             }
#
#             const values = line.map(key => moves.get(key));
#             const unique = new Set(values);
#             if (unique.has(undefined) && unique.has("x")){
#                 //let index=getRandomFloat(1,values.length);
#                 //if (!unique.has("o"))
#                 {
#                     for (let r = 0; r < values.length; r++) {
#                         if (values[r] === undefined)
#                             move=line[r];
#                     }
#                 }
#                 linePicked=line;
#                 break;
#             }
#         }
#     }
#     let btn=document.getElementById(String(move));
#     if (btn){
#         if(!btn.disabled) {
#             btn.disabled=true;
#             btn.innerHTML="x";
#             moves.set(move,"x");
#         }
#     }
#
#     //console.log(btn);
#     //console.log(move);
#
# }