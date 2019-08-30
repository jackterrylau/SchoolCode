//Implement Javascript function with required parameters.

// Approach 1. Check undefined value method.(檢查參數法)
function testMethod1(x,y) {
    if (x===undefined && y===undefined) {throw new Error("Parameter x and y is required")}
    if (x===undefined) {throw new Error("Parameter x is required")}
    if (y===undefined) {throw new Error("Parameter y is required")}

    return x+y
}

// Approach 2. Parameter with exception method.(參數預設值強制丟出異常法)
function throwRequiredException() {
    throw new Error("Missing parameter") 
}

function testMethod2(a=throwRequiredException()) {
    return a*a;
}

// test function

try {
    testMethod1(1)
} catch (e) { 
    console.log("testMethod1(1) : " + e.message)
}

try {
    testMethod1()
} catch (e) { 
    console.log("testMethod1() : " + e.message)
}

console.log("testMethod1(1,2) = " + testMethod1(1,2))

try {
    testMethod2()
} catch (e) { 
    console.log("testMethod2() : " + e.message)
}

try {
    testMethod2(undefined)
} catch (e) { 
    console.log("testMethod2(undefined) : " + e.message)
}

console.log("testMethod2(3) = " + testMethod2(3))

