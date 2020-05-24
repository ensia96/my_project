var members = ['mango', 'mongo', 'haha']
console.log(members[1])
var i = 0;
while (i < members.length) {
  console.log('array loop',members[i])
  i += 1
}

var roles = {
  'programmer':'mango',
  'designer' : 'mongo',
  'manager': 'haha',
}

console.log(roles.programmer)
console.log(roles['programmer'])

for (var n in roles) {
  console.log('object =>',n,  'value =>', roles[n])
}