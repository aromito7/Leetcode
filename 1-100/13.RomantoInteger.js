/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    sum = 0
    values = { 'I' : 1,
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000}

    for(let i = 0; i < s.length - 1; i++){
        const current = values[s[i]]
        const next  = values[s[i+1]] 
        
        if(current < next){
            sum -= current
        }else{
            sum += current
        }
    }
    sum += values[s[s.length - 1]]

    return sum
};
