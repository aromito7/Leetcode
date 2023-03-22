/**
 * @param {character[][]} grid
 * @return {number}
 
     let status = grid[0][0]
    let count = 0
    let [x, y] = [0, 0]
    const visitted = new Set([JSON.stringify([0, 0])])
    const stack = [[0, 0]]
    
    
    while(stack.length > 0){
        [x, y] = stack.pop()
        if(status != grid[y][x]){
            if(status === '1'){
                count++
            }
            status = grid[y][x]
        }
        //console.log([x, y], status, grid[y][x], count)
        
        const neighbors = [[-1, 0],[1, 0], [0, -1], [0, 1]].map(([dx, dy]) => [x + dx, y + dy]).filter(([x, y]) => x >= 0 && y >= 0 && x < grid[0].length && y < grid.length)
        
        neighbors.forEach(([x, y]) => {
            if(!visitted.has(JSON.stringify([x, y]))){
                visitted.add(JSON.stringify([x, y]))
                if(grid[y][x] === '1'){
                    stack.push([x, y])
                }else{
                    stack.unshift([x, y])
                }
            }
        })
    }
        
    if(grid[y][x] === "1") count++
    
    return count
*/

/*
var validNeighbors = function(x, y, grid){
    // const delta1 = [[-1, 0],[1, 0], [0, -1], [0, 1], [0, 0]]
    // let neighbors = delta1.map(([dx, dy]) => [x + dx, y + dy])
    // return neighbors.filter(([x, y]) => x >= 0 && y >= 0 && x < grid[0].length && y < grid.length)
    
    return [[-1, 0],[1, 0], [0, -1], [0, 1]].map(([dx, dy]) => [x + dx, y + dy]).filter(([x, y]) => x >= 0 && y >= 0 && x < grid[0].length && y < grid.length)
}

var eliminate = function (x, y, grid){
    let output = 0
    if(grid[y][x] === 1) {
        grid[y][x] = 1
        return 1
    }
    grid[y][x] = 0
    let [dx, dy] = [null, null]
    const delta1 = [[-1, 0],[1, 0], [0, -1], [0, 1], [0, 0]]
    
    validNeighbors(x, y, grid).forEach(([dx, dy]) => {
        if(grid[dy][dx] > 0){
            grid[dy][dx]--
            if(grid[dy][dx] < 3) {
                output = eliminate(dx, dy, grid)
                return
            }
        }
    })
    return output
}
var numIslands = function(grid) {
    const matrix = Array(grid.length + 2).fill().map(() => Array(grid[0].length + 2).fill(0))
    let count = 0
    
    for(let y = 0; y < grid.length; y++){
        for(let x = 0; x < grid[y].length; x++){
            const neighbors = validNeighbors(x, y, grid)
            matrix[y+1][x+1] = grid[y][x] * neighbors.reduce((acc, [dx, dy]) => acc + Number(grid[dy][dx]), 0)
        }
    }
    
    for(let y = 0; y < matrix.length; y++){
        for(let x = 0; x < matrix[y].length; x++){
            if(matrix[y][x] === 1 || matrix[y][x] === 2) {
                //console.log(count, matrix.slice(1, matrix.length - 1).map(row => row.slice(1, row.length -1)))
                count += eliminate(x,y, matrix)
                //console.log(count, matrix.slice(1, matrix.length - 1).map(row => row.slice(1, row.length -1)))
            }
        }
    }
    
    for(let y = 1; y < matrix.length; y++){
       for(let x = 1; x < matrix[y].length; x++){
           if(matrix[y][x] > 0){
               //console.log(count, matrix.slice(1, matrix.length - 1).map(row => row.slice(1, row.length -1)))
               if(matrix[y][x] === 1){
                   count++
               }
               matrix[y+1][x]--
               matrix[y][x+1]--
           }
           matrix[y][x] = 0
       } 
    }
    
    
    return count
}
*/
var eliminateIsland = function(x, y, grid){
    let current = [x, y]
    let stack = [current]
    
    while(stack.length > 0){
        [x, y] = stack.pop()
        const neighbors = [[-1, 0],[1, 0], [0, -1], [0, 1]].map(([dx, dy]) => [x + dx, y + dy]).filter(([x, y]) => x >= 0 && y >= 0 && x < grid[0].length && y < grid.length)
        
        neighbors.forEach(([dx, dy]) => {
            if(grid[dy][dx] === '1'){
                stack.push([dx, dy])
                grid[dy][dx] = '0'
            }
        })
    }
}

var numIslands = function(grid) {
    let count = 0
    for(let y = 0; y < grid.length; y++){
        for(let x = 0; x < grid[y].length; x++){
            if(grid[y][x] === '1'){
                eliminateIsland(x, y, grid)
                count++
            }
        }
    }
    return count
}
