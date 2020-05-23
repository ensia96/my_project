var num = [1,400,2,4,5,6,7]
var i = 0
var total = 0

while(i<num.length){
  console.log(num[i])
  total += num[i]
  i += 1
}

console.log(`total : ${total}`)