function sub() {
    console.log("sub function內b在宣告處之前應該等於多少？")
    console.log(b)

    var a = 10
    var b = 1
    if(a<100) { b=a}
    console.log("sub function內b應該等於多少？")
    console.log(b)
  }
  try {
    sub()
    console.log("sub function外b應該等於多少？")
    console.log(b)
  } catch (e) {
      console.log("Error: " + e.message)
  }

var latter

function outter() {
    var c = 15

    console.log("outter呼叫內部函式inner在定義宣告inner(x)之前!")
    console.log("inner(7) = " + inner(7))

    function inner(x=c) {
        return x*x
    }

    latter = inner //建立閉包
    console.log("outter呼叫內部函式inner在定義宣告inner(x)之後!")
    console.log("inner() = " + inner())
}

outter()
console.log("用閉包latter()呼叫inner() : " )
console.log(latter())
console.log("用閉包latter(8)呼叫inner(8) : " )
console.log(latter(8))

try {
    console.log("從outter外呼叫內部函式inner() : ")
    console.log(inner())
} catch(e) {
    console.log("Error: " + e.message)
}