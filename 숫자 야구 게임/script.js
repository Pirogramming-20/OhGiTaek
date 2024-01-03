const num1 = document.getElementById('number1');
const num2 = document.getElementById('number2');
const num3 = document.getElementById('number3');
const submmmit_btn = document.querySelector('button');
const result_display = document.querySelector('.result-display');
const img = document.getElementById('game-result-img');
let num_list = [num1.value,num2.value,num3.value];

// 시도가능횟수설정
let trynum = 9;

// 랜덤값 부여
let random_list = [];
let input_list=[];
let random_num, check, ex_remove, order, input_num;
let s_count = 0;
let b_count = 0; 

for (i=0; i<33; i++) {
  random_num = Math.floor(Math.random() * 9)
  if (random_list.indexOf(random_num) === -1) {
    random_list.push(random_num)
  }
  if(random_list.length == 3) break;
}
console.log(random_list);


// Enter키에 반응하여 입력이 되도록 설정
num1.addEventListener('keypress',(event) =>{
  if (event.code == 'Enter'){
    console.log('press');
    check_numbers();
  }
})
num2.addEventListener('keypress',(event) =>{
  if (event.code == 'Enter'){
    console.log('press');
    check_numbers();
  }
})
num3.addEventListener('keypress',(event) =>{
  if (event.code == 'Enter'){
    console.log('press');
    check_numbers();
  }
})


// 빈칸인 상태에서 backspace 입력 시 전칸의 내용을 지우고 포커스를 전칸으로 옮김
num2.addEventListener('keydown',(event) =>{
  if (event.code == 'Backspace' && num2.value ==''){
    console.log('back');
    num1.focus();
    num1.value = '';
  }
})
num3.addEventListener('keydown',(event) =>{
  if (event.code == 'Backspace' && num3.value ==''){
    console.log('back');
    num2.focus();
    num2.value = '';
  }
})


// 초기값 설정
window.onload=function(){
  for(let k = 0; k < 3; k++){
    // check = document.getElementsByClassName('check-result');
    // if(!check){
    //   break;
    // }
    // console.log(1);
    ex_remove = document.querySelector('.check-result');
    ex_remove.remove();
  }
  num1.focus();
}


// 입력에 따른 결과 출력
function check_numbers()  {
  s_count = 0;
  b_count = 0; 
  num_list = [num1.value,num2.value,num3.value];


  

  // 1자리 or 2자리만 입력할 경우 초기화
  if (num1.value == '' || num2.value == '' || num3.value == ''){
    num1.value = "";
    num2.value = "";
    num3.value = "";
    num1.focus();
    return ;
  }

  // console.log(typeof num1.value)
  console.log(isNaN(num1.value))
  // 중복된 수가 있을경우 or 숫자가 아닌 수를 입력할 경우 잘못된경우로 예외처리 및 재입력하도록 설정
  input_num = num1.value+' '+num2.value+' '+num3.value;
  if (num1.value == num2.value || num1.value == num3.value || num2.value == num3.value 
    || isNaN(num1.value) || isNaN(num2.value) || isNaN(num3.value)){
    num1.value = "";
    num2.value = "";
    num3.value = "";
    console.log('ddd');
    const check_result = document.createElement('div');
    check_result.className = 'check-result';
    const left = document.createElement('div');
    left.className = 'left';
    left.innerText = input_num;
    check_result.append(left,"잘못된 입력 다시 입력하세요");
    result_display.appendChild(check_result);
    return ;
  }


  // 이전에 입력한 수를 다시 입력할 경우 중복된 입력으로 예외 처리 및 재입력하도록 설정
  if(input_list.includes(input_num)){
    num1.value = "";
    num2.value = "";
    num3.value = "";

    const check_result = document.createElement('div');
    check_result.className = 'check-result';
    const left = document.createElement('div');
    left.className = 'left';
    left.innerText = input_num;
    check_result.append(left,"중복된 입력 다시 입력하세요");
    result_display.appendChild(check_result);
    return ;
  }
  console.log(input_list.includes(input_num));
  input_list.push(input_num);
  console.log(input_list);


  //결과판단
  for(let n = 0; n < 3; n++){
    for (let m =0; m < 3; m++){
      if(num_list[n]==random_list[m]){
        if(n==m) s_count++;
        else b_count++;
      }
    }
  }

  // 결과 출력
  if(s_count == 0 && b_count == 0){
    const check_result = document.createElement('div');
    check_result.className = 'check-result';

    const left = document.createElement('div');
    left.className = 'left';
    left.innerText = input_num;
    const right = document.createElement('div');
    right.className = 'out num-result';
    right.innerText = 'O';

    check_result.append(left , ":", right);
    result_display.appendChild(check_result);
  }else{
    const check_result = document.createElement('div');
    check_result.className = 'check-result';

    const left = document.createElement('div');
    left.className = 'left';
    left.innerText = input_num;
    const right = document.createElement('div');
    right.className = 'right';
    const ss = document.createElement('div');
    ss.className = 'strike num-result';
    ss.innerText = 'S';
    const bb = document.createElement('div');
    bb.className = 'ball num-result';
    bb.innerText = 'B';

    right.append(s_count,ss,b_count,bb);
    check_result.append(left , ":", right);
    result_display.appendChild(check_result);
  }

  if(s_count == 3){
    img.src = "success.png";
    submmmit_btn.disabled = true;
    return;
  }
  
  //input값 초기화
  num1.value = "";
  num2.value = "";
  num3.value = "";
  trynum --;
  if(trynum == 0){
    img.src = "fail.png";
    submmmit_btn.disabled = true;
  }
  result_display.scrollTop = result_display.scrollHeight;

}
