var kmap=
    {A:1, J:1, S : 1,
     B:2, K:2, T : 2,
     C:3, L:3, U :3,
     D:4, M:4, V :4,
     E:5, N:5, W: 5,
     F:6, O:6, X:6,
     G:7, P:7, Y: 7,
     H:8, Q:8, Z: 8,
     I:9, R:9,
     getVal:function(_input){
       var rtrnVal=0;
     for(var tmp=0, len=_input.length;tmp<len;tmp++){
       if(kmap[_input[tmp].toUpperCase()]){
       rtrnVal =rtrnVal+kmap[_input[tmp].toUpperCase()];
       }
     }
       return(rtrnVal);
    }
}
 
console.log(kmap.getVal('myname'));
