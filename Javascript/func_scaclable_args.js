//示範使用 Rest Parameter 其餘參數語法 定義 不定參數的function

//定義一個會把所有參數相乘後回傳結果的函式
function multiplication(...factors) {
    let result = 1

    factors.forEach(function (number) 
      {
          result = result * number
      }
    )

    return result
}

// Test Function
console.log ("3 * 5 * 2 = " + multiplication(3,5,2))
const arr = [16,5,6]
// 展開運算子(Spread Operator)語法
const f5 = [10,8, ...arr]
console.log("10 * 8 * 16 * 5 * 6 = " + multiplication(...f5)) // 展開運算子(Spread Operator)語法