//Test arraw_function

//const : the referece of object can't be changed.
const nums = [1,2,3,4,5,6,7,8,9,10];

/*
  Array.forEach() is the high level function of Array object.
  What is High Level Function?
  1. Accept 1 to more functions to be parameters.
  2. Output a function object.
  
  Array.forEach() can actively pass array's element to callback function with the sequence (Array_Item,Array_Index,Array) when callback function has 1-3 parameters.
  
*/

/*
  arrow function syntax:
  1. (arg_1,arg_2,.....) => { statement(arg_1,arg_2); }  左邊括號內的參數會直接傳遞到箭號右邊的 function block內
  2. arg_1 => {statement(arg_1);} 只有一個參數時，右邊的括號可以省略
  3. arg_1 => statement(arg_1)  當function statement 沒有加大括號時，代表直接 return statement(arg_1)
  4. () => {statement();}  沒有參數時的arrow function。
*/

console.log("Test arrow function with forEach() function.");
nums.forEach( v => {
    if(v%2 == 0) console.log(v);
	}
);

console.log("Test arrow function adopts 2-parameter callback style with forEach() function.");

const callback = (item, index) => {
  if (index%2 === 0) return;
  // `${index}` : backticks is used to covert varibles/expressions 'index' result into a string.
  console.log(`Array Index ${index} value is ${item}`);
}

nums.forEach(callback);

/*
array.map() 方法是什麼？他允許我們把原有的陣列映射到另外一個新的陣列，在回調函數裡面你只要給定條件，它就能對應的東西映射進去。
array.map() 會把陣列內所有 element 經過 callback 函數加工後 產生新的陣列物件。
*/

console.log("使用 array.map() 函數把原陣列物件全部 element 的值 +1 並列印出該兩個陣列內容.");

//let : the referece of object is mutable.
let new_nums = [];

new_nums = nums.map( item => item+1 );

console.log("original array = [" + nums.toString() + "]");
console.log("new      array = [" + new_nums.toString() + "]");

/*
array.filter() 可以把陣列的element 符合特定條件的element 篩選出來或過濾掉 然後產生新的陣列物件。
*/

console.log("使用 array.filter() 函數過濾掉原陣列物件中 year <= 18 的人，並列印出新陣列內容.");
const yearlist = [{name:'Mary', year:35},{name:'Shirly', year:12},{name:'Angel', year:18},{name:'Vivian',year:'15'},{name:'Vera', year:27}];
let under18 = yearlist.filter( girl => girl.year <= 18);

under18.forEach( girl => {console.log( `The girl ${girl.name} is ${girl.year} years old.`)});


